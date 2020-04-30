# -*- coding: utf-8 -*-

version = '0.0.1'


#################################################################
# Code réalisé par Squall'ss 4Li218 et Kar'sCarate'ss 129Li218
# dans le cadre du projet de métrologie Sujet 1 : Lien ZEISS CALYPSO-> DIGITAL SURF MOUNTAINS
# et P16+-> DIGITAL SURF MOUNTAINS
# dirigé par Mr Corevits
##################################################################

import sys
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


from PyQt5.QtWidgets import *

from menu import Ui_MainWindow
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

PATHFILE_TO_ANALYSE = ''
FILE_TYPE = ''

class Ecran_menuPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        global FILE_TYPE
        QtWidgets.QMainWindow.__init__(self)

        # Configure l'interface utilisateur.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("ZEISS converter")
        self.setWindowIcon(QtGui.QIcon("image/icon.png"))

        self.ui.UI_TEXT_VERSION_NUMBER.setText(version)

        # images
        pixmap = QPixmap('image/logo_plot.png').scaledToHeight(100)
        self.ui.UI_LABEL_PLOT.setPixmap(pixmap)
        pixmap = QPixmap('image/logo_validation.png').scaledToHeight(50)
        self.ui.UI_LABEL_LOGO_VALIDER.setPixmap(pixmap)
        pixmap = QPixmap('image/logo_add.png').scaledToHeight(50)
        self.ui.label_2.setPixmap(pixmap)

        # button
        self.ui.UI_BUTTON_CHOOSE.clicked.connect(self.choose_file)
        self.ui.UI_BUTTON_CONVERT.clicked.connect(self.convert)
        self.ui.UI_BUTTON_SAVE.clicked.connect(self.save)
        self.ui.UI_BUTTON_AGAIN.clicked.connect(self.again)

        # radio buttons
        self.ui.UI_RADIO_ZEISS.setChecked(True)
        FILE_TYPE = 'zeiss'
        self.ui.UI_RADIO_ZEISS.toggled.connect(self.onClickedZeiss)
        self.ui.UI_RADIO_P16.toggled.connect(self.onClickedP16)

        self.status = 'choose_file'
        self.update_ui_widgets_enabled()
        self.statusBar().hide()
        #self.statusBar().showMessage('Ready')  # érit ready en bas à gauche


    def onClickedZeiss(self):
        global FILE_TYPE
        FILE_TYPE = 'zeiss'

    def onClickedP16(self):
        global FILE_TYPE
        FILE_TYPE = 'p16'

    def update_ui_widgets_enabled(self):
        if self.status == 'choose_file':
            #choose_file
            self.ui.label_2.setEnabled(True)
            self.ui.UI_BUTTON_CHOOSE.setEnabled(True)

            #convert
            self.ui.UI_RADIO_ZEISS.setEnabled(False)
            self.ui.UI_RADIO_P16.setEnabled(False)
            self.ui.UI_BUTTON_CONVERT.setEnabled(False)

            # save
            self.ui.UI_LABEL_PLOT.setEnabled(False)
            self.ui.UI_BUTTON_SAVE.setEnabled(False)
            self.ui.label_3.setEnabled(False)

            # valider
            self.ui.UI_LABEL_LOGO_VALIDER.setEnabled(False)
            self.ui.UI_BUTTON_AGAIN.setEnabled(False)

        elif self.status == 'convert':
            # choose_file
            self.ui.label_2.setEnabled(False)
            self.ui.UI_BUTTON_CHOOSE.setEnabled(False)

            # convert
            self.ui.UI_RADIO_ZEISS.setEnabled(True)
            self.ui.UI_RADIO_P16.setEnabled(True)
            self.ui.UI_BUTTON_CONVERT.setEnabled(True)

            # save
            self.ui.UI_LABEL_PLOT.setEnabled(False)
            self.ui.UI_BUTTON_SAVE.setEnabled(False)
            self.ui.label_3.setEnabled(False)

            # valider
            self.ui.UI_LABEL_LOGO_VALIDER.setEnabled(False)
            self.ui.UI_BUTTON_AGAIN.setEnabled(False)

        elif self.status == 'save':
            # choose_file
            self.ui.label_2.setEnabled(False)
            self.ui.UI_BUTTON_CHOOSE.setEnabled(False)

            #convert
            self.ui.UI_RADIO_ZEISS.setEnabled(False)
            self.ui.UI_RADIO_P16.setEnabled(False)
            self.ui.UI_BUTTON_CONVERT.setEnabled(False)

            # save
            self.ui.UI_LABEL_PLOT.setEnabled(True)
            self.ui.UI_BUTTON_SAVE.setEnabled(True)
            self.ui.label_3.setEnabled(True)

            # valider
            self.ui.UI_LABEL_LOGO_VALIDER.setEnabled(False)
            self.ui.UI_BUTTON_AGAIN.setEnabled(False)

        elif self.status == 'again':
            # choose_file
            self.ui.label_2.setEnabled(False)
            self.ui.UI_BUTTON_CHOOSE.setEnabled(False)

            #convert
            self.ui.UI_RADIO_ZEISS.setEnabled(False)
            self.ui.UI_RADIO_P16.setEnabled(False)
            self.ui.UI_BUTTON_CONVERT.setEnabled(False)

            # save
            self.ui.UI_LABEL_PLOT.setEnabled(False)
            self.ui.UI_BUTTON_SAVE.setEnabled(False)
            self.ui.label_3.setEnabled(False)

            # valider
            self.ui.UI_LABEL_LOGO_VALIDER.setEnabled(True)
            self.ui.UI_BUTTON_AGAIN.setEnabled(True)

        pass

    def choose_file(self):
        global PATHFILE_TO_ANALYSE

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choisir un fichier à convertir", os.path.expanduser("~\\Desktop"),"All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            PATHFILE_TO_ANALYSE = fileName

            # at the end of function
            self.status = 'convert'
            self.update_ui_widgets_enabled()


    def convert(self):
        #dialog = QtWidgets.QDialog()
        #dialog.ui = Form()
        #dialog.ui.setupUi(dialog)
        dialog = Actions()
        dialog.exec_()
        dialog.show()

        #

        self.status = 'save'
        self.update_ui_widgets_enabled()
        pass

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Sauvergarder fichier sous",os.path.expanduser("~\\Desktop"),"All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            print(os.getcwd()+'/temp.txt')
            if fileName.split('.')[-1] != ('txt'): fileName += '.txt'
            shutil.move(os.getcwd()+'/temp.txt', fileName)
            self.ui.label_3.setText(fileName)

            # here is the picture generated
            #fileName = fileName[:-3] + 'png'
            #shutil.move(os.getcwd() + '/profile.png', fileName)



            self.status = 'again'
            self.update_ui_widgets_enabled()

    def again(self):
        self.ui.label_3.setText("Le fichier n'est pas enregistré")
        self.status = 'choose_file'
        self.update_ui_widgets_enabled()
        pass


