from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random as r

class Ui_MainWindow(QtWidgets.QWidget, object):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(816, 749)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 510, 721, 221))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "DO NOT PUSH THIS F*CKING BUTTON"))
        self.pushButton.clicked.connect(self.do_some_fcking_magik)

    def do_some_fcking_magik(self):
        self.update()

    def paintEvent(self, ev):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(QtGui.QColor(255, 255, 0))
        qp.setPen(QtGui.QColor(0, 0, 0))
        radius = r.randrange(0, 75)
        qp.drawEllipse(150 - radius, 150 - radius, 150 + radius, 150 + radius)
        qp.end()


class Window1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if True:
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon("icon.ico"))
        ex = Window1()
        ex.show()
        sys.exit(app.exec_())
