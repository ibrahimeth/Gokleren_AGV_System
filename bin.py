from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
import sys
import random
import numpy as np
from main_ui import Ui_MainWindow


class BinWindow(QMainWindow) :
    def __init__(self) :
        super(BinWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.initUI()
    
    def initUI(self) : 
        # buton fonksiyonları eklenir.
        self.ui.open_close_side_bar_btn.clicked.connect(self.openSlideMenu)
        self.ui.instagrm_btn.clicked.connect(self.sosyal)
        self.ui.info_btn.clicked.connect(self.info)

        self.ui.com_test_page_btn.clicked.connect(lambda : self.ui.com_test_page)


        print(self.ui.left_menu_cont_frame.minimumWidth())
    
    def openSlideMenu(self) :
        if str(self.ui.left_menu_cont_frame.minimumWidth) == 0 :
            self.ui.left_menu_cont_frame.setMinimumWidth(210)
        else :
            self.ui.left_menu_cont_frame.setMinimumWidth(0)
    def sosyal(self) :
        pass
    def info(self) :
        pass