import main_menureal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="db_pbo"
)
mycursor = mydb.cursor()

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.NonModal)
        LoginWindow.resize(562, 442)
        LoginWindow.setMinimumSize(QtCore.QSize(562, 442))
        LoginWindow.setMaximumSize(QtCore.QSize(562, 442))
        LoginWindow.setBaseSize(QtCore.QSize(562, 442))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wdw_chlog = QtWidgets.QTextBrowser(self.centralwidget)
        self.wdw_chlog.setGeometry(QtCore.QRect(30, 110, 501, 291))
        self.wdw_chlog.setObjectName("wdw_chlog")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(320, 30, 101, 51))
        self.btn_login.setDefault(False)
        self.btn_login.setObjectName("btn_login")
        self.inp_username = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_username.setGeometry(QtCore.QRect(90, 30, 181, 20))
        self.inp_username.setObjectName("inp_username")
        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.lbl_username.setObjectName("lbl_username")
        self.lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.lbl_password.setObjectName("lbl_password")
        self.inp_password = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_password.setGeometry(QtCore.QRect(90, 60, 181, 20))
        self.inp_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inp_password.setObjectName("inp_password")
        self.btn_registr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registr.setGeometry(QtCore.QRect(430, 30, 101, 51))
        self.btn_registr.setObjectName("btn_registr")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        #################################START#################################
        self.btn_login.pressed.connect(self.functlogin)
        
        #################################ENDS##################################

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Bababooey!"))
        self.btn_login.setText(_translate("LoginWindow", "Login"))
        self.lbl_username.setText(_translate("LoginWindow", "Username"))
        self.lbl_password.setText(_translate("LoginWindow", "Password"))
        self.btn_registr.setText(_translate("LoginWindow", "UNDER DEV"))

    def functlogin(self):
        self.username = self.inp_username.text()
        if not (self.username):
            self.show_Popup("Username dan Password tidak boleh kosong!")
            return 0
        mycursor.execute("SELECT password FROM login_info WHERE username  = '" + self.username + "\'")
        result = mycursor.fetchall()
        if not result:
            self.show_Popup("Username atau Password anda salah")
            return 0
        result = (result[0])[0]
        print(type(result))
        print(result)
        if result == self.inp_password.text():
            self.show_Popup("Anda telah berhasil Login!")
            mycursor.execute("SELECT account_role FROM login_info WHERE username  = '" + self.username + "\'")
            result = mycursor.fetchall()
            result = (result[0])[0]
            self.gotomain(LoginWindow)
        else:
            self.show_Popup("Username atau Password anda salah!")

    def gotomain(self,LoginWindow):
        self.Menu = QtWidgets.QMainWindow()
        self.ui = main_menureal.Ui_wdw_mainmenu()
        self.ui.getMeAName(self.username)
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        LoginWindow.hide()
        self.ui.btn_logout.clicked.connect(lambda: self.reapp(LoginWindow))
    
    def reapp(self, LoginWindow):
        self.Menu.hide()
        LoginWindow.show()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
