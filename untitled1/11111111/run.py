from PyQt5 import QtWidgets
import qqqq

class mywindow(QtWidgets.QWidget,qqqq.Ui_Dialog):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())