import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 4


class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        global PATHFILE_TO_ANALYSE
        global FILE_TYPE
        self.count = 0
        #super().statusBar().showMessage(PATHFILE_TO_ANALYSE, '  type: ', FILE_TYPE)
        print("in boucle ->", PATHFILE_TO_ANALYSE, FILE_TYPE)
        self.count = 0
        if FILE_TYPE == 'p16':
            self.p16_to_mountains_converter()
        elif FILE_TYPE == 'zeiss':
            print("La Zeiss suprême n'a pas encore été implémentée")
        else:
            print("""ERROR: Le type de fichier n'est pas sélectionné""")


    def p16_to_mountains_converter(self):
        l_x_plot = []
        l_y_plot = []
        l_z_plot = []
        global PATHFILE_TO_ANALYSE
        file_import = open(PATHFILE_TO_ANALYSE, 'r')
        lignes = file_import.readlines()
        file_import.close()

        file_export = open('temp.txt', 'w')

        # repr is used to visualise specials caracters
        # print(repr(file.readlines()[15]))
        # extraction of first data
        for i in range(11):
            line = lignes[i]
            line_l = line.split('\t')
            if line_l[0] == 'Number of Points':
                nb_points = int(line_l[1])
            elif line_l[0] == 'Number of Traces':
                nb_traces = int(line_l[1])
            elif line_l[0] == 'X-Resolution':
                x_res = float(line_l[1])
            elif line_l[0] == 'Y-Resolution':
                y_res = float(line_l[1])

        for i in range(nb_points):
            # print(i, '=>', lignes[11+i])
            ligne = lignes[11 + i].split('\t')[1::]  # delete first number which is line number
            for j, point in enumerate(ligne):
                #print('point', point)
                X = x_res * i
                Y = y_res * j
                Z = float(point) * 0.0001  # conversion amstrum->micron
                new_line = str(X) + ',' + str(Y) + ',' + str(Z) + '\n'

                file_export.write(new_line)  # write new line

                l_x_plot.append(X)
                l_y_plot.append(Y)
                l_z_plot.append(Z)
                self.count += 100/nb_points
                self.countChanged.emit(self.count)

        file_export.close()

        # create a 3D plot is too heavy with big files
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')

        #ax.plot_trisurf(np.array(l_x_plot), np.array(l_y_plot), np.array(l_z_plot), cmap=cm.coolwarm, linewidth=0.2,
        #                antialiased=True)

        #plt.savefig('profile.png')




class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chargement en cours')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        #self.button = QPushButton('Start', self)
        #self.button.move(0, 30)
        self.show()

        #self.button.clicked.connect(self.onButtonClick)

    #def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)


if __name__ == "__main__":
    #PyQT5
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("plastique"))

    selection = Ecran_menuPrincipal()
    selection.show()
    sys.exit(app.exec_())