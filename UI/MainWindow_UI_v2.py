# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1+2_tabs_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(1200, 700))
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
        self.browse_button.setMaximumSize(QtCore.QSize(200, 40))
        self.horizontalLayout_4.addWidget(self.browse_button)
        self.filepath_textedit = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit.setMinimumSize(QtCore.QSize(0, 50))
        self.filepath_textedit.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit.setObjectName("filepath_textedit")
        self.filepath_textedit.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_4.addWidget(self.filepath_textedit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.browse_button2 = QtWidgets.QPushButton(self.tab_data)
        self.browse_button2.setObjectName("browse_button2")
        self.browse_button2.setMaximumSize(QtCore.QSize(200, 40))
        self.horizontalLayout_3.addWidget(self.browse_button2)
        self.filepath_textedit2 = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit2.setMinimumSize(QtCore.QSize(0, 50))
        self.filepath_textedit2.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit2.setObjectName("filepath_textedit2")
        self.filepath_textedit2.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_3.addWidget(self.filepath_textedit2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.browse_button3 = QtWidgets.QPushButton(self.tab_data)
        self.browse_button3.setObjectName("browse_button3")
        self.browse_button3.setMaximumSize(QtCore.QSize(200, 40))
        self.horizontalLayout_6.addWidget(self.browse_button3)
        self.filepath_textedit3 = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit3.setMinimumSize(QtCore.QSize(0, 50))
        self.filepath_textedit3.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit3.setObjectName("filepath_textedit3")
        self.filepath_textedit3.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout_6.addWidget(self.filepath_textedit3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.download_btn = QtWidgets.QPushButton(self.tab_data)
        self.download_btn.setObjectName("download_btn")
        self.download_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.download_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.verticalLayout.addWidget(self.download_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.prmrs_mini = QtWidgets.QTextEdit()
        self.prmrs_mini.setObjectName("prmrs_mini")
        self.prmrs_mini.setReadOnly(True)
        self.prmrs_mini.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.verticalLayout.addWidget(self.prmrs_mini)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.plot_2 = QtWidgets.QWidget(self.tab_data)
        self.plot_2.setMinimumSize(QtCore.QSize(500, 0))
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_5.addWidget(self.plot_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.common_prmrs_button = QtWidgets.QPushButton(self.tab_data)
        self.common_prmrs_button.setObjectName("common_prmrs_button")
        self.common_prmrs_button.setMinimumSize(QtCore.QSize(0, 40))
        self.common_prmrs_button.setMaximumSize(QtCore.QSize(240, 40))
        self.horizontalLayout_1.addWidget(self.common_prmrs_button)
        self.model_prmrs_button = QtWidgets.QPushButton(self.tab_model)
        self.model_prmrs_button.setObjectName("model_prmrs_button")
        self.model_prmrs_button.setMinimumSize(QtCore.QSize(0, 40))
        self.model_prmrs_button.setMaximumSize(QtCore.QSize(240, 40))
        self.horizontalLayout_1.addWidget(self.model_prmrs_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout__10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__10.setObjectName("horizontalLayout__10")
        self.load_prediction_btn = QtWidgets.QPushButton(self.tab_data)
        self.load_prediction_btn.setObjectName("load_prediction_btn")
        self.load_prediction_btn.setMaximumSize(QtCore.QSize(240, 40))
        self.horizontalLayout__10.addWidget(self.load_prediction_btn)
        self.filepath_textedit_4 = QtWidgets.QTextEdit(self.tab_data)
        self.filepath_textedit_4.setMinimumSize(QtCore.QSize(0, 50))
        self.filepath_textedit_4.setMaximumSize(QtCore.QSize(500, 50))
        self.filepath_textedit_4.setObjectName("filepath_textedit_4")
        self.filepath_textedit_4.setLineWrapMode(QTextEdit.NoWrap)
        self.horizontalLayout__10.addWidget(self.filepath_textedit_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout__10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout__11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__11.setObjectName("horizontalLayout__11")
        self.label_1 = QtWidgets.QLabel()
        self.label_1.setObjectName("label_1")
        self.horizontalLayout__11.addWidget(self.label_1)
        self.delta_prediction = QtWidgets.QLineEdit()
        self.delta_prediction.setObjectName("delta_prediction")

        regExp = QtCore.QRegExp(
            "[-]{0,1}\d{0,}\.\d{0,}")  # Валидатор на ввод только чисел и точки(используется для полей ввода)
        validator = QtGui.QRegExpValidator(regExp)

        self.delta_prediction.setValidator(validator)
        self.horizontalLayout__11.addWidget(self.delta_prediction)
        self.verticalLayout_9.addLayout(self.horizontalLayout__11)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.horizontalLayout__12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__12.setObjectName("horizontalLayout__12")
        self.calculate_btn = QtWidgets.QPushButton(self.tab_data)
        self.calculate_btn.setObjectName("calculate_btn")
        self.calculate_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.calculate_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.horizontalLayout__12.addWidget(self.calculate_btn)
        self.export_btn = QtWidgets.QPushButton(self.tab_data)
        self.export_btn.setObjectName("export_btn")
        self.export_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.export_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.horizontalLayout__12.addWidget(self.export_btn)
        self.verticalLayout_9.addLayout(self.horizontalLayout__12)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.prmrs_mini_2 = QtWidgets.QTextEdit()
        self.prmrs_mini_2.setReadOnly(True)
        self.prmrs_mini_2.setObjectName("prmrs_mini_2")
        self.prmrs_mini_2.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred))
        self.verticalLayout_9.addWidget(self.prmrs_mini_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plot_3 = QtWidgets.QWidget(self.tab_model)
        self.plot_3.setObjectName("plot_3")
        self.verticalLayout_7.addWidget(self.plot_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Выбрать файл: P_заб"))
        self.browse_button2.setText(_translate("MainWindow", "Выбрать файл: Q_liq"))
        self.browse_button3.setText(_translate("MainWindow", "Выбрать файл: Q_oil"))
        self.download_btn.setText(_translate("MainWindow", "Загрузить и построить графики"))
        self.common_prmrs_button.setText(_translate("MainWindow", "Общие параметры"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Данные"))
        self.model_prmrs_button.setText(_translate("MainWindow", "Параметры модели"))
        self.load_prediction_btn.setText(_translate("MainWindow", "Импорт данных прогнозирования"))
        self.label_1.setText(_translate("MainWindow", "Дискретность шага прогнозирования, ч :"))
        self.calculate_btn.setText(_translate("MainWindow", "Расчёт"))
        self.export_btn.setText(_translate("MainWindow", "Экспорт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_model), _translate("MainWindow", "Модель"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_adaptation), _translate("MainWindow", "Адаптация"))
