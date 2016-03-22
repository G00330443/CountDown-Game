# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import inputLetter
import findWordFromDic
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from workthread import WorkThread
from Answers_page import Ui_Form

global sec
sec=0

class Ui_MainWindow(object):
    vowelButton_Times=0
    generatedWord=[]
    timer=QTimer()
    workThread=WorkThread()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(134, 20, 361, 51))
        self.label.setMinimumSize(QtCore.QSize(361, 0))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 75 italic 20pt \"Monotype Corsiva\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 551, 141))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 551, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout.addWidget(self.textBrowser_4)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.horizontalLayout.addWidget(self.textBrowser_8)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout.addWidget(self.textBrowser_9)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout.addWidget(self.textBrowser_6)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout.addWidget(self.textBrowser_7)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout.addWidget(self.textBrowser_5)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout.addWidget(self.textBrowser_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.textBrowser_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 9, 491, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 581, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.input)
     #---------------------------------------------------

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 161, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.input1)
     #----------------------------------------------------------
# CountDown function
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(400, 160, 100, 51))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        self.lcdNumber.setObjectName("lcdNumber")
        self.timer.timeout.connect(self.countTime)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 551, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 551, 89))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
 #----------------------------------------------------------
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(4, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

##pushbutton_4 is a button to control countdown function
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 160, 51, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.work)

##Submit button in the bottle of frame
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 160, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
       # self.pushButton_3.clicked.connect(self.Answer_Game)

        self.pushButton_3.clicked.connect(self.Answer_Game)
    #----------------------------------------------------------
    ## label_12
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(4, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
         #----------------------------------------------------------

        self.frame.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Countdown Word Game"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_11.setText(_translate("MainWindow", "Please press Button to input letter :"))
        self.pushButton.setText(_translate("MainWindow", "Vowels"))
        self.pushButton_2.setText(_translate("MainWindow", "Consonants"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.pushButton_4.setText(_translate("MainWindow", "start"))
        self.label_12.setText(_translate("MainWindow", "Please enter answer :"))

##Function to Generate Vowels
    def input(self):
        if self.vowelButton_Times==0 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_4.setText(number)
        elif self.vowelButton_Times==1 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_8.setText(number)
        elif self.vowelButton_Times==2 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_9.setText(number)
        elif self.vowelButton_Times==3 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_6.setText(number)
        elif self.vowelButton_Times==4 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_7.setText(number)
        elif self.vowelButton_Times==5 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_5.setText(number)
        elif self.vowelButton_Times==6 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_3.setText(number)
        elif self.vowelButton_Times==7 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser_2.setText(number)
        elif self.vowelButton_Times==8 :
            number=inputLetter.vowel()
            self.generatedWord.append(number)
            self.textBrowser.setText(number)
        else :
            self.pushButton.clicked.connect(self.msg)
        self.vowelButton_Times=self.vowelButton_Times+1


## Function to Generate  Consonants
    def input1(self):
       # print(self.vowelButton_Times)
       # print("-----------")
        if self.vowelButton_Times==0 :
            number=inputLetter.con()
            print(number)
            self.generatedWord.append(number)
            self.textBrowser_4.setText(number)
        elif self.vowelButton_Times==1 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_8.setText(number)
        elif self.vowelButton_Times==2 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_9.setText(number)
        elif self.vowelButton_Times==3 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_6.setText(number)
        elif self.vowelButton_Times==4 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_7.setText(number)
        elif self.vowelButton_Times==5 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_5.setText(number)
        elif self.vowelButton_Times==6 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_3.setText(number)
        elif self.vowelButton_Times==7 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser_2.setText(number)
        elif self.vowelButton_Times==8 :
            number=inputLetter.con()
            self.generatedWord.append(number)
            self.textBrowser.setText(number)
        else :
            self.pushButton_2.clicked.connect(self.msg)
        self.vowelButton_Times=self.vowelButton_Times+1

    def msg(self):
        reply = QMessageBox.information(QtWidgets.QWidget(),"Warning","out of range", QMessageBox.Yes | QMessageBox.No)

##Generate Answer in a other window
    def Answer_Game(self):
        findWordFromDic.set_input_word(self.generatedWord)
        print(self.generatedWord)

       # reply = QInputDialog.getMultiLineText(QtWidgets.QWidget(),)
       # reply = QMessageBox.information(QtWidgets.QWidget(),"Warning",'s', QMessageBox.Yes | QMessageBox.No)

  ## Function of Countdown
    def countTime(self):
        global  sec
        sec+=1
        self.lcdNumber.display(sec)          #LED显示数字+1

    def work(self):
        self.timer.start(1000)               #计时器每秒计数
        self.workThread.start()              #计时开始
        self.workThread.trigger.connect(self.timeStop)   #当获得循环完毕的信号时，停止计数

    def timeStop(self):
        self.timer.stop()
        print("END",self.lcdNumber.value())
        global sec
        sec=0



