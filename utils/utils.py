from PyQt4 import QtCore
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np
import datetime


class Timer(QtCore.QThread):
    '''这个类用来向主线程发射信号，通知其每隔一段时间运行一个槽函数
    Qt只允许主线程（也就是main函数在的那个线程）使用界面类，因为界面类不是线程安全的，不可重入，
    在多个线程中使用可能会出现问题，因此Qt不建议主界面线程外的线程使用图形类和调用图形类接口。
    否则有可能报错
    '''

    def __init__(self, signal='updateTime()', sleep_time=0.04):
        super(Timer, self).__init__()
        self.signal = signal
        self.sleep_time = sleep_time

    def run(self):
        while True:
            self.emit(QtCore.SIGNAL(self.signal))
            time.sleep(self.sleep_time)  # 休眠固定时间


class MyQueue():
    def __init__(self, MAX=30):
        self.MAX = MAX
        self.queue = [False for i in range(self.MAX)]

    def is_full(self):
        if len(self.queue) == self.MAX:
            return True
        elif len(self.queue) > self.MAX:
            raise Exception('上溢出')
        return False

    def is_empty(self):
        if len(self.queue) == 0:
            return True

    def enqueue(self, frame):
        if not self.is_full():
            self.queue.append(frame)
        else:
            self.dequeue()
            self.queue.append(frame)
            # print('溢出')

    def dequeue(self):
        if not self.is_empty():
            self.queue.remove(self.queue[0])
        else:
            print('没有了')


def show_image(image):
    '''
    显示图像的像素坐标，便于截取兴趣区域
    :param image:
    :return:
    '''
    i = plt.imread(image)
    plt.imshow(i)
    plt.show()


def roi_cut(filepath='../images/50.jpg', loc=(5, 130, 980, 1090)):
    '''
    截取一个矩形兴趣区域
    :param filepath:
    :param loc:
    :return:
    '''
    image = cv2.imread(filepath, 1)
    l = image[loc[0]:loc[1], loc[2]:loc[3]]
    cv2.imwrite(filepath[0:-4] + '1.jpg', l)


def gamma_trans(img, gamma):
    '''
    将图像光照归一化
    :param img:
    :param gamma:
    :return:
    '''
    # 具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    # 实现映射用的是Opencv的查表函数
    return cv2.LUT(img, gamma_table)


def find_spark(img, spark_roi):  # 火花还不够鲁邦，应该再加入颜色瞬间一高一低
    '''
    在固定区域检测火花
    :param img:
    :param spark_roi: 这个参数为一个不规则mask，二值图
    :return:
    '''
    img_gam = gamma_trans(img, 0.75)  # 光照归一化
    hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

    # 火花颜色
    lower = np.array([0, 0, 250])
    upper = np.array([360, 10, 255])
    mask = cv2.inRange(hsv, lower, upper)
    # res_1 = cv2.bitwise_and(hsv,hsv,mask=mask) # hsv颜色选取火花颜色
    res = cv2.bitwise_and(mask, mask, mask=spark_roi)  # 在该区域检索
    res /= 255
    s = np.sum(res)
    if s > 6000:
        return True
    return False


def find_spark_test():
    cap = cv2.VideoCapture('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/videos/left_cam.mp4')
    while (1):
        # Take each frame
        _, img = cap.read()

        img_gam = gamma_trans(img, 0.75)
        img0 = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/mask_1.jpg', 0)
        ret, thresh1 = cv2.threshold(img0, 127, 255, cv2.THRESH_BINARY)
        hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 250])
        upper = np.array([360, 10, 255])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img_gam, img_gam, mask=mask)
        res_1 = cv2.bitwise_and(res, res, mask=thresh1)
        num_res_1 = res_1 / 255
        print(np.sum(num_res_1))
        cv2.imshow('ga', img_gam)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        cv2.imshow('res1', res_1)
        cv2.waitKey(1)


def find_machine_test():
    # cap = cv2.VideoCapture('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/videos/left_cam.mp4')
    cap = cv2.VideoCapture('./videos/testback.mp4')
    pre = None
    curr = None
    while (1):
        # Take each frame
        _, img = cap.read()

        img_gam = gamma_trans(img, 0.75)
        img0 = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/mask_3.jpg', 0)
        ret, thresh1 = cv2.threshold(img0, 127, 255, cv2.THRESH_BINARY)
        hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 75, 200])
        upper = np.array([20, 150, 255])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(img_gam, img_gam, mask=mask)
        res_1 = cv2.bitwise_and(res, res, mask=thresh1)

        res_2 = cv2.bitwise_and(mask, mask, mask=thresh1)  # 对这个进行帧间差分
        curr = res_2
        if (curr is not None) and (pre is not None):
            all = np.sum(pre) / 255
            diff = cv2.absdiff(curr, pre) / 255
            diff_num = np.sum(diff)
            print(diff_num / all)
        pre = curr
        num_res_1 = res_1 / 255
        # print(np.sum(num_res_1))
        cv2.imshow('ga', img_gam)
        # cv2.imshow('mask', mask)
        # cv2.imshow('res', res)
        # cv2.imshow('res1', res_1)
        cv2.imshow('res2', res_2)
        cv2.waitKey(1)


def test1():
    # show_image('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/447.jpg')
    img = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/jietu.jpg')

    #
    img0 = cv2.imread('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/gam_s.jpg', 0)
    ret, thresh1 = cv2.threshold(img0, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('2', thresh1)
    # cv2.waitKey(0)

    img_gam = gamma_trans(img, 0.75)  # 亮度归一化
    # cv2.imwrite('gam.jpg',img_gam)

    hsv = cv2.cvtColor(img_gam, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 75, 200])
    upper = np.array([20, 150, 255])
    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(img_gam, img_gam, mask=mask)

    print(img_gam[190, 740])
    print(img_gam[200, 700])

    # show_image('/Users/kaimingcheng/PycharmProjects/xiaowork/maindo/images/jietu.jpg')
    # cv2.imshow('img',img)
    cv2.imshow('ga', img_gam)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.waitKey(0)

def diff_time(endtime=datetime.datetime.strptime("08:30:00", "%H:%M:%S"), starttime=datetime.datetime.strptime("07:30:00", "%H:%M:%S")):
    print((endtime - starttime).seconds)
    pass

if __name__ == '__main__':
    # test1()
    #find_machine_test()
    # find_spark_test()
    # show_image('./images/1.jpg')
    # roi_cut('./images/1.jpg', (180,420,600,810))
    # time1 = time.time()
    # mq = MyQueue()
    # mq.enqueue(1)
    # mq.enqueue(5)
    # mq.enqueue(1)
    # #mq.dequeue()
    # print(mq.queue)
    # time2 = time.time()
    # print(time2-time1)
    #find_machine_test()
    print(datetime.datetime.now())
    diff_time(datetime.datetime.now())
