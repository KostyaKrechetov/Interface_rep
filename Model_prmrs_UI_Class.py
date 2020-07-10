from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from UI.Model_prmrs_UI import Ui_Model_prmrs

class Model_prmrs(QDialog, Ui_Model_prmrs):
    def __init__(self, data):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.error_label.hide()
        self.data_ = data
        # Индексы строк таблицы, отображаемые для выбранного типа скважины
        self.vertical_well_rows = [i for i in range(6)]
        self.horizontal_well_rows = [i for i in range(8)]
        self.horizontal_well_rows.append(14)
        self.horizontal_well_rows.append(15)        # Параметр "Вертикальное положение (в долях от мощности)"
        self.frac_rows = [i for i in range(11) if i not in [6, 7]]
        self.multifrac_well_rows = [i for i in range(17)]
        self.rows = [self.vertical_well_rows, self.horizontal_well_rows, self.frac_rows, self.multifrac_well_rows]

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.comboBox.currentIndexChanged.connect(self.reservoir_form_changed)
        self.comboBox_2.currentIndexChanged.connect(self.boundary_type_changed_rect)
        self.comboBox_3.currentIndexChanged.connect(self.boundary_type_changed_circle)
        self.well_type_combo.currentIndexChanged.connect(self.well_type_changed)

        # ----- ГЕОМЕТРИЯ ----
        self.circle_radius.setText(str(data.circle_radius))
        self.W_E_length.setText(str(data.W_E_length))
        self.N_S_length.setText(str(data.N_S_length))
        self.width_of_center.setText(str(data.width_of_center))
        self.length_of_center.setText(str(data.length_of_center))

        self.reservoir_form_changed(self.data_.comboBox_ind)    # Отображение нужных параметров в зависимости от формы границ
        self.well_type_changed(self.data_.well_type)    # Отображение нужных параметров в зависимости от типа скважины
        self.draw_table()
        self.frac_dir_changed(self.data_.frac_dir)
        self.boundary_type_changed_rect(self.data_.bound_type_rect)
        self.boundary_type_changed_circle(self.data_.bound_type_circle)

    def draw_table(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(17)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(2, 100)
        self.column_names = ['Параметр', 'Значение', 'Ед. изм.']
        self.tableWidget.setHorizontalHeaderLabels(self.column_names)
        self.tableWidget.verticalHeader().hide()

        span_cells_indexes = [0, 4, 6, 8, 11, 14]   # Индексы строк, в которых будут объединены столбцы
        rows_columns_names = [
            ['Пласт', '', ''],
            ['Проницаемость ', '', 'мД'],
            ['Отн. верт. к гориз. прон  (kv/kh)', '', ''],
            ['Начальное пластовое давление', '', 'атм'],
            ['Скважина', '', ''],
            ['Скин-фактор', '', ''],
            ['Горизонтальная скважина', '', ''],
            ['Длина горизонт. ствола', '', 'м'],
            ['Трещина', '', ''],
            ['Полудлина трещины', '', 'м'],
            ['Проводимость трещины', '', 'мД * м'],
            ['МГРП', '', ''],
            ['Количество трещин', '', ''],
            ['Вид трещин', '', ''],
            ['Параметры по оси z', '', ''],
            ['Вертикальное положение (в долях от мощности)', '', 'доли'],
            ['Величина вскрытия пласта (в долях от мощности)', '', 'доли'],
        ]
        # Заполнение названий
        for i in range(self.tableWidget.rowCount()):
            for j in range(0, 3, 2):
                item = QTableWidgetItem()
                item.setText(rows_columns_names[i][j])
                item.font()
                item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)

        # Объединение ячеек
        font = QFont()
        font.setBold(True)
        for ind in span_cells_indexes:
            self.tableWidget.setSpan(ind, 0, 1, 3)
            self.tableWidget.item(ind, 0).setFont(font)

        regExp = QtCore.QRegExp(
            "[-]{0,1}\d{0,}\.\d{0,}")  # Валидатор на ввод только чисел с точкой
        validator = QtGui.QRegExpValidator(regExp)

        for i in range(self.tableWidget.rowCount()):
            if i not in span_cells_indexes:
                if i != 13:  # на 13 позиции будет ComboBox выбора направления трещины
                    item = QtWidgets.QLineEdit()
                    item.setValidator(validator)
                    self.tableWidget.setCellWidget(i, 1, item)
                else:
                    self.frac_dir = QtWidgets.QComboBox()
                    _translate = QtCore.QCoreApplication.translate
                    self.frac_dir.addItem("")
                    self.frac_dir.addItem("")
                    self.frac_dir.setItemText(0, _translate("Model_prmrs", "Вдоль ствола"))
                    self.frac_dir.setItemText(1, _translate("Model_prmrs", "Поперек ствола"))
                    self.frac_dir.currentIndexChanged.connect(self.frac_dir_changed)
                    self.tableWidget.setCellWidget(i, 1, self.frac_dir)

        self.tableWidget.cellWidget(1, 1).setText(str(self.data_.K))
        self.tableWidget.cellWidget(2, 1).setText(str(self.data_.kv_kh))
        self.tableWidget.cellWidget(3, 1).setText(str(self.data_.P_initial))
        self.tableWidget.cellWidget(5, 1).setText(str(self.data_.skin))
        self.tableWidget.cellWidget(7, 1).setText(str(self.data_.horiz_length))
        self.tableWidget.cellWidget(9, 1).setText(str(self.data_.frac_half_length))
        self.tableWidget.cellWidget(10, 1).setText(str(self.data_.frac_conductivity))
        self.tableWidget.cellWidget(12, 1).setText(str(self.data_.frac_num))
        self.tableWidget.cellWidget(15, 1).setText(str(self.data_.vertical_position))
        self.tableWidget.cellWidget(16, 1).setText(str(self.data_.vskritie_plasta))

        for i in range(self.tableWidget.rowCount()):
            if i not in self.rows[self.data_.well_type]:
                self.tableWidget.hideRow(i)

    def accept(self):
        # --- ГЕОМЕТРИЯ ---
        GeomFlag = False
        try:
            if self.comboBox.currentIndex() == 0:
                self.data_.W_E_length = float(self.W_E_length.text())
                self.data_.N_S_length = float(self.N_S_length.text())
                self.data_.width_of_center = float(self.width_of_center.text())
                self.data_.length_of_center = float(self.length_of_center.text())
                GeomFlag = True
            elif self.comboBox.currentIndex() == 1:
                self.data_.circle_radius = float(self.circle_radius.text())
                GeomFlag = True
        except:
            GeomFlag = False
            self.error_label.show()

        # Проверка поблочно на корректность данных для выбранного типа скважины
        if self.well_type_combo.currentIndex() == 0:
            try:
                self.data_.K = float(self.tableWidget.cellWidget(1,1).text())
                self.data_.kv_kh = float(self.tableWidget.cellWidget(2,1).text())
                self.data_.P_initial = float(self.tableWidget.cellWidget(3,1).text())
                self.data_.skin = float(self.tableWidget.cellWidget(5,1).text())
                self.data_.model_prmrs_flag[0] = True
            except:
                self.data_.model_prmrs_flag[0] = False
                self.error_label.show()

        elif self.well_type_combo.currentIndex() == 1:
            try:
                self.data_.K = float(self.tableWidget.cellWidget(1, 1).text())
                self.data_.kv_kh = float(self.tableWidget.cellWidget(2, 1).text())
                self.data_.P_initial = float(self.tableWidget.cellWidget(3, 1).text())
                self.data_.skin = float(self.tableWidget.cellWidget(5, 1).text())
                self.data_.horiz_length = float(self.tableWidget.cellWidget(7,1).text())
                self.data_.vertical_position = float(self.tableWidget.cellWidget(15,1).text())
                self.data_.model_prmrs_flag[1] = True
            except:
                self.data_.model_prmrs_flag[1] = False
                self.error_label.show()

        elif self.well_type_combo.currentIndex() == 2:
            try:
                self.data_.K = float(self.tableWidget.cellWidget(1, 1).text())
                self.data_.kv_kh = float(self.tableWidget.cellWidget(2, 1).text())
                self.data_.P_initial = float(self.tableWidget.cellWidget(3, 1).text())
                self.data_.skin = float(self.tableWidget.cellWidget(5, 1).text())
                self.data_.frac_half_length = float(self.tableWidget.cellWidget(9,1).text())
                self.data_.frac_conductivity = float(self.tableWidget.cellWidget(10,1).text())
                self.data_.model_prmrs_flag[2] = True
            except:
                self.data_.model_prmrs_flag[2] = False
                self.error_label.show()

        elif self.well_type_combo.currentIndex() == 3:
            try:
                self.data_.K = float(self.tableWidget.cellWidget(1, 1).text())
                self.data_.kv_kh = float(self.tableWidget.cellWidget(2, 1).text())
                self.data_.P_initial = float(self.tableWidget.cellWidget(3, 1).text())
                self.data_.skin = float(self.tableWidget.cellWidget(5, 1).text())
                self.data_.horiz_length = float(self.tableWidget.cellWidget(7, 1).text())
                self.data_.frac_half_length = float(self.tableWidget.cellWidget(9, 1).text())
                self.data_.frac_conductivity = float(self.tableWidget.cellWidget(10, 1).text())
                self.data_.frac_num = int(self.tableWidget.cellWidget(12,1).text())
                self.data_.frac_dir = self.frac_dir.currentIndex()
                self.data_.vertical_position = float(self.tableWidget.cellWidget(15,1).text())
                self.data_.vskritie_plasta = float(self.tableWidget.cellWidget(16,1).text())
                self.data_.model_prmrs_flag[3] = True
            except:
                self.data_.model_prmrs_flag[3] = False
                self.error_label.show()

        if self.data_.model_prmrs_flag[self.well_type_combo.currentIndex()] == True and GeomFlag:
            self.error_label.hide()
            self.close()

    def reservoir_form_changed(self, ind):
        self.data_.comboBox_ind = ind
        self.comboBox.setCurrentIndex(ind)
        if ind == 0:
            self.widget_2.hide()
            self.verticalWidget_3.show()
            self.comboBox_2.show()
            self.comboBox_3.hide()
        elif ind == 1:
            self.widget_2.show()
            self.verticalWidget_3.hide()
            self.comboBox_2.hide()
            self.comboBox_3.show()

    def well_type_changed(self, ind):
        self.data_.well_type = ind
        self.well_type_combo.setCurrentIndex(ind)
        for i in range(self.tableWidget.rowCount()):
            if i not in self.rows[self.data_.well_type]:
                self.tableWidget.hideRow(i)
            else:
                self.tableWidget.showRow(i)

    def frac_dir_changed(self, ind):
        self.data_.frac_dir = ind
        self.frac_dir.setCurrentIndex(ind)

    def boundary_type_changed_rect(self, ind):
        self.data_.bound_type_rect = ind
        self.comboBox_2.setCurrentIndex(ind)
        self.data_.bound_type = ind

    def boundary_type_changed_circle(self, ind):
        self.data_.bound_type_circle = ind
        self.comboBox_3.setCurrentIndex(ind)
        self.data_.bound_type = ind

