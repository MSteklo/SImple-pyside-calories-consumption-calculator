# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Aug  2 22:27:38 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(349, 359)
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setWindowIcon(QtGui.QIcon('food.png'))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(414, 18))
        self.label_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(198, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        #self.label_4.setStyleSheet("-moz-border-radius: 10px;")
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Raised)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(198, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        #self.label_6.setStyleSheet("-moz-border-radius: 10px;")
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtGui.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximumSize(QtCore.QSize(198, 50))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(150)  # Задаю максимально возможное значение
        self.spinBox_2.setMinimum(1)  # Задаю минимально возможное значение
        self.spinBox_2.setWrapping(True)  # Делаю возможным циклическую прокрутку спинбокса
        self.spinBox_2.setSuffix(" yr")  # Делаю приставку kg к значения в сминбоксе
        self.gridLayout_2.addWidget(self.spinBox_2, 2, 1, 1, 1)
        self.spinBox_3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_3.setMaximumSize(QtCore.QSize(198, 50))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(300)  # Задаю максимально возможное значение
        self.spinBox_3.setMinimum(50)  # Задаю минимально возможное значение
        self.spinBox_3.setWrapping(True)  # Делаю возможным циклическую прокрутку спинбокса
        self.spinBox_3.setSuffix(" cm")  # Делаю приставку kg к значения в сминбоксе
        self.gridLayout_2.addWidget(self.spinBox_3, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(198, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        #self.label_5.setStyleSheet("-moz-border-radius: 10px;")
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtGui.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setMaximumSize(QtCore.QSize(198, 50))
        self.spinBox.setMaximum(200)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(200)  # Задаю максимально возможное значение
        self.spinBox.setMinimum(20)  # Задаю минимально возможное значение
        self.spinBox.setWrapping(True)  # Делаю возможным циклическую прокрутку спинбокса
        self.spinBox.setSuffix(" kg")  # Делаю приставку kg к значения в сминбоксе
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Radiomale = QtGui.QRadioButton(self.groupBox)
        self.Radiomale.setMaximumSize(QtCore.QSize(198, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Radiomale.setFont(font)
        self.Radiomale.setCursor(QtCore.Qt.PointingHandCursor)
        self.Radiomale.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Radiomale.setIconSize(QtCore.QSize(16, 16))
        self.Radiomale.setObjectName("Radiomale")
        self.horizontalLayout_2.addWidget(self.Radiomale)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.Radiofemale = QtGui.QRadioButton(self.groupBox)
        self.Radiofemale.setMaximumSize(QtCore.QSize(198, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Radiofemale.setFont(font)
        self.Radiofemale.setCursor(QtCore.Qt.PointingHandCursor)
        self.Radiofemale.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Radiofemale.setIconSize(QtCore.QSize(16, 16))
        self.Radiofemale.setObjectName("Radiofemale")
        self.horizontalLayout_2.addWidget(self.Radiofemale)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(331, 20))
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setMaximumSize(QtCore.QSize(123, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton.setIconSize(QtCore.QSize(16, 16))
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setMaximumSize(QtCore.QSize(123, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_2.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setMaximumSize(QtCore.QSize(500, 32))
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#39BA42;\n"
"font-weight:bold;\n"
"font-size:18px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
" background-color:lightblue\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(16, 25))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setMaximumSize(QtCore.QSize(123, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_4.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setMaximumSize(QtCore.QSize(123, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_3.setAutoFillBackground(False)
        self.radioButton_3.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 3, 1, 1)
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setMaximumSize(QtCore.QSize(144, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.radioButton_5.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 0, 5, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 4, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setMaximumSize(QtCore.QSize(414, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtGui.QSpacerItem(127, 45, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(201, 45))
        self.label.setMargin(10)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(64, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setWhatsThis("")
        self.lcdNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setMidLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setSizeGripEnabled(0)
        self.statusbar.setStyleSheet("color: rgb(255, 0, 0)")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BZU SIMPLE CALCULATOR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "The result can only be calculated for an average build person", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "WEIGHT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "AGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "HEIGHT", None, QtGui.QApplication.UnicodeUTF8))
        self.Radiomale.setText(QtGui.QApplication.translate("MainWindow", "I AM A MALE", None, QtGui.QApplication.UnicodeUTF8))
        self.Radiofemale.setText(QtGui.QApplication.translate("MainWindow", "I AM A FEMALE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#0000ff;\">What is your activity level?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "VERY LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "HIGHEST", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#0000ff;\">Press for result</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "GET RESULTS", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("MainWindow", "HIGH", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "LOW", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("MainWindow", "AVERAGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">YOUR RESULT IS:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lcdNumber.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">Your current BZU</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setStatusTip(QtGui.QApplication.translate("MainWindow", " ", None, QtGui.QApplication.UnicodeUTF8))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     MainWindow = QtGui.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

