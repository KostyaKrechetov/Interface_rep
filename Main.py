# -*- coding: utf-8 -*-
import sys
import os
from time import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout


# Импорт модуля расчётов дебита жидкости
from Calculations.Generate import Generate

# импорт UI для основного окна
from UI.MainWindow_UI_v2 import Ui_MainWindow

# импорт класса хранения данных и классов на базе UI
from Data_class import Data
from MplForWidget_Class import MyMplCanvas
from Common_parameters_UI_Class import Common_parameters
from Model_prmrs_UI_Class import Model_prmrs

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        screen_geometry = QApplication.desktop().availableGeometry()
        self.move(int(screen_geometry.width()/20), int(screen_geometry.height()/20))
        self.setWindowTitle('Модуль краткосрочного прогнозирования')
        self.data = Data()  # Класс хранения всех данных
        self.ax2 = []       # Список вторичных осей для верхнего графика
        self.fig, self.axes = self.initial_plot()       # Инициализируем графики на первых двух вкладках
        self.fig_2, self.axes_2 = self.initial_plot()
        self.data.MAX_x = 0
        self.data.MIN_x = 0

        f = open('Design/Data_tab_stylesheet.py', 'r')      # Применение стиля
        self.styleData = f.read()
        f.close()
        # self.setStyleSheet(self.styleData)
        self.statusbar.setStyleSheet(
            "QStatusBar{padding-left:8px;background:rgba(86, 123, 133, 1);;color:red;font-weight:bold;}")

        self.browse_button.clicked.connect(self.browse_file_P_bh)
        self.browse_button2.clicked.connect(self.browse_file_Q_liq)
        self.browse_button3.clicked.connect(self.browse_file_Q_oil)
        self.download_btn.clicked.connect(self.load_data)
        self.common_prmrs_button.clicked.connect(self.show_common_prmrs)
        self.model_prmrs_button.clicked.connect(self.show_model_prmrs_window)
        self.load_prediction_btn.clicked.connect(self.browse_file_prediction)
        self.calculate_btn.clicked.connect(self.calculate)
        self.export_btn.clicked.connect(self.export)
        self.export_btn.setDisabled(True)
        self.prmrs_mini_2.hide()
        self.prmrs_mini.hide()
        self.delta_prediction.setText(str(self.data.delta))

        # Добавляем график на 1 и 2 вкладки
        self.componovka_for_mpl = QVBoxLayout(self.plot_2)
        self.canvas = MyMplCanvas(self.fig)
        self.componovka_for_mpl.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.componovka_for_mpl.addWidget(self.toolbar)

        self.componovka_for_mpl_2 = QVBoxLayout(self.plot_3)
        self.canvas_2 = MyMplCanvas(self.fig_2)
        self.componovka_for_mpl_2.addWidget(self.canvas_2)
        self.toolbar_2 = NavigationToolbar(self.canvas_2, self)
        self.componovka_for_mpl_2.addWidget(self.toolbar_2)

    def browse_file_P_bh(self, data):
        self.data.f_path_P_bh = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit.setText(self.data.f_path_P_bh)

    def browse_file_Q_liq(self):
        self.data.f_path_Q_liq = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit2.setText(self.data.f_path_Q_liq)

    def browse_file_Q_oil(self):
        self.data.f_path_prediction = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit3.setText(self.data.f_path_prediction)

    def browse_file_prediction(self):
        self.data.f_path_prediction = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.filepath_textedit_4.setText(self.data.f_path_prediction)

    def load_data(self):
        notEmpty = False
        Correct = True
        fmts_date = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%d.%m.%Y']
        fmts_time = ['%H:%M:%S', '%H:%M']
        # Считываем данные по забойному давлению
        self.data.f_path_P_bh = self.filepath_textedit.toPlainText()
        filename_P_bh, file_extension_P_bh = os.path.splitext(self.data.f_path_P_bh)
        if file_extension_P_bh == '.xlsx':
            try:
                xl_P_bh = pd.ExcelFile(self.data.f_path_P_bh)
                df1 = xl_P_bh.parse('Лист1')
                self.data.P_bh = [float(elem) for elem in df1.P_bh]
                fmt = ''
                for fmt_ in fmts_date:  # Определение формата даты
                    try:
                        datetime.strptime(str(df1.date[0]).replace(',', '.'), fmt_)
                        fmt = fmt_
                    except:
                        pass
                self.data.date_P_bh = [datetime.strptime(str(elem).replace(',', '.'), fmt).date() for elem in
                                             df1.date]  # Преобразуем в объект date
                fmt = ''
                for fmt_ in fmts_time:  # Определение формата времени
                    try:
                        datetime.strptime(str(df1.time[0]), fmt_)
                        fmt = fmt_
                    except:
                        pass
                if isinstance(df1.time[0], str):
                    self.data.time_P_bh = [datetime.strptime(elem, fmt).time() for elem in
                                             df1.time]  # Преобразуем строку в объект time
                else:
                    self.data.time_P_bh = df1.time
                self.data.datetimes_P_bh = [datetime.combine(self.data.date_P_bh[i], self.data.time_P_bh[i]) for i in
                                             range(len(self.data.date_P_bh))]  # Преобразуем в объект datetime
                notEmpty = True
            except:
                self.filepath_textedit.setPlainText('Ошибка! Неверный формат файла или данных в нём. Столбцы должны быть названы: date|time|Q_oil')
                Correct = False
        else:
            self.filepath_textedit.setPlainText('Extension .xlsx only!')

        # Считываем данные по дебиту жидкости
        self.data.f_path_Q_liq = self.filepath_textedit2.toPlainText()
        filename_Q_liq, file_extension_Q_liq = os.path.splitext(self.data.f_path_Q_liq)
        if file_extension_Q_liq == '.xlsx':
            try:
                xl_Q_liq = pd.ExcelFile(self.data.f_path_Q_liq)
                # self.filepath_textedit2.setPlainText('File received.')
                df2 = xl_Q_liq.parse('Лист1')

                self.data.Q_liq = [float(elem) for elem in df2.Q_liq]
                fmt = ''
                for fmt_ in fmts_date:  # Определение формата даты
                    try:
                        datetime.strptime(str(df2.date[0]).replace(',', '.'), fmt_)
                        fmt = fmt_
                    except:
                        pass
                self.data.date_Q_liq = [datetime.strptime(str(elem).replace(',', '.'), fmt).date() for elem in
                                       df2.date]  # Преобразуем в объект date

                fmt = ''
                for fmt_ in fmts_time:  # Определение формата времени
                    try:
                        datetime.strptime(str(df2.time[0]), fmt_)
                        fmt = fmt_
                    except:
                        pass
                if isinstance(df2.time[0], str):
                    self.data.time_Q_liq = [datetime.strptime(elem, fmt).time() for elem in
                                           df2.time]  # Преобразуем строку в объект time
                else:
                    self.data.time_Q_liq = df2.time

                self.data.datetimes_Q_liq = [datetime.combine(self.data.date_Q_liq[i], self.data.time_Q_liq[i]) for i in
                                       range(len(self.data.date_Q_liq))]  # Преобразуем в объект datetime
                notEmpty = True
            except:
                self.filepath_textedit2.setPlainText('Ошибка! Неверный формат файла или данных в нём. Столбцы должны быть названы: date|time|Q_oil')
                Correct = False
        else:
            self.filepath_textedit2.setPlainText('Extension .xlsx only!')

        # Считываем данные по дебиту нефти
        self.data.f_path_Q_oil = self.filepath_textedit3.toPlainText()
        filename_Q_oil, file_extension_Q_oil = os.path.splitext(self.data.f_path_Q_oil)
        if file_extension_Q_oil == '.xlsx':
            try:
                xl_Q_oil = pd.ExcelFile(self.data.f_path_Q_oil)
                df3 = xl_Q_oil.parse('Лист1')
                self.data.Q_oil = [float(elem) for elem in df3.Q_oil]

                fmt = ''
                for fmt_ in fmts_date:  # Определение формата даты
                    try:
                        datetime.strptime(str(df3.date[0]).replace(',', '.'), fmt_)
                        fmt = fmt_
                    except:
                        pass
                self.data.date_Q_oil = [datetime.strptime(str(elem).replace(',', '.'), fmt).date() for elem in
                                        df3.date]  # Преобразуем строку в объект date

                fmt = ''
                for fmt_ in fmts_time:  # Определение формата времени
                    try:
                        datetime.strptime(str(df3.time[0]), fmt_)
                        fmt = fmt_
                    except:
                        pass
                if isinstance(df3.time[0], str):
                    self.data.time_Q_oil = [datetime.strptime(elem, fmt).time() for elem in
                                            df3.time]  # Преобразуем строку в объект time
                else:
                    self.data.time_Q_oil = df3.time

                self.data.datetimes_Q_oil = [datetime.combine(self.data.date_Q_oil[i], self.data.time_Q_oil[i]) for i in
                                        range(len(self.data.date_Q_oil))]  # Преобразуем в объект datetime
                notEmpty = True
            except:
                self.filepath_textedit3.setPlainText('Ошибка! Неверный формат файла или данных в нём. Столбцы должны быть названы: date|time|Q_oil')
                Correct = False
        else:
            self.filepath_textedit3.setPlainText('Extension .xlsx only!')

        self.update_plot_borders()
        self.update_datetimes_prediction()
        if notEmpty and Correct:
            if self.data.model_prmrs_flag[self.data.well_type] and self.data.common_prmrs_flag:
                self.data.calculated_Q_liq = Generate(self.data)
            self.draw_plot(self.axes, tab=0)
            self.draw_plot(self.axes_2, tab=1)
            self.show_prmrs_mini()

    def initial_plot(self):
        fig, axes = plt.subplots(ncols=1, nrows=2, sharex=True)

        # fmt = dates.DateFormatter('%d.%m.%y %H:%M')

        color = 'red'
        axes[0].set_xlabel('Time')
        axes[0].set_ylabel('Q_жид, м3/сутки', color=color)
        axes[0].set_zorder(1)
        axes[0].tick_params(axis='y', labelcolor=color)
        axes[0].tick_params(axis='x', labelbottom=True)
        # axes[0].xaxis_date()
        # axes[0].xaxis.set_major_formatter(fmt)

        color = 'indigo'
        ax2 = axes[0].twinx()  # instantiate a second self.axes that shares the same x-axis
        # ax2.xaxis_date()
        # ax2.xaxis.set_major_formatter(fmt)
        # ax2.set_zorder(2)
        ax2.set_ylabel('Q_неф, м3/сутки', color=color)  # we already handled the x-label with ax1
        ax2.tick_params(axis='y', labelcolor=color)
        self.ax2.append(ax2)

        axes[1].set_ylabel('P_bh, атм', color='green')
        axes[1].tick_params(axis='y', labelcolor='green')
        # axes[1].xaxis_date()
        # axes[1].xaxis.set_major_formatter(fmt)

        # fig.autofmt_xdate()
        # plt.subplots_adjust(hspace=0.001)
        return fig, axes

    def draw_plot(self, axes=None, tab = 0):
        axes[0].clear()
        axes[1].clear()
        self.ax2[tab].clear()

        color = 'red'
        axes[0].set_xlabel('time')
        axes[0].set_ylabel('Q_жид, м3/сутки', color=color)
        axes[0].set_zorder(1)
        axes[0].tick_params(axis='y', labelcolor=color)
        axes[0].tick_params(axis='x', labelbottom=True)
        axes[0].grid(b=True, which='both', axis='both')

        color = 'indigo'
        # ax2 = axes[0].twinx()  # instantiate a second self.axes that shares the same x-axis
        self.ax2[tab].set_zorder(2)
        self.ax2[tab].set_ylabel('Q_неф, м3/сутки', color=color)  # we already handled the x-label with ax1
        self.ax2[tab].tick_params(axis='y', labelcolor=color)

        axes[1].set_ylabel('P_bh, атм', color='green')
        axes[1].tick_params(axis='y', labelcolor='green')
        axes[1].grid(b=True, which='both', axis='both')

        color = 'red'
        if self.data.datetimes_Q_liq:
            line1 = axes[0].plot(self.data.datetimes_Q_liq, self.data.Q_liq, '-o', color=color, label = 'Q_liq')
            lns = line1
        if self.data.datetimes_prediction:
            line2 = axes[0].plot(self.data.datetimes_prediction, self.data.calculated_Q_liq, '.', linestyle = "--", color='darkred', label = 'Прогноз Q_liq')
            try:
                lns = lns + line2
            except:
                lns = line2

        color = 'indigo'
        if self.data.datetimes_Q_oil:
            line3 = self.ax2[tab].plot(self.data.datetimes_Q_oil, self.data.Q_oil, marker='.', color=color, label = 'Q_oil')
            try:
                lns = lns + line3
            except:
                lns = line3

        # Настройка легенды
        labels = [l.get_label() for l in lns]
        axes[0].legend(lns, labels, loc=0)

        if self.data.datetimes_P_bh:
            axes[1].plot(self.data.datetimes_P_bh, self.data.P_bh, marker='.', color='green', label = 'P_bh')
        axes[1].legend()

        if self.data.datetimes_prediction:  # Возможно лишний if
            # Кусочно-постоянный график
            if self.data.datetimes_prediction_2:
                for i in range(len(self.data.datetimes_prediction_2) + 1):
                    if i == 0:
                        if self.data.datetimes_P_bh:
                            line_x = [self.data.datetimes_P_bh[-1], self.data.datetimes_prediction_2[0]]
                            line_y = [self.data.P_bh[-1], self.data.P_bh[-1]]
                        else:
                            continue
                    elif i == len(self.data.datetimes_prediction_2):
                        line_x = [self.data.datetimes_prediction_2[-1], self.data.datetimes_prediction_2[-1] + timedelta(days=1)]
                        line_y = [self.data.P_bh_prediction[-1], self.data.P_bh_prediction[-1]]
                    else:
                        line_x = [self.data.datetimes_prediction_2[i - 1], self.data.datetimes_prediction_2[i]]
                        line_y = [self.data.P_bh_prediction[i - 1], self.data.P_bh_prediction[i - 1]]
                    axes[1].plot(line_x, line_y, '.', linestyle = "--", color='cyan')

        self.fig.autofmt_xdate()
        self.fig_2.autofmt_xdate()
        self.fig.tight_layout()  # otherwise the right y-label is slightly clipped
        self.fig_2.tight_layout()  # otherwise the right y-label is slightly clipped
        self.fig.canvas.draw()
        self.fig_2.canvas.draw()

    def show_common_prmrs(self):
        self.common_prmrs = Common_parameters(self.data)

    def show_model_prmrs_window(self):
        self.model_prmrs = Model_prmrs(self.data)

    def calculate(self):
        notEmpty = False
        Correct = True
        # Считываем данные по забойному давлению
        self.data.f_path_prediction = self.filepath_textedit_4.toPlainText()
        filename_prediction, file_extension_prediction = os.path.splitext(self.data.f_path_prediction)
        if file_extension_prediction == '.xlsx':
            fmts_date = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%d.%m.%Y']
            fmts_time = ['%H:%M:%S', '%H:%M']
            try:
                xl_prediction = pd.ExcelFile(self.data.f_path_prediction)
                df4 = xl_prediction.parse('Лист1')
                self.data.P_bh_prediction = [float(elem) for elem in df4.P_bh_prediction]

                fmt = ''
                for fmt_ in fmts_date:  # Определение формата времени
                    try:
                        datetime.strptime(str(df4.date[0]), fmt_)
                        fmt = fmt_
                    except:
                        pass
                self.data.date_prediction = [datetime.strptime(str(elem).replace(',', '.'), fmt).date() for elem in
                                        df4.date]  # Преобразуем строку в объект date

                fmt = ''
                for fmt_ in fmts_time:  # Определение формата времени
                    try:
                        datetime.strptime(str(df4.time[0]), fmt_)
                        fmt = fmt_
                    except:
                        pass
                if isinstance(df4.time[0], str):
                    self.data.time_prediction = [datetime.strptime(elem, fmt).time() for elem in
                                                 df4.time]  # Преобразуем строку в объект time
                else:
                    self.data.time_prediction = df4.time

                self.data.datetimes_prediction_2 = [datetime.combine(self.data.date_prediction[i], self.data.time_prediction[i]) for i in
                                             range(len(self.data.date_prediction))]  # Преобразуем в объект datetime
                notEmpty = True
                self.data.delta = float(self.delta_prediction.text())
                self.update_datetimes_prediction()
            except:
                Correct = False
                self.export_btn.setDisabled(True)
                self.filepath_textedit_4.setPlainText('Ошибка! Проверьте входной файл. Столбцы должны быть названы: time|P_bh_prediction')
        else:
            self.filepath_textedit_4.setPlainText('Extension .xlsx only!')
            self.export_btn.setDisabled(True)
        if notEmpty and Correct:
            self.calculate_Q_liq()
            if self.data.datetimes_prediction:
                self.export_btn.setDisabled(False)

    def calculate_Q_liq(self):
        if self.data.model_prmrs_flag[self.data.well_type] and self.data.common_prmrs_flag:
            self.data.start_time = time()
            self.data.calculated_Q_liq = Generate(self.data)
            self.draw_plot(self.axes, tab=0)
            self.draw_plot(self.axes_2, tab=1)
            self.show_prmrs_mini()
            self.data.exec_time.append(time() - self.data.start_time)
        else:
            self.filepath_textedit_4.setPlainText('Ошибка! Введены не все параметры.')

    def update_datetimes_prediction(self):
        self.data.datetimes_prediction = []  # Моменты времени для дебита жидкости по прогнозу
        self.data.delta_dates = []

        if not (self.data.datetimes_P_bh or self.data.datetimes_Q_liq or self.data.datetimes_Q_oil):
            self.data.MIN_x = 0
            self.data.MAX_x = 0
        if self.data.MIN_x and self.data.MAX_x:
            # self.data.datetimes_prediction.append(self.data.MIN_x)
            # self.data.datetimes_prediction_2.append(self.data.MAX_x)
            pass
        else:
            self.data.MIN_x = min(self.data.datetimes_prediction_2)
            self.data.MAX_x = min(self.data.datetimes_prediction_2)

        if len(self.data.time_prediction) > 0:
            if self.data.MAX_x <= min(self.data.datetimes_prediction_2):
                # Моменты времени для забойного давления (с первой вкладки)
                for i in range(1, len(self.data.datetimes_P_bh) + 1):
                    if i == len(self.data.datetimes_P_bh):
                        self.data.delta_dates.append(self.data.datetimes_prediction_2[0] - self.data.datetimes_P_bh[i - 1])
                    else:
                        self.data.delta_dates.append(self.data.datetimes_P_bh[i] - self.data.datetimes_P_bh[i - 1])

                # Моменты времени для забойного давления прогноза (ступенчатый график)
                for i in range(1, len(self.data.datetimes_prediction_2) + 1):
                    if i == len(self.data.datetimes_prediction_2):
                        self.data.delta_dates.append(timedelta(days=1))
                    else:
                        self.data.delta_dates.append(
                            self.data.datetimes_prediction_2[i] - self.data.datetimes_prediction_2[i - 1])

                # Заполнение точек для дебита жидкости по прогнозу (зависит от выбранной дискретности)
                self.data.time_points = []
                sum = self.data.delta
                prediction_period = ((self.data.datetimes_prediction_2[-1] + timedelta(days=1)) - self.data.MIN_x).total_seconds() / 3600     # Продолжительность данных прогноза в часах
                while (sum < prediction_period):
                    self.data.time_points.append(sum)
                    sum += self.data.delta
                self.data.time_points.append(prediction_period)

                # Моменты времени для дебита жидкости по прогнозу
                for i in range(len(self.data.time_points)):
                    point = self.data.MIN_x + timedelta(hours=int(self.data.time_points[i]))
                    self.data.datetimes_prediction.append(point)

                self.statusbar.showMessage('')
            else:
                self.statusbar.showMessage('Ошибка!!! Даты в файле прогнозирования должны идти ПОСЛЕ дат, загруженных из вкладки "Данные" !!!')

    def update_plot_borders(self):
        self.data.MIN_x = 0
        self.data.MAX_x = 0
        list_max = []  # Поиск первого и последнего заданного момента времени (в частности, для адаптации)
        list_min = []
        if self.data.datetimes_Q_liq:
            # list_max.append(max(self.data.datetimes_Q_liq))
            # list_min.append(min(self.data.datetimes_Q_liq))
            pass
        if self.data.datetimes_Q_oil:
            # list_max.append(max(self.data.datetimes_Q_oil))
            # list_min.append(min(self.data.datetimes_Q_oil))
            pass
        if self.data.datetimes_P_bh:
            list_max.append(max(self.data.datetimes_P_bh))
            list_min.append(min(self.data.datetimes_P_bh))
        else:
            if self.data.datetimes_Q_liq:
                list_max.append(max(self.data.datetimes_Q_liq))
                list_min.append(min(self.data.datetimes_Q_liq))
            if self.data.datetimes_Q_oil:
                list_max.append(max(self.data.datetimes_Q_oil))
                list_min.append(min(self.data.datetimes_Q_oil))
        if list_max:
            self.data.MAX_x = max(list_max)
        if list_min:
            self.data.MIN_x = min(list_min)

    def export(self):
        result_directory = os.path.join(f'RESULT ' + str(datetime.now().strftime('%Y-%m-%d-%H.%M.%S')))
        if not os.path.exists(result_directory):
            os.makedirs(result_directory)

        # Сохранение результатов расчётов
        dict = {'Time_moments (абсолютно)':self.data.datetimes_prediction, 'Time moments (относит-но), час': self.data.time_points,
                                                                    'Q_liq рассчитанное':self.data.calculated_Q_liq}
        df_out = pd.DataFrame(dict)
        writer = pd.ExcelWriter(os.path.join(result_directory, 'Results.xlsx'))
        df_out.to_excel(writer, 'Sheet 1')
        writer.save()

        # Сохранение лога данных
        f = open(os.path.join(result_directory, 'parameters_log.txt'), 'w')
        for attr in dir(self.data):
            if not attr.startswith("__"):
                attrib = getattr(self.data, attr)
                try:
                    f.write(str(attr) + ' :\n')
                    for ind, elem in enumerate(attrib):
                        f.write('     ' + str(ind) + ' : ' + str(elem) + '\n')
                except:
                    data_attr = str(attr) + ' : ' + str(attrib) + '\n'
                    f.write(data_attr)
        f.close()
        self.statusbar.showMessage('Результаты сохранены в папку ' + 'RESULT ' + str(datetime.now().strftime('%Y-%m-%d-%H.%M.%S')))

    def show_prmrs_mini(self):
        self.prmrs_mini.show()
        self.prmrs_mini_2.show()
        output = ''
        output += 'Тип скважины : ' + str(self.data.well_names[self.data.well_type]) + '\n'
        output += 'Форма границы : ' + str(self.data.reservoir_form_names[self.data.comboBox_ind]) + '\n'
        output += 'Тип границы : ' + str(self.data.bound_type_names[self.data.bound_type]) + '\n'

        # Общие параметры
        output += 'Пористость : ' + str(self.data.porosity) + '\n'
        output += 'Эфф. толщина пласта, м : ' + str(self.data.h_eff) + '\n'
        output += 'Радиус скв., м : ' + str(self.data.rc) + '\n'
        output += 'Вязкость, сП : ' + str(self.data.mu) + '\n'
        output += 'Общая сжимаемость, 1/атм : ' + str(self.data.C_t) + '\n'
        output += 'Объем. коэфф-т : ' + str(self.data.B_liq) + '\n'

        if self.data.well_type >= 0:
            output += 'Проницаемость, мД : ' + str(self.data.K) + '\n'
            output += 'Отн. верт. к гориз. прон  (kv/kh), 1/атм : ' + str(self.data.kv_kh) + '\n'
            output += 'Начальное пластовое давление, атм : ' + str(self.data.P_initial) + '\n'
            output += 'Скин-фактор : ' + str(self.data.skin) + '\n'
        if self.data.well_type >= 1:
            output += 'Длина горизонт. ствола, м: ' + str(self.data.horiz_length) + '\n'
        if self.data.well_type >= 2:
            output += 'Полудлина трещины, м : ' + str(self.data.frac_half_length) + '\n'
            output += 'Проводимость трещины, мД * м : ' + str(self.data.frac_conductivity) + '\n'
        if self.data.well_type >= 3:
            output += 'Количество ГРП : ' + str(self.data.frac_num) + '\n'
            output += 'Направление трещин : ' + str(self.data.frac_dir_names[self.data.frac_dir]) + '\n'
            output += 'Вертикальное положение (в долях от мощности), доли : ' + str(self.data.vertical_position) + '\n'
            output += 'Величина вскрытия пласта (в долях от мощности), доли : ' + str(self.data.vskritie_plasta) + '\n'
        self.prmrs_mini.setText(output)
        self.prmrs_mini_2.setText(output)


def main():
    app = QApplication(sys.argv)
    main_ = MainWindow()
    main_.show()
    sys.exit(app.exec_())

main()
