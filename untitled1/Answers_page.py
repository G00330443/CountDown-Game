# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Answers_page.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(15, 61, 361, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(44, 19, 291, 31))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "          Answers of Countdown Word "))

    def showpa(self):
        import sys
        app=QtWidgets.QApplication(sys.argv)
        secondWindow=QtWidgets.QWidget()
        show_answer=Ui_Form()
        show_answer.setupUi(secondWindow)
        secondWindow.show()
        sys.exit(app.exec_())