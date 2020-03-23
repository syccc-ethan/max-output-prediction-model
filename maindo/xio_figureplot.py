from PyQt4 import QtGui, QtCore
import uifiles.xio_figureplot_ui as ui
import sys
from utils.utils import Timer
from figure.figure_plot import Figure_Pie, Figure_MT, Figure_Loss, Figure_OEE, Figure_Origin
from data import data_access

class XioFigurePlot(QtGui.QWidget):
    '''这个类为绘制类
    '''

    def __init__(self):
        super(XioFigurePlot, self).__init__()
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)

        self.thread_figure = Timer('updatePlay()', sleep_time=2)
        self.connect(self.thread_figure, QtCore.SIGNAL('updatePlay()'), self.draw)
        self.thread_figure.start()

    def draw(self):
        def draw_fp():  # 绘制损失饼图
            fp = Figure_Pie()
            da=data_access.EquipmentData()
            result=da.select()
            fp.plot(*(result[-1][1], result[-1][2], result[-1][3], result[-1][4]))  # '*'有一个解包的功能，将（1，1，1，1）解包为 1 1 1 1
            graphicscene_fp = QtGui.QGraphicsScene()
            graphicscene_fp.addWidget(fp.canvas)
            self.ui.graphicsView_Pie.setScene(graphicscene_fp)
            self.ui.graphicsView_Pie.show()

        def draw_oee():  # 绘制oee日推图
            L_eff=[]
            oee = Figure_OEE()
            da=data_access.OEEData()
            result=da.select()
            for i in range(1,len(result[-1])):
                if result[-1][i]!=None:
                     L_eff.append(result[-1][i])
            oee.plot(*tuple(L_eff))  # 参数
            graphicscene_oee = QtGui.QGraphicsScene()
            graphicscene_oee.addWidget(oee.canvas)
            self.ui.graphicsView_OEE.setScene(graphicscene_oee)
            self.ui.graphicsView_OEE.show()

        def draw_loss():  # 绘制损失直方图
            loss = Figure_Loss()
            da=data_access.EquipmentTimeData()
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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_app = XioFigurePlot()
    app.setQuitOnLastWindowClosed(True)
    main_app.show()
    sys.exit(app.exec_())
