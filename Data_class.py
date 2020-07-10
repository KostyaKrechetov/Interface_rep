# Класс хранения данных
class Data():
    def __init__(self):
        self.well_names = ['Вертикальная скважина', "Горизонтальная скважина", "ГРП", "ГС с МГРП"]
        self.reservoir_form_names = ['Прямоугольная']
        self.bound_type_names = ["Замкнутая", "Пост. давление целиком (сссс)", "Пост. давление Север и Юг (cncn)", "Пост. давление Запад и Восток (ncnc)"]
        self.frac_dir_names = ['Вдоль ствола', 'Поперек ствола']
        self.well_type = 0                 # Индекс типа скважины: 0 - вертик., 1 - гориз., 2 - ГРП, 3 - МГРП
        self.model_prmrs_flag = [False for i in range(4)]    # Флаг проверки, введены ли параметры модели при выборе i-го типа скважины
                                                             #   0 - вертик. скв., 1 - горизонт. скв, 2 - ГРП, 3 - МГРП
        self.common_prmrs_flag = False     # Флаг проверки, введены ли "общие параметры"
        self.comboBox_ind = 0              # Индекс формы границ: 0 - прямоугольная, 1 - круглая
        self.bound_type_rect = 0           # Индекс типа границ для прямоугольника: 0 - Замкн, 1 - пост. давление (сссс), 2 - пост. давление (cncn), 3 - пост. давление (ncnc)
        self.bound_type_circle = 0         # Индекс типа границ для окружности: 0 - Замкн, 1 - Пост. давл.
        self.bound_type = 0                # Итоговый тип границ (равен одному из вышеуказанных) (От 0 до 3)

        self.datetimes_P_bh = []
        self.datetimes_Q_liq = []
        self.datetimes_Q_oil = []
        self.datetimes_prediction = []
        self.datetimes_prediction_2 = []
        self.time_prediction = []
        self.delta_dates = []
        self.P_bh = []

        # Общие параметры
        self.porosity = '0.15'  # Пористость
        self.h_eff = '5.96'     # Эфф. толщина пласта, м
        self.rc = '0.108'        # Радиус скв., м
        self.mu = '0.338932567825029'        # Вязкость, сП
        self.C_t = '0.000047936014476'       # Общая сжимаемость, 1/атм
        self.B_liq = '1.02787536'     # Объем. коэфф-т

        # Параметры модели --- геометрия
        self.circle_radius = ''     # Радиус окружности (если форма залежи - окр-ть), м
        self.W_E_length = '1700'        # Длина прямоугольника, м
        self.N_S_length = '2300'        # Ширина прямоугольника, м
        self.width_of_center = '0.5'   # Доля от ширины до центра, доли
        self.length_of_center = '0.5'  # Доля от длины до центра, доли

        # Пласт
        self.K = '0.67'                 # Проницаемость, мД
        self.kv_kh = '1'             # Отн. верт. к гориз. прон  (kv/kh), 1/атм
        self.P_initial = '250'         # Начальное пластовое давление, атм
        # Устье скважины
        self.skin = '0'              # Скин-фактор
        # Горизонтальная скв.
        self.horiz_length = '500'      # Длина горизонт. ствола, м
        # Трещина
        self.frac_half_length = 94.28  # Полудлина трещины, м
        # self.frac_k = '350'            # Проницаемость трещины, Д
        # self.frac_width = '4'        # Ширина трещины, мм
        self.frac_conductivity = '10000'        # Проводимость трещины, мД * м
        # мгрп
        self.frac_num = '7'          # Количество ГРП
        self.frac_dir = 0           # 0 - 'Вдоль ствола', 1 - 'Поперек ствола'
        # Геометрия по оси z
        self.vertical_position = '0.5' # Вертикальное положение (в долях от мощности), доли
        self.vskritie_plasta = '1'   # Величина вскрытия пласта (в долях от мощности), доли


        # Расчёт
        self.regime_flag = 1        # 0 - постоянное заб. давл., 1 - кусочно-постоянное, 2 - кусочно-линейное
        self.time_points = [day * 24 for day in range(1, 31)]  # список для t (ОН ПЕРЕЗАПИСЫВАЕТСЯ!!!!)
        self.delta = 24
        self.exec_time = []
        # self.data.time_points = [1]
        # from math import exp
        # for i in range(1, 31):
        #     self.data.time_points.append(self.data.time_points[i - 1] * exp(0.04545))


