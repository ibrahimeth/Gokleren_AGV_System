from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore,QtGui
from main import MainWindow
from login_ui import Ui_Dialog
import sys
import webbrowser as wb

import qt_material

# from main import Entry_Window

class login_Window(QDialog):
    def __init__(self):
        super(login_Window,self).__init__()

        # Adding item on the menu bar
        tray = QSystemTrayIcon()
        tray.setIcon(QIcon(u":/feather/feather_beyaz/roboticon.ico"))
        tray.setVisible(True)

        self.timer = QTimer()
        self.t = 0

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.app = MainWindow()

        self.setWindowTitle("GÖKELREN AGV ADMİN GİRİŞ")
        self.setWindowIcon(QIcon(u":/feather/feather_beyaz/roboticon.ico"))

        self.initui()
        
    def initui(self) :
        self.ui.password_lineedit.setStyleSheet("color : red;font: 75 14pt 'MS Shell Dlg 2';")
        self.ui.password_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.password_lineedit.setEchoMode(QLineEdit.Password)
        self.ui.password_lineedit.returnPressed.connect(self.Contol)
        self.ui.giris_btn.clicked.connect(self.Contol)
        self.ui.insta_btn.clicked.connect(self.social)
        self.show()
    
    def social(self) :
        hesap = "https://www.instagram.com/huma_arge_takimi/"
        wb.open(hesap)

    def Contol(self) :

        self.giff = QDialog(self)

        self.vbox = QVBoxLayout()

        self.girisyapiliyor = QLabel("KONTROL YAPILIYOR ...")
        self.girisyapiliyor.setObjectName("giriş")
        self.girisyapiliyor.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.girisyapiliyor.setAlignment(QtCore.Qt.AlignHCenter)
        self.girisyapiliyor.setStyleSheet("color : red ; font: 25pt")

        bekle = QLabel("deneme")

        bekle.setAlignment(QtCore.Qt.AlignHCenter)

        loading = QMovie(u":/feather/feather_beyaz/humamix2.gif")
        loading.setScaledSize(QSize(300,300))

        bekle.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        bekle.setMovie(loading)

        self.vbox.addWidget(bekle)
        self.vbox.addWidget(self.girisyapiliyor)

        loading.start()

        self.giff.setLayout(self.vbox)

        self.giff.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.giff.setWindowFlags(QtCore.Qt.Window| QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.giff.setWindowModality(QtCore.Qt.ApplicationModal)

        self.timer.timeout.connect(self.time)
        self.timer.start(1000)
        
        self.hide()
        self.giff.show()

    def time(self) :
        self.t += 1
        if self.t >2 :
            if self.ui.password_lineedit.text() == "admin" :
                self.girisyapiliyor.setText("HOŞGELDİNİZ")
                if self.t >4 :
                    self.giff.close()
                    self.t = 0
                    self.timer.stop()
                    self.app.showMaximized()
            else:
                self.t = 0
                self.timer.stop()
                self.giff.close()
                self.ui.hata_mesaj.setText("LÜTFEN ŞİFREYİ DOĞRU GİRİNİZ \nHUMA AR-GE TEKNİK EKİBİ")
                self.show()

def mainLOOP():
    fas = QApplication(sys.argv)
    win = login_Window()
    sys.exit(fas.exec_())

mainLOOP()

