from UI.Parameters_QDialog_UI_v2 import Ui_Dialog

from PyQt5.QtWidgets import QDialog


class Parameters(QDialog, Ui_Dialog):
    def __init__(self, data):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()
        self.data_ = data

        self.buttonBox.accepted.connect(self.accept_)
        self.buttonBox.rejected.connect(self.reject)
        self.comboBox.currentIndexChanged.connect(self.redraw)

        self.rc.setText(str(data.rc))
        self.length.setText(str(data.length))
        self.B_liq.setText(str(data.B_liq))
        self.mu.setText(str(data.mu))
        self.K.setText(str(data.K))
        self.kv_kh.setText(str(data.kv_kh))
        self.C_t.setText(str(data.C_t))
        self.phi.setText(str(data.phi))
        self.textEdit_15.setText(str(data.textEdit_15))
        self.P_initial.setText(str(data.P_initial))
        self.W_E_length.setText(str(data.W_E_length))
        self.N_S_length.setText(str(data.N_S_length))
        self.bound_1.setText(str(data.bound_1))
        self.bound_2.setText(str(data.bound_2))
        self.h_eff.setText(str(data.h_eff))
        self.vertical_position.setText(str(data.vertical_position))
        self.vskritie_plasta.setText(str(data.vskritie_plasta))
        self.circle_radius.setText(str(data.circle_radius))

        self.redraw(self.data_.comboBox_ind)

    def accept_(self):
        self.data_.rc = float(self.rc.text())
        self.data_.length = float(self.length.text())
        self.data_.B_liq = float(self.B_liq.text())
        self.data_.mu = float(self.mu.text())
        self.data_.K = float(self.K.text())
        self.data_.kv_kh = float(self.kv_kh.text())
        self.data_.C_t = float(self.C_t.text())
        self.data_.phi = float(self.phi.text())
        self.data_.textEdit_15 = float(self.textEdit_15.text())
        self.data_.P_initial = float(self.P_initial.text())
        self.data_.circle_radius = float(self.circle_radius.text())
        self.data_.W_E_length = float(self.W_E_length.text())
        self.data_.N_S_length = float(self.N_S_length.text())
        self.data_.bound_1 = float(self.bound_1.text())
        self.data_.bound_2 = float(self.bound_2.text())
        self.data_.h_eff = float(self.h_eff.text())
        self.data_.vertical_position = float(self.vertical_position.text())
        self.data_.vskritie_plasta = float(self.vskritie_plasta.text())
        self.close()

    def redraw(self, ind):
        self.data_.comboBox_ind = ind
        self.comboBox.setCurrentIndex(ind)
        if ind == 0:
            self.verticalWidget_2.hide()
            self.verticalWidget_3.show()
            self.comboBox_2.show()
            self.comboBox_3.hide()
        elif ind == 1:
            self.verticalWidget_2.show()
            self.verticalWidget_3.hide()
            self.comboBox_2.hide()
            self.comboBox_3.show()