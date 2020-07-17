# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1+2_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit, QFileDialog, QDialog


import pandas as pd
import numpy as np

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QFile
from PyQt5.QtGui import QFont
from UI.Parameters_QDialog_UI import Ui_Dialog
from Data_class import Data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.data = Data()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumWidth(900)
        MainWindow.setMinimumHeight(500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(40, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data = QtWidgets.QWidget()
        self.tab_data.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_data.sizePolicy().hasHeightForWidth())
        self.tab_data.setSizePolicy(sizePolicy)
        self.tab_data.setMinimumSize(QtCore.QSize(700, 0))
        self.tab_data.setObjectName("tab_data")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_data)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.browse_button = QtWidgets.QPushButton(self.tab_data)
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout_4.addWidget(self.browse_button)
        self.filepath_textedit = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit.setEnabled(True)
        self.download_btn = QtWidgets.QPushButton(self.tab_data)
        self.download_btn.setObjectName("download_btn")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filepath_textedit.sizePolicy().hasHeightForWidth())
        self.filepath_textedit.setSizePolicy(sizePolicy)
        self.filepath_textedit.setMinimumSize(QtCore.QSize(500, 50))
        self.filepath_textedit.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit.setUndoRedoEnabled(True)
        self.filepath_textedit.setReadOnly(False)
        self.filepath_textedit.setObjectName("filepath_textedit")
        self.filepath_textedit.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_4.addWidget(self.filepath_textedit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.browse_button2 = QtWidgets.QPushButton(self.tab_data)
        self.browse_button2.setObjectName("browse_button2")
        self.horizontalLayout_11.addWidget(self.browse_button2)
        self.filepath_textedit2 = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filepath_textedit2.sizePolicy().hasHeightForWidth())
        self.filepath_textedit2.setSizePolicy(sizePolicy)
        self.filepath_textedit2.setMinimumSize(QtCore.QSize(500, 50))
        self.filepath_textedit2.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit2.setUndoRedoEnabled(True)
        self.filepath_textedit2.setReadOnly(False)
        self.filepath_textedit2.setObjectName("filepath_textedit2")
        self.filepath_textedit2.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_11.addWidget(self.filepath_textedit2)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.browse_button3 = QtWidgets.QPushButton(self.tab_data)
        self.browse_button3.setObjectName("browse_button3")
        self.horizontalLayout_12.addWidget(self.browse_button3)
        self.filepath_textedit3 = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filepath_textedit3.sizePolicy().hasHeightForWidth())
        self.filepath_textedit3.setSizePolicy(sizePolicy)
        self.filepath_textedit3.setMinimumSize(QtCore.QSize(500, 50))
        self.filepath_textedit3.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit3.setUndoRedoEnabled(True)
        self.filepath_textedit3.setReadOnly(False)
        self.filepath_textedit3.setObjectName("filepath_textedit3")
        self.filepath_textedit3.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_12.addWidget(self.filepath_textedit3)
        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.data_prmrs_button = QtWidgets.QPushButton(self.tab_data)
        self.data_prmrs_button.setObjectName("common_prmrs_button")
        self.data_prmrs_button.setMaximumWidth(100)
        self.data_prmrs_button.setMaximumHeight(30)
        self.verticalLayout.addWidget(self.download_btn)
        self.verticalLayout.addWidget(self.data_prmrs_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.plot_2 = QtWidgets.QWidget(self.tab_data)
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_5.addWidget(self.plot_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plot_1 = QtWidgets.QWidget(self.tab_data)
        self.plot_1.setObjectName("plot_1")
        self.verticalLayout_6.addWidget(self.plot_1)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_model = QtWidgets.QWidget()
        self.tab_model.setObjectName("tab_model")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_model)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.well_type_combo = QtWidgets.QComboBox(self.tab_model)
        self.well_type_combo.setObjectName("well_type_combo")
        self.well_type_combo.addItem("")
        self.well_type_combo.addItem("")
        self.well_type_combo.addItem("")
        self.well_type_combo.addItem("")
        self.verticalLayout_9.addWidget(self.well_type_combo)
        self.form_of_area_combo = QtWidgets.QComboBox(self.tab_model)
        self.form_of_area_combo.setObjectName("form_of_area_combo")
        self.form_of_area_combo.addItem("")
        self.form_of_area_combo.addItem("")
        self.verticalLayout_9.addWidget(self.form_of_area_combo)
        self.boundaries_type_combo = QtWidgets.QComboBox(self.tab_model)
        self.boundaries_type_combo.setEditable(False)
        self.boundaries_type_combo.setObjectName("boundaries_type_combo")
        self.boundaries_type_combo.addItem("")
        self.boundaries_type_combo.addItem("")
        self.boundaries_type_combo.addItem("")
        self.verticalLayout_9.addWidget(self.boundaries_type_combo)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.model_prmrs_button = QtWidgets.QPushButton(self.tab_model)
        self.model_prmrs_button.setObjectName("model_prmrs_button")
        self.horizontalLayout_5.addWidget(self.model_prmrs_button)
        self.prmrs_dunno_button = QtWidgets.QPushButton(self.tab_model)
        self.prmrs_dunno_button.setObjectName("prmrs_dunno_button")
        self.horizontalLayout_5.addWidget(self.prmrs_dunno_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plot_3 = QtWidgets.QWidget(self.tab_model)
        self.plot_3.setObjectName("plot_3")
        self.verticalLayout_7.addWidget(self.plot_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.plot_4 = QtWidgets.QWidget(self.tab_model)
        self.plot_4.setObjectName("plot_4")
        self.verticalLayout_8.addWidget(self.plot_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_model, "")
        self.tab_adaptation = QtWidgets.QWidget()
        self.tab_adaptation.setObjectName("tab_adaptation")
        self.tabWidget.addTab(self.tab_adaptation, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        f = open('Design/Data_tab_stylesheet.py', 'r')
        self.styleData = f.read()
        f.close()
        self.setStyleSheet(self.styleData)

        self.browse_button.clicked.connect(self.browse_file_P_bh)
        self.browse_button2.clicked.connect(self.browse_file_Q_liq)
        self.browse_button3.clicked.connect(self.browse_file_Q_oil)
        self.filepath_textedit.textChanged.connect(self.update_path_P_bh)
        self.filepath_textedit2.textChanged.connect(self.update_path_Q_liq)
        self.filepath_textedit3.textChanged.connect(self.update_path_Q_oil)
        self.download_btn.clicked.connect(self.load_data)
        self.data_prmrs_button.clicked.connect(self.show_prmrs_selection)

    def browse_file_P_bh(self, data):
        self.data.f_path_P_bh = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit.setText(self.data.f_path_P_bh)
        self.data.filename_P_bh, self.data.file_extension_P_bh = os.path.splitext(self.data.f_path_P_bh)

    def browse_file_Q_liq(self):
        self.data.f_path_Q_liq = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit2.setText(self.data.f_path_Q_liq)
        self.data.filename_Q_liq, self.data.file_extension_Q_liq = os.path.splitext(self.data.f_path_Q_liq)

    def browse_file_Q_oil(self):
        self.data.f_path_Q_oil = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit3.setText(self.data.f_path_Q_oil)
        self.data.filename_Q_oil, self.data.file_extension_Q_oil = os.path.splitext(self.data.f_path_Q_oil)

    def update_path_P_bh(self):
        self.data.f_path_P_bh = self.filepath_textedit.toPlainText()
        self.data.filename_P_bh, self.data.file_extension_P_bh = os.path.splitext(self.data.f_path_P_bh)

    def update_path_Q_liq(self):
        self.data.f_path_Q_liq = self.filepath_textedit2.toPlainText()
        self.data.filename_Q_liq, self.data.file_extension_Q_liq = os.path.splitext(self.data.f_path_Q_liq)

    def update_path_Q_oil(self):
        self.data.f_path_Q_oil = self.filepath_textedit3.toPlainText()
        self.data.filename_Q_oil, self.data.file_extension_Q_oil = os.path.splitext(self.data.f_path_Q_oil)

    def load_data(self):
        if self.data.file_extension_P_bh == '.xlsx':
            self.data.xl_P_bh = pd.ExcelFile(self.data.f_path_P_bh)
            self.filepath_textedit.setPlainText('File received.')
        else:
            self.filepath_textedit.setPlainText('Error!!! Wrong input file extension! .xlsx only!')
        if self.data.file_extension_Q_liq == '.xlsx':
            self.data.xl_Q_liq = pd.ExcelFile(self.data.f_path_Q_liq)
            self.filepath_textedit2.setPlainText('File received.')
        else:
            self.filepath_textedit2.setPlainText('Error!!! Wrong input file extension! .xlsx only!')
        if self.data.file_extension_Q_oil == '.xlsx':
            self.data.xl_Q_oil = pd.ExcelFile(self.data.f_path_Q_oil)
            self.filepath_textedit3.setPlainText('File received.')
        else:
            self.filepath_textedit3.setPlainText('Error!!! Wrong input file extension! .xlsx only!')


    def show_prmrs_selection(self):
        self.dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(self.dialog)
        self.dialog.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Browse File P_забойное"))
        self.browse_button2.setText(_translate("MainWindow", "Browse File Q_жидкости"))
        self.browse_button3.setText(_translate("MainWindow", "Browse File Q_нефти"))
        self.download_btn.setText(_translate("MainWindow", "Ok"))
        self.data_prmrs_button.setText(_translate("MainWindow", "Parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.well_type_combo.setItemText(0, _translate("MainWindow", "Vertical well"))
        self.well_type_combo.setItemText(1, _translate("MainWindow", "Horizontal well"))
        self.well_type_combo.setItemText(2, _translate("MainWindow", "ВС с МГРП"))
        self.well_type_combo.setItemText(3, _translate("MainWindow", "ГС с МГРП"))
        self.form_of_area_combo.setItemText(0, _translate("MainWindow", "Круговая область"))
        self.form_of_area_combo.setItemText(1, _translate("MainWindow", "Прямоугольная"))
        self.boundaries_type_combo.setCurrentText(_translate("MainWindow", "Mixed boundaries"))
        self.boundaries_type_combo.setItemText(0, _translate("MainWindow", "Mixed boundaries"))
        self.boundaries_type_combo.setItemText(1, _translate("MainWindow", "Непроницаемые"))
        self.boundaries_type_combo.setItemText(2, _translate("MainWindow", "Границы поддержания постоянного давления"))
        self.model_prmrs_button.setText(_translate("MainWindow", "Model parameters"))
        self.prmrs_dunno_button.setText(_translate("MainWindow", "Parameters ????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_model), _translate("MainWindow", "Model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_adaptation), _translate("MainWindow", "Adaptation"))