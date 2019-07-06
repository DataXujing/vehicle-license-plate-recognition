# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
# 'C:\Users\Administrator\Desktop\car_id_detect_reg\card_soft\my_main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# __author__ = xujing
# __date__ = 2019-07-05

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtGui import QFont,QIcon
import sys
import qtawesome

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/pic/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # 将按钮边框去掉，文字设置为白色，背景灰色
        qss1 = '''
        QPushButton{border:none;color:cyan;}
        QPushButton#pushButton_3{
            border:none;
            border-bottom:1px solid cyan;
            font-size:22px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        QPushButton#pushButton_4{
            border:none;
            border-bottom:1px solid cyan;
            font-size:22px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        QPushButton#pushButton_5{
            border:none;
            border-bottom:1px solid cyan;
            font-size:22px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        QPushButton#pushButton_8{
            border:none;
            border-bottom:1px solid cyan;
            font-size:15px;
            font-weight:900;
        }
        QPushButton#pushButton_3:hover{border-left:4px solid red;font-weight:700;}
        QPushButton#pushButton_4:hover{border-left:4px solid red;font-weight:700;}
        QPushButton#pushButton_5:hover{border-left:4px solid red;font-weight:700;}
        QPushButton#pushButton_8:hover{border-left:4px solid red;font-weight:700;}
        backfround:black;

       
        '''

        # 圆角窗口
        qss2 = '''#MainWindow{
            background:black;
            border-radius:30px
        }

        '''
        # 下拉列表样式
        qss3 = '''QComboBox{
            border: 1px solid cyan;
            border-radius:2px;
            color: white;
            select-background-color:cyan;
            background-color:black;
            selection-color:black;
        }
        '''

        # table qss
        qss4 = '''
        #tableWidget{
            border：none;
            border-color:cyan;
            background:black;
            color: cyan;
            font-size: 14px;
            font-weight:800;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        '''


        # graph qss
        qss5 = '''
        #graphicsView{
            border：none;
            border-color:cyan;
            background:black;
        }
        '''
        # button 6,7
        qss6 = '''
        QPushButton
        {  
            font-size:16px;
            font-weight:900;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            /* 前景色 */  
            color:rgb(248, 248, 255);  
         
            /* 背景色 */  
            background-color:rgb(0,229,238);  
         
            /* 边框风格 */  
            border-style:outset;  
         
            /* 边框宽度 */  
            border-width:2px;  
         
            /* 边框颜色 */  
            border-color:rgb(255,0,0);  
         
            /* 边框倒角 */  
            border-radius:10px;  
         
            /* 控件最小宽度 */  
            min-width:50px;  
         
            /* 控件最小高度 */  
            min-height:20px;  
         
            /* 内边距 */  
            padding:4px;  
        } 
         
        /* 鼠标按下时的效果 */ 
        QPushButton#pushButton:pressed 
        {  
            /* 改变背景色 */  
            background-color:rgb(0,255,127);  
         
            /* 改变边框风格 */  
            border-style:inset;  
         
            /* 使文字有一点移动 */  
            padding-left:3px;  
            padding-top:3px;  
        }
         
        /* 按钮样式 */ 
        QPushButton:flat 
        {  
            border:2px solid red;  
        } 
         
        /*鼠标悬浮时的效果*/
        QPushButton:hover
        {
            color:rgb(255, 222, 173);
            background-color:rgb(0,255,127); /*改变背景色*/
            border-style:inset;/*改变边框风格*/
            padding-left:3px;
            padding-top:3px;
        }

        '''
        MainWindow.setStyleSheet(qss2)

        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        MainWindow.setWindowOpacity(0.95) # 设置窗口透明度

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet(qss3)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 611, 501))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        QToolTip.setFont(QFont("SansSerif",6))
        self.pushButton.setToolTip("<b>最小化</b>")
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip("<b>关闭</b>")
        self.pushButton_2.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 90, 191, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/pic/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(qss1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(700, 140, 181, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 230, 191, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/pic/shibie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(qss1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(700, 290, 171, 41))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);font-size: 24px;font-weight:1000;")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 360, 181, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/pic/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(qss1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(700, 400, 181, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 492, 75, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pic/pic/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(qss6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 490, 71, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pic/pic/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(qss6)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet(qss1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "交通门禁车牌检测和识别系统"))
        self.pushButton.setText(_translate("MainWindow", "-"))
        self.pushButton_2.setText(_translate("MainWindow", "✘"))
        self.pushButton_3.setText(_translate("MainWindow", "车牌检测"))
        self.pushButton_4.setText(_translate("MainWindow", "车牌识别"))
        self.pushButton_5.setText(_translate("MainWindow", "车牌颜色"))
        self.pushButton_6.setText(_translate("MainWindow", "图像"))
        self.pushButton_7.setText(_translate("MainWindow", "视频"))
        self.pushButton_8.setText(_translate("MainWindow", "交通门禁车牌检测和识别系统"))

import my_pic_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

