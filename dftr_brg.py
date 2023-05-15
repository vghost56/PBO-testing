from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="db_pbo"
)
mycursor = mydb.cursor()

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

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
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_kodbrg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kodbrg.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.lbl_kodbrg.setObjectName("lbl_kodbrg")
        self.lbl_nambrg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nambrg.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.lbl_nambrg.setObjectName("lbl_nambrg")
        self.lbl_stokttl = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stokttl.setGeometry(QtCore.QRect(10, 200, 47, 13))
        self.lbl_stokttl.setObjectName("lbl_stokttl")
        self.lbl_stokavbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stokavbl.setGeometry(QtCore.QRect(110, 200, 71, 16))
        self.lbl_stokavbl.setObjectName("lbl_stokavbl")
        self.inp_kodbrg = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_kodbrg.setGeometry(QtCore.QRect(10, 100, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_kodbrg.sizePolicy().hasHeightForWidth())
        self.inp_kodbrg.setSizePolicy(sizePolicy)
        self.inp_kodbrg.setText("")
        self.inp_kodbrg.setObjectName("inp_kodbrg")
        self.inp_nambrg = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_nambrg.setGeometry(QtCore.QRect(10, 160, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_nambrg.sizePolicy().hasHeightForWidth())
        self.inp_nambrg.setSizePolicy(sizePolicy)
        self.inp_nambrg.setText("")
        self.inp_nambrg.setObjectName("inp_nambrg")
        self.dir_bast = QtWidgets.QPushButton(self.centralwidget)
        self.dir_bast.setGeometry(QtCore.QRect(230, 280, 21, 21))
        self.dir_bast.setObjectName("dir_bast")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(10, 450, 221, 23))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(680, 460, 51, 21))
        self.btn_del.setObjectName("btn_del")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.btn_back.setObjectName("btn_back")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 20, 471, 431))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.inp_stkttl = QtWidgets.QSpinBox(self.centralwidget)
        self.inp_stkttl.setGeometry(QtCore.QRect(10, 220, 61, 22))
        self.inp_stkttl.setMaximum(10000)
        self.inp_stkttl.setObjectName("inp_stkttl")
        self.inp_stokavbl = QtWidgets.QSpinBox(self.centralwidget)
        self.inp_stokavbl.setGeometry(QtCore.QRect(110, 220, 61, 22))
        self.inp_stokavbl.setMaximum(10000)
        self.inp_stokavbl.setObjectName("inp_stokavbl")
        self.lbl_nambrg_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nambrg_2.setGeometry(QtCore.QRect(10, 260, 101, 16))
        self.lbl_nambrg_2.setObjectName("lbl_nambrg_2")
        self.inp_bastdir = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_bastdir.setGeometry(QtCore.QRect(10, 280, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_bastdir.sizePolicy().hasHeightForWidth())
        self.inp_bastdir.setSizePolicy(sizePolicy)
        self.inp_bastdir.setText("")
        self.inp_bastdir.setObjectName("inp_bastdir")
        self.inp_rowdel = QtWidgets.QComboBox(self.centralwidget)
        self.inp_rowdel.setGeometry(QtCore.QRect(600, 460, 69, 21))
        self.inp_rowdel.setObjectName("inp_rowdel")
        wdw_gdgrg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wdw_gdgrg)
        self.statusbar.setObjectName("statusbar")
        wdw_gdgrg.setStatusBar(self.statusbar)
        self.connecting()

        #################################START#################################
        self.dir_bast.pressed.connect(self.finddir)
        self.btn_submit.pressed.connect(self.submit)
        #################################ENDS##################################

        self.retranslateUi(wdw_gdgrg)
        QtCore.QMetaObject.connectSlotsByName(wdw_gdgrg)

    def retranslateUi(self, wdw_gdgrg):
        _translate = QtCore.QCoreApplication.translate
        wdw_gdgrg.setWindowTitle(_translate("wdw_gdgrg", "Daftar Barang"))
        self.lbl_title.setText(_translate("wdw_gdgrg", "Daftar Barang"))
        self.lbl_kodbrg.setText(_translate("wdw_gdgrg", "Kode Barang"))
        self.lbl_nambrg.setText(_translate("wdw_gdgrg", "Nama Barang"))
        self.lbl_stokttl.setText(_translate("wdw_gdgrg", "Stok Total"))
        self.lbl_stokavbl.setText(_translate("wdw_gdgrg", "Stok Tersedia"))
        self.inp_kodbrg.setPlaceholderText(_translate("wdw_gdgrg", "ex. BK001"))
        self.inp_nambrg.setPlaceholderText(_translate("wdw_gdgrg", "ex. Sendal Swallow"))
        self.dir_bast.setText(_translate("wdw_gdgrg", "..."))
        self.btn_submit.setText(_translate("wdw_gdgrg", "Submit"))
        self.btn_del.setText(_translate("wdw_gdgrg", "Delete"))
        self.btn_back.setText(_translate("wdw_gdgrg", "Kembali"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("wdw_gdgrg", "ID Barang"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("wdw_gdgrg", "Nama Barang"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("wdw_gdgrg", "Stok Total"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("wdw_gdgrg", "Stok Tersedia"))
        self.lbl_nambrg_2.setText(_translate("wdw_gdgrg", "BAST Perolehan"))
        self.inp_bastdir.setPlaceholderText(_translate("wdw_gdgrg", "ex. C:\\Users\\Public\\Documents\\bast.jpg"))

    def connecting(self):
        order = "SELECT * from barang"
        mycursor.execute(order)
        data = mycursor.fetchall()
        if not data:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(1)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, 0, item)
            item = self.tableWidget.item(0, 0)
            item.setText("NULL")
        else:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, ndata in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(ndata)))

    def finddir(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.inp_bastdir.setText(self.path)

    def submit(self):
        idbrg = self.inp_kodbrg.text()
        namabrg = self.inp_nambrg.text()
        stoktot = self.inp_stkttl.text()
        stokavl = self.inp_stokavbl.text()
        bast = self.inp_bastdir.text()
        
        bast = convertToBinaryData(bast)
        stoktot = int(stoktot)
        stokavl = int(stokavl)
        try:
            sql_insert_blob_query = """ INSERT INTO barang
                            (id_barang, nama_barang, stok_total, stok_tersedia, bast_perolehan) VALUES (%s,%s,%s,%s,%s)"""
            inputdat = (idbrg,namabrg,stoktot,stokavl,bast)
            result = mycursor.execute(sql_insert_blob_query,inputdat)
            mydb.commit()
        except mysql.connector.Error as error:
            self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
            masuk = 0
        self.connecting()

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
