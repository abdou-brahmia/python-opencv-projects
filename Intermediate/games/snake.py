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
    image = np.zeros([30, 30, 3], dtype=np.uint8)
    FrameEnd = np.zeros([30, 30, 3], dtype=np.uint8)
    
    th = None

    ColorBlack=(000,000,000)
    ColorWhite=(255,255,255)
    ColorRed=(255,000,000)
    ColorGreen=(000,255,000)
    ColorBlue=(000,000,255)
    
    ColorSnake=ColorRed
    ColorEat=ColorBlue
    speed=0.5
    Score=0
    snake=[]
    state=1
    stateThread=0

    orientation="D"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 390, 390))
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, 0, 20, 430))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 210, 160, 210))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
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
        self.label_3.setGeometry(QtCore.QRect(10, 400, 200, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4") 


        self.Left = QtWidgets.QPushButton(self.groupBox)
        self.Left.setGeometry(QtCore.QRect(15, 75, 40, 30))
        self.Left.setObjectName("Left")
        self.Left.clicked.connect(self.MethodeLeft)

        self.Right = QtWidgets.QPushButton(self.groupBox)
        self.Right.setGeometry(QtCore.QRect(105, 75, 40, 30))
        self.Right.setObjectName("Right")
        self.Right.clicked.connect(self.MethodeRight)

        self.Up = QtWidgets.QPushButton(self.groupBox)
        self.Up.setGeometry(QtCore.QRect(60, 40, 40, 30))
        self.Up.setObjectName("Up")
        self.Up.clicked.connect(self.MethodeUp)

        self.Down = QtWidgets.QPushButton(self.groupBox)
        self.Down.setGeometry(QtCore.QRect(60, 75, 40, 30))
        self.Down.setObjectName("Down")
        self.Down.clicked.connect(self.MethodeDown)


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(460, 30, 160, 170))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        
        
        self.NewGame = QtWidgets.QPushButton(self.groupBox_2)
        self.NewGame.setGeometry(QtCore.QRect(10, 30, 140, 30))
        self.NewGame.setObjectName("NewGame")
        self.NewGame.clicked.connect(self.MethodeNewGame)
        self.NewGame.setEnabled(True)
        

        self.StopGame = QtWidgets.QPushButton(self.groupBox_2)
        self.StopGame.setGeometry(QtCore.QRect(10, 90, 140, 30))
        self.StopGame.setObjectName("StopGame")
        self.StopGame.clicked.connect(self.MethodeStopGame)
        self.StopGame.setEnabled(False)
        
        
        self.StartGame = QtWidgets.QPushButton(self.groupBox_2)
        self.StartGame.setGeometry(QtCore.QRect(10, 125, 140, 30))
        self.StartGame.setObjectName("StartGame")
        self.StartGame.clicked.connect(self.MethodeStartGame)
        self.StartGame.setEnabled(False)
        

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(430, 205, 240, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        MainWindow.setCentralWidget(self.centralwidget)

        QShortcut(QtCore.Qt.Key_Up, MainWindow, self.MethodeUp)
        QShortcut(QtCore.Qt.Key_Down, MainWindow, self.MethodeDown)
        QShortcut(QtCore.Qt.Key_Left, MainWindow, self.MethodeLeft)
        QShortcut(QtCore.Qt.Key_Right, MainWindow, self.MethodeRight)

        self.creeFrameEnd()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Snake Game"))
        self.label_2.setText(_translate("MainWindow", "Snake"))
        self.Left.setText(_translate("MainWindow", "Left"))
        self.Right.setText(_translate("MainWindow", "Right"))
        self.Down.setText(_translate("MainWindow", "Down"))
        self.Up.setText(_translate("MainWindow", "Up"))
        self.StopGame.setText(_translate("MainWindow", "StopGame"))
        self.StartGame.setText(_translate("MainWindow", "StartGame"))
        self.NewGame.setText(_translate("MainWindow", "NewGame"))
        self.label_3.setText(_translate("MainWindow", "Copyrite : abdou brahmia _2021"))
        self.label_4.setText(_translate("MainWindow", "Score : 0"))

        self.affiche()
        #self.creatEat()
        #self.SnakeEat()
        #self.MethodeDown()
        #self.step()
        #time.sleep(1)
        #self.step()





    def MethodeUp(self):
        #print ("up")
        self.orientation="U"
    def MethodeDown(self):
        #print ("Down")
        self.orientation="D"
    def MethodeLeft(self):
        #print ("Left")
        self.orientation="L"
    def MethodeRight(self):
        #print ("Right")
        self.orientation="R"


    def creatEat (self):
        pointX=random.randrange(30)
        pointY=random.randrange(30)
        #print(self.snake[0])
        if ((pointX,pointY) in self.snake):
            #print ("in the snake")
            while ((pointX,pointY) in self.snake):
                pointX=random.randrange(30)
                pointY=random.randrange(30)
                        
        #else :
        #    print ("not in the snake")
        self.Eat=(pointX,pointY)
        self.image[pointX,pointY]=self.ColorEat
        self.affiche()

    def SnakeEat(self):
        self.snake.append(self.Eat)
        self.image[self.Eat]=self.ColorSnake
        #print(self.Eat)
        self.affiche()
        self.creatEat()
        
        if ( ((self.Score%2)==0)and self.Score<=14 ) :
            self.speed-=0.05



    def step(self):
        a=len(self.snake)-1
        #print(self.snake)
        time.sleep(0.05)
        x=self.snake[a][0]
        y=self.snake[a][1]

        #x=head[0]
        #y=head[1]
        if (self.orientation=="L"):
            y-=1
        elif(self.orientation=="R"):
            y+=1
        elif(self.orientation=="U"):
            x-=1
        elif(self.orientation=="D"):
            x+=1
        
        if (x==-1 or x==30):
            #print ("end game")
            self.state=0
            self.endGame()
        elif (y==-1 or y==30):
            #print ("end game")
            self.state=0
            self.endGame()
        elif ((x,y) in self.snake):
            #print ("end game")
            self.state=0
            self.endGame()
        elif ((x,y)==self.Eat):
            self.Score+=1
            self.SnakeEat()
            self.label_4.setText("Score : "+str(self.Score))
        else :
            self.SnakeMarche(x,y)

    def SnakeMarche(self,x,y):
        self.snake.append((x,y))
        self.image[x,y]=self.ColorSnake
        xx,yy=self.snake[0]
        self.snake.remove(self.snake[0])
        self.image[xx,yy]=self.ColorBlack
        
        self.affiche()

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
        self.image = np.zeros([30, 30, 3], dtype=np.uint8)
        self.snake=[]
        a=random.randrange(30)
        b=random.randrange(30)
        self.snake.append((a,b))
        self.image[a,b]=self.ColorSnake
        self.creatEat()

        self.speed=0.8
        self.Score=0
        self.label_4.setText("Score : "+str(self.Score))

        self.state=1
        self.StartGame.setEnabled(False)
        self.StopGame.setEnabled(True)
        self.NewGame.setEnabled(True)
            
    
    def MethodeStartGame(self):
        self.state=1
        self.StartGame.setEnabled(False)
        self.StopGame.setEnabled(True)
        self.NewGame.setEnabled(True)

    def MethodeStopGame(self):
        self.state=0
        self.StartGame.setEnabled(True)
        self.StopGame.setEnabled(False)
        self.NewGame.setEnabled(True)

        
        
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


    def play(self):
        while (True):
            if (self.state==1):
                self.step()
            time.sleep(self.speed)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())
    

    ##########  abdou brahmia
    ##########  computer sience 
    ##########  university 8 mai 1945
