# coding=utf-8
# It is a main program script

import sys
from bzustatus import *  # Импортирую интерфейс
from PySide import QtGui




class Logic(QtGui.QMainWindow):  # Creating a main class
    def __init__(self):

        def get_results():
            minimal = float(1.2)    # Very low activity
            low = float(1.375)      # Low activity
            average = float(1.55)   # Average activity
            high = float(1.725)     # High activity
            veryhigh = float(1.9)   # Highest activity

            if ui.Radiomale.isChecked() == 1:    # Если выбрано I am a male
                bmr = 88.36 + (13.4 * ui.spinBox.value()) + (4.8 * ui.spinBox_3.value()) - (5.7 * ui.spinBox_2.value())
                bmr = round(bmr)
                if ui.radioButton.isChecked() == 1:
                    result = minimal * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_3.isChecked() == 1:
                    result = low * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_5.isChecked() == 1:
                    result = average * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_4.isChecked() == 1:
                    result = high * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_2.isChecked() == 1:
                    result = veryhigh * bmr
                    ui.statusbar.showMessage(("Success"))
                else:
                    ui.statusbar.showMessage(("Choose your activity level"), 3000)
                result = round(result)
                ui.lcdNumber.display(result)
            elif ui.Radiofemale.isChecked() == 1:  # Если выбрано I am a female
                bmr = 447.6 + (9.2 * ui.spinBox.value()) + (3.1 * ui.spinBox_3.value()) - (4.3 * ui.spinBox_2.value())
                bmr = round(bmr)
                if ui.radioButton.isChecked() == 1:
                    result = minimal * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_3.isChecked() == 1:
                    result = low * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_5.isChecked() == 1:
                    result = average * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_4.isChecked() == 1:
                    result = high * bmr
                    ui.statusbar.showMessage(("Success"))
                elif ui.radioButton_2.isChecked() == 1:
                    result = veryhigh * bmr
                    ui.statusbar.showMessage(("Success"))

                else:
                    ui.statusbar.showMessage(("Choose your activity level"), 3000)
                result = round(result)
                ui.lcdNumber.display(result)
                print(result)

            else:
                ui.statusbar.showMessage(("Choose your sex"), 3000)

        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.statusbar.showMessage(("Program launched successfully"), 1000)


        # Основная логика приложения
        ui.pushButton.clicked.connect(get_results)



        # Делаю зацикливание появления главного окна
        sys.exit(app.exec_())


qqq = Logic()  # Создаю объект класса Logic
