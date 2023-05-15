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

def convertdate(tanggal):
    idx1 = tanggal.find('/')
    bulan = tanggal[0:idx1]
    if (len(bulan)!=2):
        bulan = '0'+bulan
    idx2 = tanggal.find('/',idx1+1)
    hari = tanggal[idx1+1:idx2]
    if (len(hari)!=2):
        hari = '0'+hari
    tahun = tanggal[idx2+1:]
    return f'{tahun}-{bulan}-{hari}'

class Ui_wdw_tambahbarang(object):
    def setupUi(self, wdw_tambahbarang):
        wdw_tambahbarang.setObjectName("wdw_tambahbarang")
        wdw_tambahbarang.resize(745, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdw_tambahbarang.sizePolicy().hasHeightForWidth())
        wdw_tambahbarang.setSizePolicy(sizePolicy)
        wdw_tambahbarang.setMinimumSize(QtCore.QSize(745, 510))
        wdw_tambahbarang.setMaximumSize(QtCore.QSize(745, 510))
        self.centralwidget = QtWidgets.QWidget(wdw_tambahbarang)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_idpinj = QtWidgets.QLabel(self.centralwidget)
        self.lbl_idpinj.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.lbl_idpinj.setObjectName("lbl_idpinj")
        self.lbl_idpem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_idpem.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.lbl_idpem.setObjectName("lbl_idpem")
        self.lbl_jumbar = QtWidgets.QLabel(self.centralwidget)
        self.lbl_jumbar.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.lbl_jumbar.setObjectName("lbl_jumbar")
        self.inp_idpinj = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_idpinj.setGeometry(QtCore.QRect(10, 100, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_idpinj.sizePolicy().hasHeightForWidth())
        self.inp_idpinj.setSizePolicy(sizePolicy)
        self.inp_idpinj.setText("")
        self.inp_idpinj.setObjectName("inp_idpinj")
        self.inp_idpem = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_idpem.setGeometry(QtCore.QRect(10, 150, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_idpem.sizePolicy().hasHeightForWidth())
        self.inp_idpem.setSizePolicy(sizePolicy)
        self.inp_idpem.setText("")
        self.inp_idpem.setObjectName("inp_idpem")
        self.dir_bastdis = QtWidgets.QPushButton(self.centralwidget)
        self.dir_bastdis.setGeometry(QtCore.QRect(200, 400, 21, 21))
        self.dir_bastdis.setObjectName("dir_bastdis")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(10, 450, 211, 23))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.btn_back.setObjectName("btn_back")
        self.inp_jumbar = QtWidgets.QSpinBox(self.centralwidget)
        self.inp_jumbar.setGeometry(QtCore.QRect(10, 250, 61, 22))
        self.inp_jumbar.setMaximum(1000)
        self.inp_jumbar.setObjectName("inp_jumbar")
        self.lbl_bastdis = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bastdis.setGeometry(QtCore.QRect(10, 380, 101, 16))
        self.lbl_bastdis.setObjectName("lbl_bastdis")
        self.inp_bastdir = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_bastdir.setGeometry(QtCore.QRect(10, 400, 181, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inp_bastdir.sizePolicy().hasHeightForWidth())
        self.inp_bastdir.setSizePolicy(sizePolicy)
        self.inp_bastdir.setText("")
        self.inp_bastdir.setObjectName("inp_bastdir")
        self.lbl_kombar = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kombar.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.lbl_kombar.setObjectName("lbl_kombar")
        self.lbl_tglpinj = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tglpinj.setGeometry(QtCore.QRect(10, 280, 81, 16))
        self.lbl_tglpinj.setObjectName("lbl_tglpinj")
        self.lbl_tglpeng = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tglpeng.setGeometry(QtCore.QRect(120, 280, 91, 16))
        self.lbl_tglpeng.setObjectName("lbl_tglpeng")
        self.inp_datepinj = QtWidgets.QDateEdit(self.centralwidget)
        self.inp_datepinj.setGeometry(QtCore.QRect(10, 300, 101, 22))
        self.inp_datepinj.setObjectName("inp_datepinj")
        self.inp_datepeng = QtWidgets.QDateEdit(self.centralwidget)
        self.inp_datepeng.setGeometry(QtCore.QRect(120, 300, 101, 22))
        self.inp_datepeng.setObjectName("inp_datepeng")
        self.lbl_gedung = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gedung.setGeometry(QtCore.QRect(10, 330, 47, 13))
        self.lbl_gedung.setObjectName("lbl_gedung")
        self.lbl_norgn = QtWidgets.QLabel(self.centralwidget)
        self.lbl_norgn.setGeometry(QtCore.QRect(120, 330, 71, 16))
        self.lbl_norgn.setObjectName("lbl_norgn")
        self.inp_combgdg = QtWidgets.QComboBox(self.centralwidget)
        self.inp_combgdg.setGeometry(QtCore.QRect(10, 350, 101, 22))
        self.inp_combgdg.setObjectName("inp_combgdg")
        self.inp_combnrgn = QtWidgets.QComboBox(self.centralwidget)
        self.inp_combnrgn.setGeometry(QtCore.QRect(120, 350, 101, 22))
        self.inp_combnrgn.setObjectName("inp_combnrgn")
        self.inp_combbar = QtWidgets.QComboBox(self.centralwidget)
        self.inp_combbar.setGeometry(QtCore.QRect(10, 200, 181, 22))
        self.inp_combbar.setObjectName("inp_combbar")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(230, 10, 511, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_datpinjam = QtWidgets.QWidget()
        self.tab_datpinjam.setObjectName("tab_datpinjam")
        self.inp_rowdel = QtWidgets.QComboBox(self.tab_datpinjam)
        self.inp_rowdel.setGeometry(QtCore.QRect(370, 420, 69, 21))
        self.inp_rowdel.setObjectName("inp_rowdel")
        self.btn_reset = QtWidgets.QPushButton(self.tab_datpinjam)
        self.btn_reset.setGeometry(QtCore.QRect(180, 420, 51, 23))
        self.btn_reset.setObjectName("btn_reset")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_datpinjam)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 491, 411))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.btn_filter = QtWidgets.QPushButton(self.tab_datpinjam)
        self.btn_filter.setGeometry(QtCore.QRect(120, 420, 51, 23))
        self.btn_filter.setObjectName("btn_filter")
        self.btn_del = QtWidgets.QPushButton(self.tab_datpinjam)
        self.btn_del.setGeometry(QtCore.QRect(450, 420, 51, 21))
        self.btn_del.setObjectName("btn_del")
        self.inp_filter = QtWidgets.QComboBox(self.tab_datpinjam)
        self.inp_filter.setGeometry(QtCore.QRect(10, 420, 101, 22))
        self.inp_filter.setObjectName("inp_filter")
        self.tabWidget.addTab(self.tab_datpinjam, "")
        self.tab_datbar = QtWidgets.QWidget()
        self.tab_datbar.setObjectName("tab_datbar")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_datbar)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 0, 491, 441))
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_datbar, "")
        wdw_tambahbarang.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wdw_tambahbarang)
        self.statusbar.setObjectName("statusbar")
        wdw_tambahbarang.setStatusBar(self.statusbar)
        self.connectingpem()
        self.connectingbrg()
        self.combbar()
        self.combged()
        self.combrgn()
        #################################START#################################
        self.dir_bastdis.pressed.connect(self.finddir)
        self.btn_submit.pressed.connect(self.submit)
        self.btn_filter.pressed.connect(self.filter)
        self.btn_reset.pressed.connect(self.connectingpem)
        #################################ENDS##################################

        self.retranslateUi(wdw_tambahbarang)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdw_tambahbarang)

    def retranslateUi(self, wdw_tambahbarang):
        _translate = QtCore.QCoreApplication.translate
        wdw_tambahbarang.setWindowTitle(_translate("wdw_tambahbarang", "Daftar Barang"))
        self.lbl_title.setText(_translate("wdw_tambahbarang", "Daftar Peminjaman"))
        self.lbl_idpinj.setText(_translate("wdw_tambahbarang", "ID Peminjaman"))
        self.lbl_idpem.setText(_translate("wdw_tambahbarang", "ID Peminjam"))
        self.lbl_jumbar.setText(_translate("wdw_tambahbarang", "Jumlah Barang"))
        self.inp_idpinj.setPlaceholderText(_translate("wdw_tambahbarang", "ex. BK-100101-001 (Tipe - Tanggal - Urut)"))
        self.inp_idpem.setPlaceholderText(_translate("wdw_tambahbarang", "ex. 119140194 (NIM,NIP,no.KTP,dll)"))
        self.dir_bastdis.setText(_translate("wdw_tambahbarang", "..."))
        self.btn_submit.setText(_translate("wdw_tambahbarang", "Submit"))
        self.btn_back.setText(_translate("wdw_tambahbarang", "Kembali"))
        self.lbl_bastdis.setText(_translate("wdw_tambahbarang", "BAST Disposisi"))
        self.inp_bastdir.setPlaceholderText(_translate("wdw_tambahbarang", "ex. C:\\Users\\Public\\Documents\\bast.jpg"))
        self.lbl_kombar.setText(_translate("wdw_tambahbarang", "ID Barang"))
        self.lbl_tglpinj.setText(_translate("wdw_tambahbarang", "Tanggal Pinjam"))
        self.lbl_tglpeng.setText(_translate("wdw_tambahbarang", "Tanggal Kembali"))
        self.lbl_gedung.setText(_translate("wdw_tambahbarang", "Gedung"))
        self.lbl_norgn.setText(_translate("wdw_tambahbarang", "No. Ruangan"))
        self.btn_reset.setText(_translate("wdw_tambahbarang", "Reset"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("wdw_tambahbarang", "ID Peminjaman"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("wdw_tambahbarang", "ID Peminjam"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("wdw_tambahbarang", "ID Barang"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("wdw_tambahbarang", "Jumlah Barang"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("wdw_tambahbarang", "Tanggal Pinj."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("wdw_tambahbarang", "Gedung"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("wdw_tambahbarang", "No. Ruangan"))
        self.btn_filter.setText(_translate("wdw_tambahbarang", "Filter"))
        self.btn_del.setText(_translate("wdw_tambahbarang", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_datpinjam), _translate("wdw_tambahbarang", "Data Peminjaman"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("wdw_tambahbarang", "ID Barang"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("wdw_tambahbarang", "Nama Barang"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("wdw_tambahbarang", "Stok Total"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("wdw_tambahbarang", "Stok Tersedia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_datbar), _translate("wdw_tambahbarang", "Daftar Barang"))
    
    def connectingpem(self):
        order = "SELECT * FROM peminjaman"
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

    def connectingbrg(self):
        order = "SELECT * FROM barang"
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

    def filter(self):
        target = self.inp_filter.currentText()
        order = f"SELECT * FROM peminjaman WHERE gedung='{target}'"
        mycursor.execute(order)
        data = mycursor.fetchall()
        if not data:
            self.tableWidget.setColumnCount(1)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(0, item)            
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

    def combo(self,target,loc):
        order = f"SELECT {target} FROM {loc}"
        mycursor.execute(order)
        data = mycursor.fetchall()
        mydb.commit()
        return data
        

    def combbar(self):
        self.data = []
        self.data1 = self.combo("id_barang","barang")
        for i in self.data1:
            self.data.append(i[0])
        self.inp_combbar.addItems(self.data)

    def combged(self):
        self.data = []
        self.data1 = self.combo("kode_gedung","gedung")
        for i in self.data1:
            self.data.append(i[0])
        self.inp_combgdg.addItems(self.data)
        self.inp_filter.addItems(self.data)

    def combrgn(self):
        self.data = []
        self.data1 = self.combo("no_ruangan","ruangan")
        for i in self.data1:
            self.data.append(i[0])
        self.inp_combnrgn.addItems(self.data)

    
    def submit(self):
        idpin = self.inp_idpinj.text()
        idpem = self.inp_idpem.text()
        idbrg = self.inp_combbar.currentText()
        jumbrg = self.inp_jumbar.text()
        tglpin = self.inp_datepinj.text()
        tglpin = convertdate(str(tglpin))
        tglpem = self.inp_datepeng.text()
        tglpem = convertdate(str(tglpem))
        gedg = self.inp_combgdg.currentText()
        norgn = self.inp_combnrgn.currentText()
        bastdis = self.inp_bastdir.text()

        bastdis = convertToBinaryData(bastdis)
        jumbrg = int(jumbrg)
        try:
            sql_insert_blob_query = """ INSERT INTO peminjaman
                            (id_peminjaman, id_peminjam, id_barang, jumlah_barang, tgl_peminjaman, tgl_pengembalian, gedung, no_ruangan, bast_disposisi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            inputdat = (idpin, idpem, idbrg, jumbrg, tglpin, tglpem, gedg, norgn, bastdis)
            result = mycursor.execute(sql_insert_blob_query,inputdat)
            mydb.commit()
        except mysql.connector.Error as error:
            self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
            masuk = 0
        self.connectingpem()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdw_tambahbarang = QtWidgets.QMainWindow()
    ui = Ui_wdw_tambahbarang()
    ui.setupUi(wdw_tambahbarang)
    wdw_tambahbarang.show()
    sys.exit(app.exec_())
