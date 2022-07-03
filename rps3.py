# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
b=0
c=0
x=0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(570, 740))
        MainWindow.setMaximumSize(QtCore.QSize(570, 740))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("allhand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    color: rgb(249, 240, 107);\n"
"    \n"
"    background-color: rgb(61, 56, 70);\n"
"    border-color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(152, 106, 68);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rock = QtWidgets.QPushButton(self.centralwidget)
        self.rock.setGeometry(QtCore.QRect(70, 180, 100, 100))
        self.rock.setStyleSheet("QPushButton{\n"
"    background-color: rgb(154, 153, 150);\n"
"    border-color: rgb(36, 31, 49);\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(222, 221, 218);\n"
"}")
        self.rock.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rock.setIcon(icon1)
        self.rock.setIconSize(QtCore.QSize(100, 90))
        self.rock.setDefault(True)
        self.rock.setObjectName("rock")
        self.scisor = QtWidgets.QPushButton(self.centralwidget)
        self.scisor.setEnabled(True)
        self.scisor.setGeometry(QtCore.QRect(390, 180, 100, 100))
        self.scisor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scisor.setAutoFillBackground(False)
        self.scisor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(154, 153, 150);\n"
"    \n"
"    border-top-color: rgb(192, 97, 203);\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(222, 221, 218);\n"
"}")
        self.scisor.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("scissor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scisor.setIcon(icon2)
        self.scisor.setIconSize(QtCore.QSize(100, 100))
        self.scisor.setCheckable(False)
        self.scisor.setDefault(True)
        self.scisor.setObjectName("scisor")
        self.paper = QtWidgets.QPushButton(self.centralwidget)
        self.paper.setGeometry(QtCore.QRect(230, 180, 100, 100))
        self.paper.setStyleSheet("QPushButton{\n"
"    background-color: rgb(154, 153, 150);\n"
"    border-color: rgb(36, 31, 49);\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(222, 221, 218);\n"
"}\n"
"")
        self.paper.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paper.setIcon(icon3)
        self.paper.setIconSize(QtCore.QSize(100, 100))
        self.paper.setDefault(True)
        self.paper.setObjectName("paper")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 300, 100, 40))
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel{\n"
"    border-radius:20px;\n"
"    \n"
"    background-color: rgb(229, 165, 10);\n"
"    font: 63 11pt \"Corbel Light\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 300, 100, 40))
        self.label_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("QLabel{\n"
"    border-radius:20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 63 11pt \"Corbel Light\";\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 300, 100, 41))
        self.label_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: rgb(40, 206, 224);\n"
"    font: 63 11pt \"Corbel Light\";\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 30, 421, 131))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(222, 221, 218);\n"
"    border-radius: 8px; \n"
"    border-color: rgb(229, 165, 10);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(23)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(280, 70, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(103, 420, 175, 71))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"    background-color: rgb(154, 153, 150);\n"
"   border-radius: 5px;\n"
"border :1px solid white;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(103, 380, 175, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"background-color: rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(277, 380, 180, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"background-color: rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(277, 420, 180, 71))
        font = QtGui.QFont()
        font.setFamily("Artifakt Element")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"    background-color: rgb(154, 153, 150);\n"
"   border-radius: 5px;\n"
"border :1px solid white;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 510, 300, 150))
        self.label_11.setMinimumSize(QtCore.QSize(300, 150))
        self.label_11.setMaximumSize(QtCore.QSize(300, 150))
        # self.label_11.setStyleSheet("QLabel{\n"
        # "background-color: rgb(61, 56, 70);\n"
        # "border-radius:8px;\n"
        # "}")
        self.label_11.setText("")
        #self.label_11.setPixmap(QtGui.QPixmap("lose.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.rock.raise_()
        self.paper.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.scisor.raise_()
        self.label_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setStyleSheet("QMenuBar{\n"
"    background-color: rgb(97, 53, 131);\n"
"border-radius:5px;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setMinimumSize(QtCore.QSize(150, 0))
        self.menuOptions.setMaximumSize(QtCore.QSize(150, 16777215))
        self.menuOptions.setAutoFillBackground(False)
        self.menuOptions.setStyleSheet("QMenu{\n"
"    background-color: rgb(154, 153, 150);\n"
"    border-radius:5px;\n"
"}")
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionRestart)
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.rock.clicked.connect(lambda:self.play(1))
        self.paper.clicked.connect(lambda:self.play(2))
        self.scisor.clicked.connect(lambda:self.play(3))

        self.actionRestart.triggered.connect(self.restart)
        self.actionQuit.triggered.connect(self.quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rodk pePPar Sijor"))
        self.label.setText(_translate("MainWindow", "ROCK"))
        self.label_2.setText(_translate("MainWindow", "PAPER"))
        self.label_3.setText(_translate("MainWindow", "SCISSOR"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#e5a50a;\">Rock</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Paper"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3584e4;\">Scissor</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "User"))
        self.label_9.setText(_translate("MainWindow", "Computer"))
        self.label_10.setText(_translate("MainWindow", "-"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionRestart.setShortcut(_translate("MainWindow", "R"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Q"))
    def play(self,n):
        global b,c,x
        a = random.randint(1,3)    
        print(a)
        #print(d)
        self.judge(a,n)
        d = str(b)
        e = str(c)
        self.label_8.setText(d)
        self.label_10.setText(e)
        n=0
        print(b)
        print(c)
        print(x)
        x+=1 
        if x == 3 :
                self.rock.setEnabled(False)
                self.paper.setEnabled(False)
                self.scisor.setEnabled(False)
                if b == c :
                        print("tie")
                        self.label_11.setStyleSheet("QLabel{\n"
                        "background-color: rgb(119, 118, 123);\n"
                        "border-radius:8px;\n"
                        "}")
                        self.label_11.setPixmap(QtGui.QPixmap("tie.png"))
                elif b>c:
                        print("b win")
                        self.label_11.setStyleSheet("QLabel{\n"
                        "background-color: rgb(119, 118, 123);\n"
                        "border-radius:8px;\n"
                        "}")
                        self.label_11.setPixmap(QtGui.QPixmap("win.png"))
                else:
                        print("c win")
                        self.label_11.setStyleSheet("QLabel{\n"
                        "background-color: rgb(119, 118, 123);\n"
                        "border-radius:8px;\n"
                        "}")
                        self.label_11.setPixmap(QtGui.QPixmap("lose.png"))
        else:
                pass
                                  
    
    # 1 rock 2 paper 3 scissor
    def judge(self,a,n):
        global b,c
        if a == n:
                print("same")
        elif n == 1:
                if a == 2:
                        print("lost to paper")
                        c+=1
                else :
                        print("won ro scijor")
                        b+=1
        elif n == 2:
                if a == 1:
                        print("won to a rdok")
                        b+=1
                else :
                        print("lost to scijor")
                        c+=1
        elif n == 3:
                if a == 2:
                        print("lost to rodk")
                        c+=1
                else :
                        print("won to paper")
                        b+=1       

    def restart(self):
        global b,c,x
        b = 0
        c = 0
        x = 0
        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scisor.setEnabled(True)
        self.label_8.setText("-")
        self.label_10.setText("-")
        self.label_11.setStyleSheet("QLabel{\n"
        "background-color: rgb(61, 56, 70);\n"
        "border-radius:8px;\n"
        "}")
        self.label_11.setPixmap(QtGui.QPixmap(""))

    def quit(self):
        print("Over")
        sys.exit(app.exec_())    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
