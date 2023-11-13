import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from mongodbconnection import DbConnect
from matplotlib.widgets import Widget
import numpy as np

from main_ui import Ui_MainWindow

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow,self).__init__()
        # self.db = DbConnect()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ag = 1
        self.rowc = 0
        self.cloumc = 0
        self.a = 1
        self.initUI()
    
    def initUI(self) : 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # buton fonksiyonları eklenir.
        self.ui.open_close_side_bar_btn.clicked.connect(self.openSlideMenu)
        self.ui.instagrm_btn.clicked.connect(self.sosyal)
        self.ui.info_btn.clicked.connect(self.info)
        self.ui.x_btn.clicked.connect(lambda : self.close())
        self.ui._btn.clicked.connect(lambda : self.showMinimized())
        self.ui.medum_btn.clicked.connect(self.restore_or_maximize_window)
        self.ui.home_page_buton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.map_page_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.Map_page))
        self.ui.gorev_page_buton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.gorev_page))
        self.ui.grafik_panel_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.grafik_Panell_page))
        self.ui.com_test_page_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.com_test_page))

        # sayfa butonları tanımlanır 
        self.ui.com_test_page_btn.clicked.connect(lambda : self.ui.com_test_page)
        
        # görev sayfası edit 
        self.ui.sayac_show_text.setText(str(self.ag))
        self.ui.gorev_send_btn.clicked.connect(self.grafikgecir)

        # test part
        # while True :
        #     time.sleep(1)
        #     # self.ui.label_9.setText(self.db.control("aana"))
        def moveWindow(e):
            if self.isMaximized == False :
                if e.buttons() == Qt.LeftButton :
                    self.move(self.pos() + e.globalPos() - self.ClickPosition)
                    self.clickPoistion = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event) :
        self.clickPosition = event.globalPos()

    def grafikgecir(self) :
        print(self.ui.hedef_Combobox)
        # self.ui.grv_list.setItem(1 , 1,  self.ui.hedef_Combobox.currentText())
        # self.ui.grv_list.setItem(0 , 1, self.ui.Gorev_combobox.currentText())
        self.rowc += 1
        self.cloumc += 1    
        
        print(self.ui.hedef_Combobox.Text())

    def openSlideMenu(self) :
        width = self.ui.left_menu_cont_frame.width()
        if width == 0 :
            newWidth = 210
        else :
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
           
    def sosyal(self) :
        pass
    def info(self) :
        pass
    def restore_or_maximize_window(self) :
        if self.isMaximized():
            self.showNormal()
            self.ui.medum_btn.setIcon(QIcon(u":/feather/feather_beyaz/maximize-2.svg"))
        else :
            self.showMaximized()
            self.ui.medum_btn.setIcon(QIcon(u":/feather/feather_beyaz/minimize-2.svg"))
  