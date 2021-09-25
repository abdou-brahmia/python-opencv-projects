# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyGame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import numpy as np
import time
import random
import threading

class Ui_MainWindow(object):

    image = np.zeros([5, 5, 3], dtype=np.uint8)
    FrameEnd = np.zeros([30, 30, 3], dtype=np.uint8)
    
    th = None
    Score=0
    ColorBlack=(000,000,000)
    ColorWhite=(255,255,255)
    ColorRed=(255,000,000)
    ColorGreen=(000,255,000)
    ColorBlue=(000,000,255)
    
    ColorOne=ColorRed
    ColorTwo=ColorBlue

    state=1
    stateThread=0

    celulle = [0,0,0,0,0,0,0,0,0]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 390, 390))
        self.label.setText("")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, 50, 20, 330))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 210, 180, 200))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.Button_1 = QtWidgets.QPushButton(self.groupBox)
        self.Button_1.setGeometry(QtCore.QRect(10, 80, 40, 27))
        self.Button_1.setObjectName("Button_1")
        self.Button_1.clicked.connect(self.Meth1)
        
        self.Button_2 = QtWidgets.QPushButton(self.groupBox)
        self.Button_2.setGeometry(QtCore.QRect(60, 80, 41, 27))
        self.Button_2.setObjectName("Button_2")
        self.Button_2.clicked.connect(self.Meth2)
        
        self.Button_3 = QtWidgets.QPushButton(self.groupBox)
        self.Button_3.setGeometry(QtCore.QRect(110, 80, 41, 27))
        self.Button_3.setObjectName("Button_3")
        self.Button_3.clicked.connect(self.Meth3)
        
        self.Button_4 = QtWidgets.QPushButton(self.groupBox)
        self.Button_4.setGeometry(QtCore.QRect(10, 40, 41, 31))
        self.Button_4.setObjectName("Button_4")
        self.Button_4.clicked.connect(self.Meth4)
        
        self.Button_5 = QtWidgets.QPushButton(self.groupBox)
        self.Button_5.setGeometry(QtCore.QRect(60, 40, 41, 31))
        self.Button_5.setObjectName("Button_5")
        self.Button_5.clicked.connect(self.Meth5)
        
        self.Button_6 = QtWidgets.QPushButton(self.groupBox)
        self.Button_6.setGeometry(QtCore.QRect(110, 40, 41, 31))
        self.Button_6.setObjectName("Button_6")
        self.Button_6.clicked.connect(self.Meth6)
        
        self.Button_7 = QtWidgets.QPushButton(self.groupBox)
        self.Button_7.setGeometry(QtCore.QRect(10, 0, 41, 31))
        self.Button_7.setObjectName("Button_7")
        self.Button_7.clicked.connect(self.Meth7)
        
        self.Button_8 = QtWidgets.QPushButton(self.groupBox)
        self.Button_8.setGeometry(QtCore.QRect(60, 0, 41, 31))
        self.Button_8.setObjectName("Button_8")
        self.Button_8.clicked.connect(self.Meth8)
        
        self.Button_9 = QtWidgets.QPushButton(self.groupBox)
        self.Button_9.setGeometry(QtCore.QRect(110, 0, 41, 31))
        self.Button_9.setObjectName("Button_9")
        self.Button_9.clicked.connect(self.Meth9)
        
        self.groupBox.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 125, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lobster Two")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 410, 191, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 400, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 10, 180, 170))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.NewGame = QtWidgets.QPushButton(self.groupBox_2)
        self.NewGame.setGeometry(QtCore.QRect(10, 20, 150, 30))
        self.NewGame.setMouseTracking(False)
        self.NewGame.setObjectName("NewGame")
        self.NewGame.clicked.connect(self.MethodeNewGame)
        self.NewGame.setEnabled(True)

        self.StartGame = QtWidgets.QPushButton(self.groupBox_2)
        self.StartGame.setGeometry(QtCore.QRect(10, 125, 150, 30))
        self.StartGame.setObjectName("StartGame")
        self.StartGame.clicked.connect(self.MethodeStartGame)
        self.StartGame.setEnabled(False)

        self.StopGame = QtWidgets.QPushButton(self.groupBox_2)
        self.StopGame.setGeometry(QtCore.QRect(10, 90, 150, 30))
        self.StopGame.setObjectName("StopGame")
        self.StopGame.clicked.connect(self.MethodeStopGame)
        self.StopGame.setEnabled(False)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 190, 170, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)

        QShortcut(QtCore.Qt.Key_1, MainWindow, self.Meth1)
        QShortcut(QtCore.Qt.Key_2, MainWindow, self.Meth2)
        QShortcut(QtCore.Qt.Key_3, MainWindow, self.Meth3)
        QShortcut(QtCore.Qt.Key_4, MainWindow, self.Meth4)
        QShortcut(QtCore.Qt.Key_5, MainWindow, self.Meth5)
        QShortcut(QtCore.Qt.Key_6, MainWindow, self.Meth6)
        QShortcut(QtCore.Qt.Key_7, MainWindow, self.Meth7)
        QShortcut(QtCore.Qt.Key_8, MainWindow, self.Meth8)
        QShortcut(QtCore.Qt.Key_9, MainWindow, self.Meth9)
        
        self.affiche()
        self.creeFrameEnd()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Piano Game"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "Piano"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.StartGame.setText(_translate("MainWindow", "StartGame"))
        self.NewGame.setText(_translate("MainWindow", "NewGame"))
        self.StopGame.setText(_translate("MainWindow", "StopGame"))
        self.label_3.setText(_translate("MainWindow", "Copyrite : abdou brahmia _2020"))
        self.label_4.setText(_translate("MainWindow", "Score  : 0"))










    def Meth1(self):
        if ((self.celulle[0]==1)and( self.state)):
            self.celulle[0]=0
            self.image[4,0]=self.ColorBlack
            self.affiche()
    def Meth2(self):
        if ((self.celulle[1]==1)and( self.state)):
            self.celulle[1]=0
            self.image[4,2]=self.ColorBlack
            self.affiche()
    def Meth3(self):
        if ((self.celulle[2]==1) and( self.state)):
            self.celulle[2]=0
            self.image[4,4]=self.ColorBlack
            self.affiche()
    def Meth4(self):
        if ((self.celulle[3]==1)and( self.state)):
            self.celulle[3]=0
            self.image[2,0]=self.ColorBlack
            self.affiche()
    def Meth5(self):
        if ((self.celulle[4]==1)and( self.state)):
            self.celulle[4]=0
            self.image[2,2]=self.ColorBlack
            self.affiche()
    def Meth6(self):
        if ((self.celulle[5]==1)and( self.state)):
            self.celulle[5]=0
            self.image[2,4]=self.ColorBlack
            self.affiche()
    def Meth7(self):
        if ((self.celulle[6]==1)and( self.state)):
            self.celulle[6]=0
            self.image[0,0]=self.ColorBlack
            self.affiche()
    def Meth8(self):
        if ((self.celulle[7]==1)and( self.state)):
            self.celulle[7]=0
            self.image[0,2]=self.ColorBlack
            self.affiche()
    def Meth9(self):
        if ((self.celulle[8]==1)and( self.state)):
            self.celulle[8]=0
            self.image[0,4]=self.ColorBlack
            self.affiche()
    

    def play(self):
        while (True):
            if (self.state==1):
                self.step()
                time.sleep(1)
                if (self.state==0):
                    while not( self.state):
                        time.sleep(1)
                    time.sleep(1)
                self.endStep()
                    
            time.sleep(0.5)


    def step(self):
        val=random.randrange(1,10,1)
        self.celulle[val-1]=1
        y=int((val-1)/3)
        x=(val -(y*3))-1
        y=2-y
        print(val)
        print(x)
        print(y)
        self.image[y*2,x*2]=self.ColorBlue
        self.affiche()
        

        print(self.celulle)

    def endStep(self):
        value=0
        for i in self.celulle:
            if (i ==1):
                value=1
                break
        if (value ==1):
            self.state=0
            self.endGame()
        else:
            self.Score+=1
            self.label_4.setText('Score : '+str(self.Score))


    def affiche(self):
        height, width, channels = self.image.shape
        bytesPerLine = channels * width
        qImg = QtGui.QImage(self.image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        pixmap_image = QtGui.QPixmap(pixmap01)
        self.label.setPixmap(pixmap_image)
        self.label.setScaledContents(True)
     
    def MethodeNewGame(self):
        if not(self.stateThread):
            self.th =threading.Thread(target=self.play)
            self.th.start()
            self.stateThread=1
        self.image = np.zeros([5, 5, 3], dtype=np.uint8)

        self.label_4.setText("Score : "+str(self.Score))
        self.Score=0

        self.state=1
        self.StartGame.setEnabled(False)
        self.StopGame.setEnabled(True)
        self.NewGame.setEnabled(True)
        self.groupBox.setEnabled(True)


    def MethodeStartGame(self):
        self.state=1
        self.StartGame.setEnabled(False)
        self.StopGame.setEnabled(True)
        self.NewGame.setEnabled(True)
        self.groupBox.setEnabled(True)

    def MethodeStopGame(self):
        self.state=0
        self.StartGame.setEnabled(True)
        self.StopGame.setEnabled(False)
        self.NewGame.setEnabled(True)
        self.groupBox.setEnabled(False)



    def creeFrameEnd(self):
       
        ### E 
        self.FrameEnd[6,3]=self.ColorRed
        self.FrameEnd[7,3]=self.ColorRed
        self.FrameEnd[8,3]=self.ColorRed
        self.FrameEnd[9,3]=self.ColorRed
        self.FrameEnd[10,3]=self.ColorRed
        self.FrameEnd[11,3]=self.ColorRed
        self.FrameEnd[12,3]=self.ColorRed
        self.FrameEnd[13,3]=self.ColorRed
        self.FrameEnd[6,4]=self.ColorRed
        self.FrameEnd[7,4]=self.ColorRed
        self.FrameEnd[8,4]=self.ColorRed
        self.FrameEnd[9,4]=self.ColorRed
        self.FrameEnd[10,4]=self.ColorRed
        self.FrameEnd[11,4]=self.ColorRed
        self.FrameEnd[12,4]=self.ColorRed
        self.FrameEnd[13,4]=self.ColorRed
        self.FrameEnd[6,5]=self.ColorRed
        self.FrameEnd[6,6]=self.ColorRed
        self.FrameEnd[6,7]=self.ColorRed
        self.FrameEnd[7,5]=self.ColorRed
        self.FrameEnd[7,6]=self.ColorRed
        self.FrameEnd[7,7]=self.ColorRed
        self.FrameEnd[9,5]=self.ColorRed
        self.FrameEnd[9,6]=self.ColorRed
        self.FrameEnd[9,7]=self.ColorRed
        self.FrameEnd[10,5]=self.ColorRed
        self.FrameEnd[10,6]=self.ColorRed
        self.FrameEnd[10,7]=self.ColorRed
        self.FrameEnd[12,5]=self.ColorRed
        self.FrameEnd[12,6]=self.ColorRed
        self.FrameEnd[12,7]=self.ColorRed
        self.FrameEnd[13,5]=self.ColorRed
        self.FrameEnd[13,6]=self.ColorRed
        self.FrameEnd[13,7]=self.ColorRed


        ### N

        self.FrameEnd[6,10]=self.ColorGreen
        self.FrameEnd[7,10]=self.ColorGreen
        self.FrameEnd[8,10]=self.ColorGreen
        self.FrameEnd[9,10]=self.ColorGreen
        self.FrameEnd[10,10]=self.ColorGreen
        self.FrameEnd[11,10]=self.ColorGreen
        self.FrameEnd[12,10]=self.ColorGreen
        self.FrameEnd[13,10]=self.ColorGreen
        self.FrameEnd[6,11]=self.ColorGreen
        self.FrameEnd[7,11]=self.ColorGreen
        self.FrameEnd[8,11]=self.ColorGreen
        self.FrameEnd[9,11]=self.ColorGreen
        self.FrameEnd[10,11]=self.ColorGreen
        self.FrameEnd[11,11]=self.ColorGreen
        self.FrameEnd[12,11]=self.ColorGreen
        self.FrameEnd[13,11]=self.ColorGreen
        self.FrameEnd[6,16]=self.ColorGreen
        self.FrameEnd[7,16]=self.ColorGreen
        self.FrameEnd[8,16]=self.ColorGreen
        self.FrameEnd[9,16]=self.ColorGreen
        self.FrameEnd[10,16]=self.ColorGreen
        self.FrameEnd[11,16]=self.ColorGreen
        self.FrameEnd[12,16]=self.ColorGreen
        self.FrameEnd[13,16]=self.ColorGreen
        self.FrameEnd[6,17]=self.ColorGreen
        self.FrameEnd[7,17]=self.ColorGreen
        self.FrameEnd[8,17]=self.ColorGreen
        self.FrameEnd[9,17]=self.ColorGreen
        self.FrameEnd[10,17]=self.ColorGreen
        self.FrameEnd[11,17]=self.ColorGreen
        self.FrameEnd[12,17]=self.ColorGreen
        self.FrameEnd[13,17]=self.ColorGreen
        self.FrameEnd[7,12]=self.ColorGreen
        self.FrameEnd[8,12]=self.ColorGreen
        self.FrameEnd[9,12]=self.ColorGreen
        self.FrameEnd[8,13]=self.ColorGreen
        self.FrameEnd[9,13]=self.ColorGreen
        self.FrameEnd[10,13]=self.ColorGreen
        self.FrameEnd[9,14]=self.ColorGreen
        self.FrameEnd[10,14]=self.ColorGreen
        self.FrameEnd[11,14]=self.ColorGreen
        self.FrameEnd[10,15]=self.ColorGreen
        self.FrameEnd[11,15]=self.ColorGreen
        self.FrameEnd[12,15]=self.ColorGreen
        
        ### D

        self.FrameEnd[6,20]=self.ColorBlue
        self.FrameEnd[7,20]=self.ColorBlue
        self.FrameEnd[8,20]=self.ColorBlue
        self.FrameEnd[9,20]=self.ColorBlue
        self.FrameEnd[10,20]=self.ColorBlue
        self.FrameEnd[11,20]=self.ColorBlue
        self.FrameEnd[12,20]=self.ColorBlue
        self.FrameEnd[13,20]=self.ColorBlue
        self.FrameEnd[6,21]=self.ColorBlue
        self.FrameEnd[7,21]=self.ColorBlue
        self.FrameEnd[8,21]=self.ColorBlue
        self.FrameEnd[9,21]=self.ColorBlue
        self.FrameEnd[10,21]=self.ColorBlue
        self.FrameEnd[11,21]=self.ColorBlue
        self.FrameEnd[12,21]=self.ColorBlue
        self.FrameEnd[13,21]=self.ColorBlue
        self.FrameEnd[6,23]=self.ColorBlue
        self.FrameEnd[7,23]=self.ColorBlue
        self.FrameEnd[12,23]=self.ColorBlue
        self.FrameEnd[13,23]=self.ColorBlue
        self.FrameEnd[7,24]=self.ColorBlue
        self.FrameEnd[8,24]=self.ColorBlue
        self.FrameEnd[9,24]=self.ColorBlue
        self.FrameEnd[10,24]=self.ColorBlue
        self.FrameEnd[11,24]=self.ColorBlue
        self.FrameEnd[12,24]=self.ColorBlue
        self.FrameEnd[8,25]=self.ColorBlue
        self.FrameEnd[9,25]=self.ColorBlue
        self.FrameEnd[10,25]=self.ColorBlue
        self.FrameEnd[11,25]=self.ColorBlue
        self.FrameEnd[6,22]=self.ColorBlue
        self.FrameEnd[13,22]=self.ColorBlue



    def endGame(self):
        self.image = self.FrameEnd
        self.affiche()
        self.StartGame.setEnabled(False)
        self.StopGame.setEnabled(False)
        self.groupBox.setEnabled(False)
        self.celulle=[0,0,0,0,0,0,0,0,0]



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

