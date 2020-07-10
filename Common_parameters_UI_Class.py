from PyQt5.QtWidgets import QDialog
from UI.Common_parameters_UI_v3 import Ui_Common_prmrs


class Common_parameters(QDialog, Ui_Common_prmrs):
    def __init__(self, data):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()
        self.error_label.hide()

        self.data_ = data

        self.porosity.setText(str(data.porosity))
        self.h_eff.setText(str(data.h_eff))
        self.rc.setText(str(data.rc))
        self.mu.setText(str(data.mu))
        self.C_t.setText(str(data.C_t))
        self.B_liq.setText(str(data.B_liq))

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        try:
            self.data_.porosity = float(self.porosity.text())
            self.data_.h_eff = float(self.h_eff.text())
            self.data_.rc = float(self.rc.text())
            self.data_.mu = float(self.mu.text())
            self.data_.C_t = float(self.C_t.text())
            self.data_.B_liq = float(self.B_liq.text())
            self.data_.common_prmrs_flag = True
            self.error_label.hide()
            self.close()
        except:
            self.error_label.show()
            # self.close()


