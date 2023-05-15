from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="db_pbo"
)
mycursor = mydb.cursor()

class Ui_wdw_gdgrg(object):
    def setupUi(self, wdw_gdgrg):
        wdw_gdgrg.setObjectName("wdw_gdgrg")
        wdw_gdgrg.resize(745, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdw_gdgrg.sizePolicy().hasHeightForWidth())
        wdw_gdgrg.setSizePolicy(sizePolicy)
        wdw_gdgrg.setMinimumSize(QtCore.QSize(745, 510))
        wdw_gdgrg.setMaximumSize(QtCore.QSize(745, 510))
        self.centralwidget = QtWidgets.QWidget(wdw_gdgrg)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.btn_back.setObjectName("btn_back")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 231, 171))
        self.groupBox.setObjectName("groupBox")
        self.lbl_kodgdg = QtWidgets.QLabel(self.groupBox)
        self.lbl_kodgdg.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.lbl_kodgdg.setObjectName("lbl_kodgdg")
        self.inp_namgdg = QtWidgets.QLineEdit(self.groupBox)
        self.inp_namgdg.setGeometry(QtCore.QRect(10, 40, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_namgdg.sizePolicy().hasHeightForWidth())
        self.inp_namgdg.setSizePolicy(sizePolicy)
        self.inp_namgdg.setText("")
        self.inp_namgdg.setObjectName("inp_namgdg")
        self.inp_kodgdg = QtWidgets.QLineEdit(self.groupBox)
        self.inp_kodgdg.setGeometry(QtCore.QRect(10, 90, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_kodgdg.sizePolicy().hasHeightForWidth())
        self.inp_kodgdg.setSizePolicy(sizePolicy)
        self.inp_kodgdg.setText("")
        self.inp_kodgdg.setObjectName("inp_kodgdg")
        self.lbl_namgdg = QtWidgets.QLabel(self.groupBox)
        self.lbl_namgdg.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.lbl_namgdg.setObjectName("lbl_namgdg")
        self.btn_submit = QtWidgets.QPushButton(self.groupBox)
        self.btn_submit.setGeometry(QtCore.QRect(10, 140, 211, 23))
        self.btn_submit.setObjectName("btn_submit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 240, 231, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lbl_kodrgn = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_kodrgn.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.lbl_kodrgn.setObjectName("lbl_kodrgn")
        self.lbl_kodgdg_2 = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_kodgdg_2.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.lbl_kodgdg_2.setObjectName("lbl_kodgdg_2")
        self.inp_kodrgn = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_kodrgn.setGeometry(QtCore.QRect(10, 90, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_kodrgn.sizePolicy().hasHeightForWidth())
        self.inp_kodrgn.setSizePolicy(sizePolicy)
        self.inp_kodrgn.setText("")
        self.inp_kodrgn.setObjectName("inp_kodrgn")
        self.lbl_pjrgn = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_pjrgn.setGeometry(QtCore.QRect(10, 120, 171, 16))
        self.lbl_pjrgn.setObjectName("lbl_pjrgn")
        self.inp_pjrgn = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_pjrgn.setGeometry(QtCore.QRect(10, 140, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_pjrgn.sizePolicy().hasHeightForWidth())
        self.inp_pjrgn.setSizePolicy(sizePolicy)
        self.inp_pjrgn.setText("")
        self.inp_pjrgn.setClearButtonEnabled(False)
        self.inp_pjrgn.setObjectName("inp_pjrgn")
        self.btn_submit_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_submit_2.setGeometry(QtCore.QRect(10, 200, 211, 23))
        self.btn_submit_2.setObjectName("btn_submit_2")
        self.inp_kombged = QtWidgets.QComboBox(self.groupBox_2)
        self.inp_kombged.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.inp_kombged.setObjectName("inp_kombged")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 20, 481, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_gdng = QtWidgets.QWidget()
        self.tab_gdng.setObjectName("tab_gdng")
        self.tableWidget1 = QtWidgets.QTableWidget(self.tab_gdng)
        self.tableWidget1.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.tableWidget1.setShowGrid(True)
        self.tableWidget1.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget1.setRowCount(20)
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setObjectName("tableWidget1")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        self.btn_del = QtWidgets.QPushButton(self.tab_gdng)
        self.btn_del.setGeometry(QtCore.QRect(410, 410, 51, 21))
        self.btn_del.setObjectName("btn_del")
        self.inp_rowdel = QtWidgets.QComboBox(self.tab_gdng)
        self.inp_rowdel.setGeometry(QtCore.QRect(330, 410, 69, 21))
        self.inp_rowdel.setObjectName("inp_rowdel")
        self.tabWidget.addTab(self.tab_gdng, "")
        self.tab_ruang = QtWidgets.QWidget()
        self.tab_ruang.setObjectName("tab_ruang")
        self.btn_del_2 = QtWidgets.QPushButton(self.tab_ruang)
        self.btn_del_2.setGeometry(QtCore.QRect(410, 410, 51, 21))
        self.btn_del_2.setObjectName("btn_del_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_ruang)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.inp_rowdel_2 = QtWidgets.QComboBox(self.tab_ruang)
        self.inp_rowdel_2.setGeometry(QtCore.QRect(330, 410, 69, 21))
        self.inp_rowdel_2.setObjectName("inp_rowdel_2")
        self.tabWidget.addTab(self.tab_ruang, "")
        wdw_gdgrg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wdw_gdgrg)
        self.statusbar.setObjectName("statusbar")
        wdw_gdgrg.setStatusBar(self.statusbar)
        self.connectinggdg()
        self.connectingrg()
        self.refresh()
        #################################START#################################
        self.btn_submit.pressed.connect(self.submitgdg)
        self.btn_submit_2.pressed.connect(self.submitrgn)
        #################################ENDS##################################

        self.retranslateUi(wdw_gdgrg)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdw_gdgrg)

    def retranslateUi(self, wdw_gdgrg):
        _translate = QtCore.QCoreApplication.translate
        wdw_gdgrg.setWindowTitle(_translate("wdw_gdgrg", "Daftar Gedung & Ruangan"))
        self.btn_back.setText(_translate("wdw_gdgrg", "Kembali"))
        self.groupBox.setTitle(_translate("wdw_gdgrg", "Daftar Gedung"))
        self.lbl_kodgdg.setText(_translate("wdw_gdgrg", "Kode Gedung"))
        self.inp_namgdg.setPlaceholderText(_translate("wdw_gdgrg", "ex. Gedung Z"))
        self.inp_kodgdg.setPlaceholderText(_translate("wdw_gdgrg", "ex. G-Z"))
        self.lbl_namgdg.setText(_translate("wdw_gdgrg", "Nama Gedung"))
        self.btn_submit.setText(_translate("wdw_gdgrg", "Submit"))
        self.groupBox_2.setTitle(_translate("wdw_gdgrg", "Daftar Ruangan"))
        self.lbl_kodrgn.setText(_translate("wdw_gdgrg", "Kode Ruangan"))
        self.lbl_kodgdg_2.setText(_translate("wdw_gdgrg", "Kode Gedung"))
        self.inp_kodrgn.setPlaceholderText(_translate("wdw_gdgrg", "ex. Z01"))
        self.lbl_pjrgn.setText(_translate("wdw_gdgrg", "Penanggungjawab Ruangan"))
        self.inp_pjrgn.setPlaceholderText(_translate("wdw_gdgrg", "ex. Panjul Richard Salvador"))
        self.btn_submit_2.setText(_translate("wdw_gdgrg", "Submit"))
        self.tableWidget1.setSortingEnabled(True)
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("wdw_gdgrg", "Nama Gedung"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("wdw_gdgrg", "ID Gedung"))
        self.btn_del.setText(_translate("wdw_gdgrg", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gdng), _translate("wdw_gdgrg", "Daftar Gedung"))
        self.btn_del_2.setText(_translate("wdw_gdgrg", "Delete"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("wdw_gdgrg", "ID Gedung"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("wdw_gdgrg", "No. Ruangan"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("wdw_gdgrg", "Pj. Ruangan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ruang), _translate("wdw_gdgrg", "Daftar Ruangan"))

    def connectinggdg(self):
        order = "SELECT * FROM gedung"
        mycursor.execute(order)
        data = mycursor.fetchall()
        if not data:
            self.tableWidget1.setColumnCount(1)
            self.tableWidget1.setRowCount(1)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setVerticalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setItem(0, 0, item)
            item = self.tableWidget1.item(0, 0)
            item.setText("NULL")
        else:
            self.tableWidget1.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget1.insertRow(row_number)
                for column_number, ndata in enumerate(row_data):
                    self.tableWidget1.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(ndata)))

    def connectingrg(self):
        order = "SELECT * FROM ruangan"
        mycursor.execute(order)
        data = mycursor.fetchall()
        if not data:
            self.tableWidget_2.setColumnCount(1)
            self.tableWidget_2.setRowCount(1)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(0, 0, item)
            item = self.tableWidget_2.item(0, 0)
            item.setText("NULL")
        else:
            self.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget_2.insertRow(row_number)
                for column_number, ndata in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(ndata)))

    def combo(self):
        order = "SELECT kode_gedung FROM gedung"
        mycursor.execute(order)
        data = mycursor.fetchall()
        mydb.commit()
        return data

    def refresh(self):
        self.inp_kombged.clear()
        self.gedung = []
        self.gedung1 = self.combo()
        for i in self.gedung1:
            self.gedung.append(i[0])
        self.inp_kombged.addItems(self.gedung)

    
    def submitgdg(self):
        namgdg = self.inp_namgdg.text()
        kodgdg = self.inp_kodgdg.text()
        
        try:
            sql_insert_blob_query = """ INSERT INTO gedung
                            (nama_gedung, kode_gedung) VALUES (%s,%s)"""
            inputdat = (namgdg,kodgdg)
            result = mycursor.execute(sql_insert_blob_query,inputdat)
            mydb.commit()
        except mysql.connector.Error as error:
            self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
            masuk = 0
        self.connectinggdg()
        self.refresh()

    def submitrgn(self):
        kombgdg = self.inp_kombged.currentText()
        kodrgn = self.inp_kodrgn.text()
        pjrgn = self.inp_pjrgn.text()

        try:
            sql_insert_blob_query = """ INSERT INTO ruangan
                            (kode_gedung, no_ruangan, pj_ruangan) VALUES (%s,%s,%s)"""
            inputdat = (kombgdg,kodrgn,pjrgn)
            result = mycursor.execute(sql_insert_blob_query,inputdat)
            mydb.commit()
        except mysql.connector.Error as error:
            self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
            masuk = 0
        self.connectingrg()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdw_gdgrg = QtWidgets.QMainWindow()
    ui = Ui_wdw_gdgrg()
    ui.setupUi(wdw_gdgrg)
    wdw_gdgrg.show()
    sys.exit(app.exec_())
