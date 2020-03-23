from PyQt4 import QtGui, QtCore
from PyQt4.QtNetwork import *
import uifiles.xio_playvideo_ui as ui
import sys
import cv2
import threading
import time
from utils.utils import Timer



class XioPlayVideo(QtGui.QWidget):
    '''这个类为主程序类
    '''

    def __init__(self):
        super(XioPlayVideo, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.left_cam = cv2.VideoCapture('./videos/left_cam.mp4')  # 左摄像头
        self.right_cam = cv2.VideoCapture('./videos/right_cam.mp4')
        self.frame_left = None
        self.frame_right = None

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
        self.thread_tcp = None  # 该线程用来完成tcp，未写完


    def video_receive_local(self, cam1='./videos/left_cam.mp4', cam2='./videos/right_cam.mp4', time_flag=True):
        '''该方法用来接收本地视频
        :param cam1: 左摄像头数据源
        :param cam2: 右摄像头数据源
        :param time_flag: 是否休眠，本地视频为True
        :return: None
        '''
        if self.left_cam.isOpened() is False:
            self.left_cam = cv2.VideoCapture(cam1)
        if self.right_cam.isOpened() is False:
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
            frame_resize = cv2.resize(frame_change, (500, 300), interpolation=cv2.INTER_AREA)
            image = QtGui.QImage(frame_resize.data, frame_resize.shape[1], frame_resize.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 处理成QImage
            label.setPixmap(QtGui.QPixmap.fromImage(image))

        def label_show_right(frame, label=self.ui.label_2):  # 右空间Lable播放
            label_show_left(frame, label)

        if self.frame_left is not None:
            label_show_left(self.frame_left)
        if self.frame_right is not None:
            label_show_right(self.frame_right)

    def video_recog(self):
        pass

    def data_read(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioPlayVideo()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
