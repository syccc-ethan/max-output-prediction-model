import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


class Figure_Origin():
    '''这个类是绘图父类
    '''

    def __init__(self):
        self.figure = plt.figure(figsize=(6.5, 4), facecolor='lightgoldenrodyellow')  # 等下继承一个父类
        self.canvas = FigureCanvas(self.figure)

    def plot(self, *args, **kwargs):
        pass


class Figure_MT(Figure_Origin):
    '''这个类是绘制耗材图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_MT, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_mt():
            ax = self.figure.add_subplot(111)
            ax.yaxis.grid(True) # y 方向网格
            n_groups = 3

            means_plan = (4, 3, 3)

            means_fact = (3, 5, 3)

            index = np.arange(n_groups) + 0.5
            bar_width = 0.2

            opacity = 0.4 # 直方图透明度

            rects1 = ax.bar(index, means_plan, bar_width,
                            alpha=opacity, color='red',

                            label='实际投入')

            rects2 = ax.bar(index + bar_width + 0.1, means_fact, bar_width,
                            alpha=opacity, color='yellow',
                            label='计划投入')
            ax.set_title('耗材分时监控图',fontsize=20)
            ax.set_xticks(index + bar_width + 0.2 / 2)
            ax.set_xticklabels(('焊丝', '氩气', '焊嘴'))
            ax.set_ylim(0, 10)
            ax.set_xlim(0, 4)
            ax.legend(loc=2)

            self.figure.tight_layout()
            # plt.show()
            self.canvas.draw()
            plt.close() # 关闭，否则会出现warning

        plot_mt()


class Figure_OEE(Figure_Origin):
    '''这个类是绘制OEE日推图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_OEE, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_oee():
            import matplotlib as mpl
            import matplotlib.ticker as mtick
            mpl.rc('ytick', labelsize=10)
            fmt = '%.f%%'
            yticks = mtick.FormatStrFormatter(fmt)
            axes = self.figure.add_subplot(111)
            rect = axes.patch
            rect.set_facecolor('lightblue')

            # 画点
            Y=list(args)
            #print(Y)
            X=[x for x in range(1,len(Y)+1)]
            #print(X)
            type1 = axes.plot(X, Y, label="OEE变化对比", c='g', lw=2, marker='s', mec='r', mfc='r', ms='5')

            # 加标题
            axes.set_title("OEE效能日推图", fontsize=20)

            axes.set_xticks((range(0, 14)))
            axes.tick_params(axis='both', labelsize=10)
            # axes.set_xlabel(str(month) + "月", fontsize=15)  # 20
            axes.set_ylabel("OEE", fontsize=15)
            # 加坐标轴范围
            axes.set_xlim(0.0, 12.0)
            axes.set_xticklabels(("", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                                  "16:00", "17:00", "18:00"), fontsize=8)
            axes.set_ylim(0, 100)
            axes.yaxis.set_major_formatter(yticks)
            axes.legend(loc=1)  # 设置legend位置
            for a, b in zip(X, Y):
                axes.text(a + 0.1, b + 0.01, '%1.f%%' % b, ha='center', va='bottom', color='purple', fontsize=10)  # 25
            axes.yaxis.grid(True)
            self.canvas.draw()
            plt.close()
        plot_oee()


class Figure_Loss(Figure_Origin):
    '''这个类是绘制损失统计图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_Loss, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_loss():

            ax = self.figure.add_subplot(111)
            rect = ax.patch
            rect.set_facecolor('lightblue')

            x_label = ('换气瓶', '换焊丝', '调试', '其他')
            x_pos = np.arange(len(x_label))
            performance = list(args)
            ax.bar(x_pos, performance, width=0.30, align='center', alpha=0.4, color=['red', 'green', 'blue', 'gray'])
            X = np.arange(len(x_label))
            Y = performance
            for a, b in zip(X, Y):
                ax.text(a, b + 0.05, '%.0f' % b, ha='right', color='purple', va='bottom', fontsize=15)

            ax.set_xticks(x_pos)
            ax.set_yticks([0, 400, 800, 1200, 1600])
            ax.set_ylabel('时间：分钟', fontsize=10)
            ax.set_title("设备工作损失时间统计", fontsize=20)  # 30
            ax.set_xticklabels((u'换气瓶', u'换焊丝', u'调试', u'其他'), fontsize=15)
            ax.yaxis.grid(True)
            self.canvas.draw()
            plt.close()

        return plot_loss()



class Figure_Pie(Figure_Origin):
    '''这个类是绘制饼图
    '''

    def __init__(self, parent=None, width=3.5, height=2.8, dpi=100):
        super(Figure_Pie, self).__init__()

    def plot(self, *args, **kwargs):
        def plot_pie():
            ax = self.figure.add_subplot(111)
            ax.set_title("设备工作损失时间占比",fontsize=20)
            labels = '换气瓶', '换焊丝', '调试', '其他'
            sizes = args
            explode = (0, 0.1, 0, 0)  # 第一个异常在饼图冲凸显，凸显度为0.1
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True,
                   startangle=90)
            ax.axis('equal')
            self.canvas.draw()
            plt.close()

        plot_pie()


if __name__ == "__main__":
    p = Figure_Pie()
    p.plot(1, 1, 1, 1)
