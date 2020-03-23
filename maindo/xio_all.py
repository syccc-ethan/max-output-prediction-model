from PyQt4 import QtGui, QtCore
import uifiles.xio_all_ui as ui
import sys
import cv2
import threading
import time
import datetime
from utils.utils import Timer, MyQueue
from utils.vision import Vision
import socketserver
import time
from figure.figure_plot import *
from data import data_access


def data_deal(func):  # 要接受参数就要改成三层装饰器
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
    action = None  # 用来通知显示现在是由于什么原因导致静止

    @data_deal
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        # print(data)
        if data == 'action1':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data == 'action2':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data == 'action3':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data == 'action4':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data == 'action5':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data == 'action6':
            dz = data  # 动作
            da = data_access.DataAccess()
            da.insert_action(dz)
            action = data
        elif data[0:4] == 'stop':
            dz = data[4:]
            da = data_access.DataAccess()
            da.insert_action(dz, FLAG='end')
            # 更新动作表
            result = da.select_("select * from dz ORDER BY SJC DESC limit 2")
            time_diff = int((result[0][0] - result[1][0]).seconds)
            lossTime = data_access.EquipmentTimeData()
            result_loss = lossTime.select_("select * from loss ORDER BY SJ DESC limit 1")
            current_time = datetime.datetime.now().strftime('%Y-%m-%d')
            time_diff = time_diff + result_loss[0][int(dz[-1])]  # 此处投机
            lossTime.update_('update loss set ' + dz + '=' + str(time_diff) + ' where SJ="%s"' % current_time)

            action = None


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class XioAll(QtGui.QWidget):
    '''这个类为主程序类
    '''
    HOST = 'localhost'
    PORT = 8081
    TOTAL = 0
    isStatic = True
    action = None
    pre_action = None
    action_video = None # 视频内能识别
    pre_action_video = None

    def __init__(self):
        super(XioAll, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)

        self.frame_left = None
        self.frame_right = None
        self.is_work = True
        self.one_static_time = 0  # 一次故障静止的时间
        self.all_time = 0  # 一天的工作时间
        self.q = MyQueue()  # 存放帧队列,改为存放状态比较好
        self.vision = Vision()
        # 若日期发生改变，自行插入全零数据
        da = data_access.EquipmentTimeData()  # 对损失项统计表进行操作
        result_loss = da.select_("select * from loss ORDER BY SJ DESC limit 1")
        current_time = datetime.datetime.now().strftime('%Y-%m-%d')
        if str(result_loss[0][0]) != current_time:
            da.update('insert into loss(SJ,action1,action2,action3,action4,action5,action6)values'
                      '("%s",%d,%d,%d,%d,%d,%d)' % (current_time, 0, 0, 0, 0, 0, 0))
        else:
            pass

        da_oee = data_access.OEEData()  # 对oee实时利用率进行统计
        result_oee = da_oee.select_('select * from oee_date ORDER BY SJC DESC limit 1')
        if str(result_oee[0][0]) != current_time:
            da_oee.update_('insert into oee_date(SJC,O8,O9,O10,O11,O12,O13,O14,O15,O16,O17,O18)values'
                           '("' + current_time + '",0,0,0,0,0,0,0,0,0,0,0)')
        else:
            pass
        self.thread_figure = Timer('updatePlay()', sleep_time=120)  # 该线程用来每隔2分钟刷新绘图区
        self.connect(self.thread_figure, QtCore.SIGNAL('updatePlay()'), self.draw)
        self.thread_figure.start()

        self.server = ThreadedTCPServer((self.HOST, self.PORT), ThreadedTCPRequestHandler)  # 该线程用来一直监听客户端的请求
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

        self.thread_video_receive = threading.Thread(target=self.video_receive_local)  # 该线程用来读取视频流
        self.thread_video_receive.start()

        self.thread_time = Timer('updatePlay()')  # 该线程用来每隔0.04秒在label上绘图
        self.connect(self.thread_time, QtCore.SIGNAL('updatePlay()'), self.video_play)
        self.thread_time.start()

        self.thread_recog = Timer('updatePlay()', sleep_time=1)  # 该线程用来每隔一秒分析图像
        self.connect(self.thread_recog, QtCore.SIGNAL('updatePlay()'), self.video_recog)
        self.thread_recog.start()

        self.thread_data = Timer('updatePlay()', sleep_time=1800)  # 该线程用来每隔半小时向数据库读取数据
        self.connect(self.thread_data, QtCore.SIGNAL('updatePlay()'), self.data_read)
        self.thread_data.start()

    def video_receive_local(self, cam1='./videos/left_cam.mp4', cam2='./videos/right_cam.mp4', time_flag=True):
        '''该方法用来接收本地视频
        :param cam1: 左摄像头数据源
        :param cam2: 右摄像头数据源
        :param time_flag: 是否休眠，本地视频为True
        :return: None
        '''
        self.left_cam = cv2.VideoCapture(cam1)
        self.right_cam = cv2.VideoCapture(cam2)
        ret_1, frame_1 = self.left_cam.read()
        ret_2, frame_2 = self.right_cam.read()
        while True:
            self.frame_left = frame_1
            self.frame_right = frame_2
            if ret_1 is False:
                self.left_cam = cv2.VideoCapture(cam1)
            if ret_2 is False:
                self.right_cam = cv2.VideoCapture(cam2)
            ret_1, frame_1 = self.left_cam.read()
            ret_1, frame_2 = self.right_cam.read()
            if time_flag is True:
                time.sleep(0.04)

    def video_receive_rstp(self, cam1='rstp:', cam2='rstp:'):
        '''该方法用来接收网络视频
        :param cam1: 左摄像头数据源
        :param cam2: 右摄像头数据源
        :return: None
        '''
        self.video_receive_local(cam1=cam1, cam2=cam2, time_flag=False)

    def video_play(self):
        '''该方法用来播放视频
        :return: None
        '''

        def label_show_left(frame, label=self.ui.label):  # 左控件label播放
            height, width, _ = frame.shape
            frame_change = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resize = cv2.resize(frame_change, (360, 240), interpolation=cv2.INTER_AREA)
            image = QtGui.QImage(frame_resize.data, frame_resize.shape[1], frame_resize.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 处理成QImage
            label.setPixmap(QtGui.QPixmap.fromImage(image))

        def label_show_right(frame, label=self.ui.label_2):  # 右空间Lable播放
            label_show_left(frame, label)

        if self.frame_left is not None:
            label_show_left(self.frame_left)
        if self.frame_right is not None:
            label_show_right(self.frame_right)

    def draw(self):
        '''
        展示图标
        :return:
        '''

        def draw_fp():  # 绘制损失饼图
            fp = Figure_Pie()
            da = data_access.EquipmentData()
            result = da.select()
            fp.plot(*(result[-1][1], result[-1][2], result[-1][3], result[-1][4]))  # '*'有一个解包的功能，将（1，1，1，1）解包为 1 1 1 1
            graphicscene_fp = QtGui.QGraphicsScene()
            graphicscene_fp.addWidget(fp.canvas)
            self.ui.graphicsView_Pie.setScene(graphicscene_fp)
            self.ui.graphicsView_Pie.show()

        def draw_oee():  # 绘制oee日推图
            current_time = datetime.datetime.now().strftime('%Y-%m-%d')
            lossTime = data_access.EquipmentTimeData()
            result_loss = lossTime.select_("select * from loss ORDER BY SJ DESC limit 1")
            zongshijian = time.strftime('%H:%M:%S', time.localtime(time.time()))
            huanxing = result_loss[0][1]
            dailiao = result_loss[0][2]
            shebeiguzhang = result_loss[0][3]
            tingzhi = result_loss[0][4]
            # qitashijian=result[0][5]
            # kongyunzhuan=result[0][6]
            fuheshijian = (int(zongshijian.split(':')[0]) - 8) * 3600 + int(zongshijian.split(':')[1]) * 60 + int(
                zongshijian.split(':')[2]) - tingzhi
            shijijiagong_1 = fuheshijian - huanxing - dailiao - shebeiguzhang
            eff = int(shijijiagong_1 / fuheshijian * 100)  # 计算效率
            print(eff)

            hour = time.localtime()[3]  # 实时更新
            da_oee = data_access.OEEData()
            da_oee.update_("update oee_date set O" + str(hour) + "=" + str(eff) + ' where SJC="' + current_time + '"')
            L_eff = []
            oee = Figure_OEE()
            da = data_access.OEEData()
            result = da.select()
            hour = time.localtime()[3]
            if hour < 20:
                for i in range(1, hour - 6):
                    L_eff.append(result[-1][i])
            oee.plot(*tuple(L_eff))  # 参数
            graphicscene_oee = QtGui.QGraphicsScene()
            graphicscene_oee.addWidget(oee.canvas)
            self.ui.graphicsView_OEE.setScene(graphicscene_oee)
            self.ui.graphicsView_OEE.show()

        def draw_loss():  # 绘制损失直方图
            loss = Figure_Loss()
            da = data_access.EquipmentTimeData()
            result = da.select()
            loss.plot(*(result[-1][1], result[-1][2], result[-1][3], result[-1][4]))
            graphicscene_loss = QtGui.QGraphicsScene()
            graphicscene_loss.addWidget(loss.canvas)
            self.ui.graphicsView_Loss.setScene(graphicscene_loss)
            self.ui.graphicsView_Loss.show()

        def draw_mt():  # 绘制耗材使用图
            mt = Figure_MT()
            mt.plot()
            graphicscene_mt = QtGui.QGraphicsScene()
            graphicscene_mt.addWidget(mt.canvas)
            self.ui.graphicsView_MT.setScene(graphicscene_mt)
            self.ui.graphicsView_MT.show()

        draw_fp()
        draw_loss()
        draw_mt()
        draw_oee()

    def video_recog(self):
        '''
        视频识别部分
        :return:
        '''
        frame_left = self.frame_left  # 原始彩色图，左边摄像头
        frame_left_gray = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)  # 原始图的灰度图

        # frame_right = self.frame_left  # 原始彩色图
        # frame_right_gray = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

        def video_recog_left():
            img = frame_left
            spark = self.vision.find_spark(img)
            self.q.enqueue(spark)
            # print(spark)
            if spark or True in self.q.queue:  # 如果一段间隔时间内不断有火花（和机器移动，稍后完成），则说明机器必定处于工作状态
                #print('work')
                self.action_video = None
                self.one_static_time = 0  # 恢复到运动后，一次静止时间重新清零
            else:
                # ******* 截图
                self.one_static_time += 1  # 一次静止时间
                if self.one_static_time % 60 == 0:
                    print('start or static')
                    print('静止了，往catch文件夹中查看原因')
                    t = time.localtime()
                    hour = t[3]
                    mini = t[4]
                    seco = t[5]
                    filename = str(hour) + '-' + str(mini) + '-' + str(seco)
                    cv2.imwrite('./catch/' + filename + '.jpg', img)
                # ********

                self.action = ThreadedTCPRequestHandler.action # 键盘操作
                if self.action is not None:  # 往面板上写当前由于什么原因导致机器静止
                    if self.pre_action is None:
                        print(self.action)
                        message = '[' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                      time.localtime(time.time())) + ']' + str(self.action)
                        self.displayMessage(message)

                if self.vision.tiaoshi(frame_left_gray):
                    self.action_video = 'tiaoshi'
                if self.action_video is not None:
                    if self.pre_action_video is None:
                        print(self.action_video)
                        message = '[' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                      time.localtime(time.time())) + ']' + str(self.action_video)
                        self.displayMessage(message)



        def video_recog_right():  # 以后用来做换气瓶等的实现
            pass

        video_recog_left()
        video_recog_right()
        self.pre_action = self.action
        self.pre_action_video = self.action_video

    def data_read(self):
        pass

    def displayMessage(self, message):
        self.ui.textBrowser.append(message)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioAll()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
