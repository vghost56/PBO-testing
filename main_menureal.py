import dftr_brg,dftr_gdgrg,dftr_pegawai,dftr_pinjamadmin
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdw_mainmenu(object):
    def setupUi(self, wdw_mainmenu):
        wdw_mainmenu.setObjectName("wdw_mainmenu")
        wdw_mainmenu.resize(412, 272)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdw_mainmenu.sizePolicy().hasHeightForWidth())
        wdw_mainmenu.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(wdw_mainmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_daftarbrg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_daftarbrg.setGeometry(QtCore.QRect(20, 120, 141, 71))
        self.btn_daftarbrg.setObjectName("btn_daftarbrg")
        self.btn_pnjmbrg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pnjmbrg.setGeometry(QtCore.QRect(20, 20, 141, 71))
        self.btn_pnjmbrg.setObjectName("btn_pnjmbrg")
        self.btn_dftrakun = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dftrakun.setGeometry(QtCore.QRect(250, 120, 141, 71))
        self.btn_dftrakun.setObjectName("btn_dftrakun")
        self.btn_dftrgdg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dftrgdg.setGeometry(QtCore.QRect(250, 20, 141, 71))
        self.btn_dftrgdg.setObjectName("btn_dftrgdg")
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(320, 210, 71, 31))
        self.btn_logout.setObjectName("btn_logout")
        wdw_mainmenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wdw_mainmenu)
        self.statusbar.setObjectName("statusbar")
        wdw_mainmenu.setStatusBar(self.statusbar)

        #################################START#################################
        self.btn_dftrgdg.pressed.connect(lambda: self.gotodftrged(wdw_mainmenu))
        self.btn_daftarbrg.pressed.connect(lambda: self.gotodftrbrg(wdw_mainmenu))
        self.btn_dftrakun.pressed.connect(lambda: self.gotodftrpeg(wdw_mainmenu))
        self.btn_pnjmbrg.pressed.connect(lambda: self.gotodftrpem(wdw_mainmenu))
        #################################ENDS##################################

        self.retranslateUi(wdw_mainmenu)
        QtCore.QMetaObject.connectSlotsByName(wdw_mainmenu)

    def retranslateUi(self, wdw_mainmenu):
        _translate = QtCore.QCoreApplication.translate
        wdw_mainmenu.setWindowTitle(_translate("wdw_mainmenu", "Main Menu"))
        self.btn_daftarbrg.setText(_translate("wdw_mainmenu", "Daftar Barang"))
        self.btn_pnjmbrg.setText(_translate("wdw_mainmenu", "Daftar Peminjaman"))
        self.btn_dftrakun.setText(_translate("wdw_mainmenu", "Daftar Pegawai/Akun"))
        self.btn_dftrgdg.setText(_translate("wdw_mainmenu", "Daftar Gedung/Ruangan"))
        self.btn_logout.setText(_translate("wdw_mainmenu", "Logout"))

    def getMeAName(self,username):
        self.username=username
    
    def gotodftrbrg(self,wdw_mainmenu):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = dftr_brg.Ui_wdw_gdgrg()
        
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        wdw_mainmenu.hide()
        self.ui.btn_back.clicked.connect(lambda: self.reapp(wdw_mainmenu))

    def gotodftrged(self,wdw_mainmenu):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = dftr_gdgrg.Ui_wdw_gdgrg()
        
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        wdw_mainmenu.hide()
        self.ui.btn_back.clicked.connect(lambda: self.reapp(wdw_mainmenu))

    def gotodftrpeg(self,wdw_mainmenu):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = dftr_pegawai.Ui_wdw_daftarpegakun()
        
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        wdw_mainmenu.hide()
        self.ui.btn_back.clicked.connect(lambda: self.reapp(wdw_mainmenu))

    def gotodftrpem(self,wdw_mainmenu):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = dftr_pinjamadmin.Ui_wdw_tambahbarang()
        
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        wdw_mainmenu.hide()
        self.ui.btn_back.clicked.connect(lambda: self.reapp(wdw_mainmenu))

    def reapp(self,wdw_mainmenu):
        self.Menu.hide()
        wdw_mainmenu.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdw_mainmenu = QtWidgets.QMainWindow()
    ui = Ui_wdw_mainmenu()
    ui.setupUi(wdw_mainmenu)
    wdw_mainmenu.show()
    sys.exit(app.exec_())
