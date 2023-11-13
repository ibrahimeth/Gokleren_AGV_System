
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 912)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("*{\n"
"\n"
"    background-color: rgb(94, 102, 109);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    \n"
"    background-color: rgb(234, 184, 35);\n"
"    border-radius : 9px ;\n"
"    color: rgb(4, 4, 4);\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setStyleSheet("background-color: rgb(56, 60, 97);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.header_left_frame = QtWidgets.QFrame(self.header_frame)
        self.header_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_left_frame.setObjectName("header_left_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_10.setContentsMargins(7, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.open_close_side_bar_btn = QtWidgets.QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setStyleSheet("QPushButton#open_close_side_bar_btn{\n"
"    background-color:rgb(56, 60, 97);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 21px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 6em;\n"
"    padding: 3px;\n"
"\n"
"}\n"
"\n"
"QPushButton#open_close_side_bar_btn:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/align-left.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QtCore.QSize(32, 32))
        self.open_close_side_bar_btn.setObjectName("open_close_side_bar_btn")
        self.horizontalLayout_10.addWidget(self.open_close_side_bar_btn, 0, QtCore.Qt.AlignLeft)
        self.Huma_LOGO = QtWidgets.QLabel(self.header_left_frame)
        self.Huma_LOGO.setMaximumSize(QtCore.QSize(310, 75))
        self.Huma_LOGO.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Huma_LOGO.setStyleSheet(".QLabel{\n"
"    border-radius : 10px ;\n"
"}")
        self.Huma_LOGO.setText("")
        self.Huma_LOGO.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/logo_siyah.png"))
        self.Huma_LOGO.setScaledContents(True)
        self.Huma_LOGO.setObjectName("Huma_LOGO")
        self.horizontalLayout_10.addWidget(self.Huma_LOGO, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.header_left_frame)
        self.header_top_frame = QtWidgets.QFrame(self.header_frame)
        self.header_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_top_frame.setObjectName("header_top_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_top_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logo = QtWidgets.QLabel(self.header_top_frame)
        self.logo.setMaximumSize(QtCore.QSize(65, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logo.setFont(font)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/roboticon.ico"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setIndent(1)
        self.logo.setObjectName("logo")
        self.horizontalLayout_4.addWidget(self.logo, 0, QtCore.Qt.AlignRight)
        self.yazi = QtWidgets.QLabel(self.header_top_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yazi.setFont(font)
        self.yazi.setStyleSheet("color: rgb(255, 255, 255);")
        self.yazi.setObjectName("yazi")
        self.horizontalLayout_4.addWidget(self.yazi, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.header_top_frame)
        self.header_right_frame = QtWidgets.QFrame(self.header_frame)
        self.header_right_frame.setStyleSheet("QPushButton{\n"
"    background-color:rgb(56, 60, 97);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 13px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 0em;\n"
"    padding:1px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(92, 98, 159);\n"
"    border-style: inset;\n"
"}")
        self.header_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_right_frame.setObjectName("header_right_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._btn = QtWidgets.QPushButton(self.header_right_frame)
        self._btn.setStyleSheet("border:none;")
        self._btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._btn.setIcon(icon1)
        self._btn.setIconSize(QtCore.QSize(25, 25))
        self._btn.setObjectName("_btn")
        self.horizontalLayout_3.addWidget(self._btn)
        self.medum_btn = QtWidgets.QPushButton(self.header_right_frame)
        self.medum_btn.setStyleSheet("border:none;")
        self.medum_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/minimize-2.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.medum_btn.setIcon(icon2)
        self.medum_btn.setIconSize(QtCore.QSize(25, 25))
        self.medum_btn.setObjectName("medum_btn")
        self.horizontalLayout_3.addWidget(self.medum_btn, 0, QtCore.Qt.AlignVCenter)
        self.x_btn = QtWidgets.QPushButton(self.header_right_frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.x_btn.setFont(font)
        self.x_btn.setStyleSheet("border:none;")
        self.x_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_btn.setIcon(icon3)
        self.x_btn.setIconSize(QtCore.QSize(25, 25))
        self.x_btn.setObjectName("x_btn")
        self.horizontalLayout_3.addWidget(self.x_btn)
        self.horizontalLayout_2.addWidget(self.header_right_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.header_frame)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu_cont_frame = QtWidgets.QFrame(self.main_frame)
        self.left_menu_cont_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.left_menu_cont_frame.setMaximumSize(QtCore.QSize(0, 16777215))
        self.left_menu_cont_frame.setStyleSheet("background-color: rgb(56, 66, 85);")
        self.left_menu_cont_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_cont_frame.setObjectName("left_menu_cont_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setContentsMargins(5, 10, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menu_frame = QtWidgets.QFrame(self.left_menu_cont_frame)
        self.menu_frame.setMinimumSize(QtCore.QSize(200, 0))
        self.menu_frame.setStyleSheet("QPushButton{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 16px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_frame)
        self.gridLayout.setContentsMargins(0, 0, 32, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(23)
        self.gridLayout.setObjectName("gridLayout")
        self.com_test_page_btn = QtWidgets.QPushButton(self.menu_frame)
        self.com_test_page_btn.setStyleSheet("\n"
"\n"
"QPushButton#com_test_page_btn{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton#com_test_page_btn:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.com_test_page_btn.setIcon(icon4)
        self.com_test_page_btn.setIconSize(QtCore.QSize(35, 35))
        self.com_test_page_btn.setObjectName("com_test_page_btn")
        self.gridLayout.addWidget(self.com_test_page_btn, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.home_page_buton = QtWidgets.QPushButton(self.menu_frame)
        self.home_page_buton.setStyleSheet("QPushButton#home_page_buton{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton#home_page_buton:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"QPushButton#home_page_buton:pressed{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_page_buton.setIcon(icon5)
        self.home_page_buton.setIconSize(QtCore.QSize(35, 35))
        self.home_page_buton.setObjectName("home_page_buton")
        self.gridLayout.addWidget(self.home_page_buton, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.grafik_panel_btn = QtWidgets.QPushButton(self.menu_frame)
        self.grafik_panel_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/trello.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.grafik_panel_btn.setIcon(icon6)
        self.grafik_panel_btn.setIconSize(QtCore.QSize(35, 35))
        self.grafik_panel_btn.setObjectName("grafik_panel_btn")
        self.gridLayout.addWidget(self.grafik_panel_btn, 6, 0, 1, 1)
        self.gorev_page_buton = QtWidgets.QPushButton(self.menu_frame)
        self.gorev_page_buton.setStyleSheet("\n"
"QPushButton#gorev_page_buton{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton#gorev_page_buton:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gorev_page_buton.setIcon(icon7)
        self.gorev_page_buton.setIconSize(QtCore.QSize(35, 35))
        self.gorev_page_buton.setObjectName("gorev_page_buton")
        self.gridLayout.addWidget(self.gorev_page_buton, 2, 0, 1, 1)
        self.map_page_btn = QtWidgets.QPushButton(self.menu_frame)
        self.map_page_btn.setStyleSheet("\n"
"QPushButton#map_page_btn{\n"
"    background-color:rgb(56, 66, 85);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 25px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton#map_page_btn:hover{\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.map_page_btn.setIcon(icon8)
        self.map_page_btn.setIconSize(QtCore.QSize(35, 35))
        self.map_page_btn.setObjectName("map_page_btn")
        self.gridLayout.addWidget(self.map_page_btn, 1, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.menu_frame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.left_menu_cont_frame)
        self.main_bodY_contents = QtWidgets.QFrame(self.main_frame)
        self.main_bodY_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_bodY_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_bodY_contents.setObjectName("main_bodY_contents")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.main_bodY_contents)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_bodY_contents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Home)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame = QtWidgets.QFrame(self.Home)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(35, 10, 35, 20)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setMaximumSize(QtCore.QSize(250, 150))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/konumsembol.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setMaximumSize(QtCore.QSize(350, 200))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/QR CODE.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setMaximumSize(QtCore.QSize(300, 150))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/662.png"))
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_15 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setMaximumSize(QtCore.QSize(300, 200))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/görev list .png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.MAPGRAPHHOME = QtWidgets.QVBoxLayout()
        self.MAPGRAPHHOME.setObjectName("MAPGRAPHHOME")
        self.gridLayout_2.addLayout(self.MAPGRAPHHOME, 3, 1, 1, 1)
        self.speedhomeibre = QtWidgets.QVBoxLayout()
        self.speedhomeibre.setObjectName("speedhomeibre")
        self.gridLayout_2.addLayout(self.speedhomeibre, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame)
        self.stackedWidget.addWidget(self.Home)
        self.Map_page = QtWidgets.QWidget()
        self.Map_page.setObjectName("Map_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Map_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.map_frane = QtWidgets.QFrame(self.Map_page)
        self.map_frane.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.map_frane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map_frane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.map_frane.setObjectName("map_frane")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.map_frane)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.map_frane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_10 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.mapx = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapx.sizePolicy().hasHeightForWidth())
        self.mapx.setSizePolicy(sizePolicy)
        self.mapx.setMaximumSize(QtCore.QSize(300, 300))
        self.mapx.setObjectName("mapx")
        self.gridLayout_8.addWidget(self.mapx, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.mapy = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapy.sizePolicy().hasHeightForWidth())
        self.mapy.setSizePolicy(sizePolicy)
        self.mapy.setMaximumSize(QtCore.QSize(300, 16777215))
        self.mapy.setObjectName("mapy")
        self.gridLayout_8.addWidget(self.mapy, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_13.addLayout(self.gridLayout_8)
        self.horizontalLayout_14.addWidget(self.frame_10)
        self.MappingGraph = QtWidgets.QVBoxLayout()
        self.MappingGraph.setObjectName("MappingGraph")
        self.horizontalLayout_14.addLayout(self.MappingGraph)
        self.verticalLayout_12.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.map_frane)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.RESETbtmapping = QtWidgets.QPushButton(self.frame_4)
        self.RESETbtmapping.setObjectName("RESETbtmapping")
        self.verticalLayout_11.addWidget(self.RESETbtmapping)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.map_frane)
        self.stackedWidget.addWidget(self.Map_page)
        self.gorev_page = QtWidgets.QWidget()
        self.gorev_page.setStyleSheet("")
        self.gorev_page.setObjectName("gorev_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gorev_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gorev_frame = QtWidgets.QFrame(self.gorev_page)
        self.gorev_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gorev_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gorev_frame.setObjectName("gorev_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gorev_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gorev_edit_frame = QtWidgets.QFrame(self.gorev_frame)
        self.gorev_edit_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.gorev_edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gorev_edit_frame.setObjectName("gorev_edit_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gorev_edit_frame)
        self.gridLayout_3.setContentsMargins(50, 20, 50, 20)
        self.gridLayout_3.setHorizontalSpacing(100)
        self.gridLayout_3.setVerticalSpacing(35)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hedef_Combobox = QtWidgets.QComboBox(self.gorev_edit_frame)
        self.hedef_Combobox.setMinimumSize(QtCore.QSize(20, 35))
        self.hedef_Combobox.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.hedef_Combobox.setEditable(False)
        self.hedef_Combobox.setIconSize(QtCore.QSize(16, 16))
        self.hedef_Combobox.setObjectName("hedef_Combobox")
        self.hedef_Combobox.addItem("")
        self.hedef_Combobox.addItem("")
        self.hedef_Combobox.addItem("")
        self.hedef_Combobox.addItem("")
        self.hedef_Combobox.addItem("")
        self.gridLayout_3.addWidget(self.hedef_Combobox, 1, 2, 1, 1)
        self.Gorev_combobox = QtWidgets.QComboBox(self.gorev_edit_frame)
        self.Gorev_combobox.setMinimumSize(QtCore.QSize(20, 35))
        self.Gorev_combobox.setObjectName("Gorev_combobox")
        self.Gorev_combobox.addItem("")
        self.Gorev_combobox.addItem("")
        self.Gorev_combobox.addItem("")
        self.gridLayout_3.addWidget(self.Gorev_combobox, 3, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gorev_edit_frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.row_count_input = QtWidgets.QLineEdit(self.gorev_edit_frame)
        self.row_count_input.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.row_count_input.setFont(font)
        self.row_count_input.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 9px;\n"
"    border-color: beige;\n"
"\n"
"    min-width: 10em;\n"
"    padding: -8px;\n"
"")
        self.row_count_input.setAlignment(QtCore.Qt.AlignCenter)
        self.row_count_input.setObjectName("row_count_input")
        self.gridLayout_3.addWidget(self.row_count_input, 4, 0, 1, 1)
        self.gorev_send_btn = QtWidgets.QPushButton(self.gorev_edit_frame)
        self.gorev_send_btn.setStyleSheet("QPushButton#gorev_send_btn {\n"
"    background-color: #Aa3636;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#gorev_send_btn:hover {\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        self.gorev_send_btn.setObjectName("gorev_send_btn")
        self.gridLayout_3.addWidget(self.gorev_send_btn, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gorev_edit_frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.gorev_edit_frame, 0, QtCore.Qt.AlignTop)
        self.frame_8 = QtWidgets.QFrame(self.gorev_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.grv_hata_msg = QtWidgets.QLabel(self.frame_8)
        self.grv_hata_msg.setStyleSheet("*{\n"
"    width: 100px;\n"
"    padding: 10px;\n"
"    border: 20px solid black ;\n"
"    padding: 1px;\n"
"}")
        self.grv_hata_msg.setObjectName("grv_hata_msg")
        self.verticalLayout_14.addWidget(self.grv_hata_msg)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.gorev_tablo_frame = QtWidgets.QFrame(self.gorev_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gorev_tablo_frame.sizePolicy().hasHeightForWidth())
        self.gorev_tablo_frame.setSizePolicy(sizePolicy)
        self.gorev_tablo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gorev_tablo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gorev_tablo_frame.setObjectName("gorev_tablo_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.gorev_tablo_frame)
        self.horizontalLayout_13.setContentsMargins(0, 10, 0, 6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.grv_list = QtWidgets.QTableWidget(self.gorev_tablo_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grv_list.sizePolicy().hasHeightForWidth())
        self.grv_list.setSizePolicy(sizePolicy)
        self.grv_list.setMinimumSize(QtCore.QSize(500, 330))
        self.grv_list.setMaximumSize(QtCore.QSize(500, 600))
        self.grv_list.setStyleSheet("*{\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"}")
        self.grv_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grv_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.grv_list.setAutoScrollMargin(16)
        self.grv_list.setTextElideMode(QtCore.Qt.ElideRight)
        self.grv_list.setShowGrid(True)
        self.grv_list.setGridStyle(QtCore.Qt.SolidLine)
        self.grv_list.setWordWrap(True)
        self.grv_list.setCornerButtonEnabled(True)
        self.grv_list.setRowCount(1)
        self.grv_list.setObjectName("grv_list")
        self.grv_list.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.grv_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.grv_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.grv_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.grv_list.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.grv_list.setItem(0, 1, item)
        self.grv_list.horizontalHeader().setCascadingSectionResizes(False)
        self.grv_list.horizontalHeader().setDefaultSectionSize(225)
        self.grv_list.horizontalHeader().setMinimumSectionSize(73)
        self.grv_list.horizontalHeader().setSortIndicatorShown(False)
        self.grv_list.verticalHeader().setCascadingSectionResizes(False)
        self.grv_list.verticalHeader().setDefaultSectionSize(32)
        self.grv_list.verticalHeader().setMinimumSectionSize(12)
        self.grv_list.verticalHeader().setSortIndicatorShown(False)
        self.grv_list.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_13.addWidget(self.grv_list, 0, QtCore.Qt.AlignBottom)
        self.sayac_show_text = QtWidgets.QLabel(self.gorev_tablo_frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.sayac_show_text.setFont(font)
        self.sayac_show_text.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;")
        self.sayac_show_text.setText("")
        self.sayac_show_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sayac_show_text.setObjectName("sayac_show_text")
        self.horizontalLayout_13.addWidget(self.sayac_show_text, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.gorev_tablo_frame)
        self.frame_2.setMinimumSize(QtCore.QSize(260, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(7, 10, 7, 10)
        self.verticalLayout_6.setSpacing(47)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sisteme_gonder_btn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.sisteme_gonder_btn.setFont(font)
        self.sisteme_gonder_btn.setStyleSheet("QPushButton#sisteme_gonder_btn {\n"
"    background-color: rgb(13, 19, 122);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#sisteme_gonder_btn:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.sisteme_gonder_btn.setObjectName("sisteme_gonder_btn")
        self.verticalLayout_6.addWidget(self.sisteme_gonder_btn)
        self._upbtn = QtWidgets.QPushButton(self.frame_2)
        self._upbtn.setMinimumSize(QtCore.QSize(186, 0))
        self._upbtn.setStyleSheet("QPushButton#_upbtn {\n"
"    background-color: #Aa3636;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#_upbtn:hover {\n"
"    background-color: #000000;\n"
"\n"
"    border-style: inset;\n"
"}")
        self._upbtn.setObjectName("_upbtn")
        self.verticalLayout_6.addWidget(self._upbtn)
        self._downbtn = QtWidgets.QPushButton(self.frame_2)
        self._downbtn.setStyleSheet("QPushButton#_downbtn {\n"
"    background-color: #Aa3636;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#_downbtn:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self._downbtn.setObjectName("_downbtn")
        self.verticalLayout_6.addWidget(self._downbtn)
        self.grv_list_temizle_btn = QtWidgets.QPushButton(self.frame_2)
        self.grv_list_temizle_btn.setStyleSheet("QPushButton#grv_list_temizle_btn {\n"
"    background-color : rgb(71, 156, 1);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#grv_list_temizle_btn:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grv_list_temizle_btn.setObjectName("grv_list_temizle_btn")
        self.verticalLayout_6.addWidget(self.grv_list_temizle_btn)
        self.horizontalLayout_13.addWidget(self.frame_2, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.gorev_tablo_frame)
        self.verticalLayout_4.addWidget(self.gorev_frame)
        self.stackedWidget.addWidget(self.gorev_page)
        self.grafik_Panell_page = QtWidgets.QWidget()
        self.grafik_Panell_page.setObjectName("grafik_Panell_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.grafik_Panell_page)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_9 = QtWidgets.QFrame(self.grafik_Panell_page)
        self.frame_9.setStyleSheet("QPushButton#grafikresetbtn {\n"
"    background-color: rgb(13, 19, 122);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#grafikresetbtn:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}\n"
"QPushButton#grafikstopbtn:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"QPushButton#grafikstopbtn {\n"
"    background-color: rgb(234, 184, 35);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.engineamper = QtWidgets.QVBoxLayout()
        self.engineamper.setObjectName("engineamper")
        self.gridLayout_6.addLayout(self.engineamper, 0, 4, 1, 1)
        self.backendrightrpm = QtWidgets.QVBoxLayout()
        self.backendrightrpm.setObjectName("backendrightrpm")
        self.gridLayout_6.addLayout(self.backendrightrpm, 2, 4, 1, 1)
        self.pilgrafik = QtWidgets.QVBoxLayout()
        self.pilgrafik.setObjectName("pilgrafik")
        self.gridLayout_6.addLayout(self.pilgrafik, 0, 2, 1, 1)
        self.frontrightrpm = QtWidgets.QVBoxLayout()
        self.frontrightrpm.setObjectName("frontrightrpm")
        self.gridLayout_6.addLayout(self.frontrightrpm, 1, 4, 1, 1)
        self.hizgrafik = QtWidgets.QVBoxLayout()
        self.hizgrafik.setObjectName("hizgrafik")
        self.gridLayout_6.addLayout(self.hizgrafik, 0, 1, 1, 1)
        self.backendleftrpm = QtWidgets.QVBoxLayout()
        self.backendleftrpm.setObjectName("backendleftrpm")
        self.gridLayout_6.addLayout(self.backendleftrpm, 2, 1, 1, 1)
        self.frontleftrpm = QtWidgets.QVBoxLayout()
        self.frontleftrpm.setObjectName("frontleftrpm")
        self.gridLayout_6.addLayout(self.frontleftrpm, 1, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(6, -1, 6, 6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.grafikpertimesayac = QtWidgets.QLabel(self.frame_9)
        self.grafikpertimesayac.setStyleSheet("\n"
"font: 75 8pt \"MS Shell Dlg 2\"")
        self.grafikpertimesayac.setObjectName("grafikpertimesayac")
        self.gridLayout_7.addWidget(self.grafikpertimesayac, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.grafikgeisslider = QtWidgets.QSlider(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafikgeisslider.sizePolicy().hasHeightForWidth())
        self.grafikgeisslider.setSizePolicy(sizePolicy)
        self.grafikgeisslider.setMaximum(100)
        self.grafikgeisslider.setProperty("value", 100)
        self.grafikgeisslider.setSliderPosition(100)
        self.grafikgeisslider.setOrientation(QtCore.Qt.Horizontal)
        self.grafikgeisslider.setTickInterval(0)
        self.grafikgeisslider.setObjectName("grafikgeisslider")
        self.gridLayout_7.addWidget(self.grafikgeisslider, 2, 0, 1, 3)
        self.grafikstopbtn = QtWidgets.QPushButton(self.frame_9)
        self.grafikstopbtn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(234, 184, 35);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color:black;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grafikstopbtn.setObjectName("grafikstopbtn")
        self.gridLayout_7.addWidget(self.grafikstopbtn, 1, 2, 1, 1)
        self.grafiktpertime_A = QtWidgets.QPushButton(self.frame_9)
        self.grafiktpertime_A.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 19, 122);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grafiktpertime_A.setObjectName("grafiktpertime_A")
        self.gridLayout_7.addWidget(self.grafiktpertime_A, 0, 2, 1, 1)
        self.grafikpertime_E = QtWidgets.QPushButton(self.frame_9)
        self.grafikpertime_E.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 19, 122);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grafikpertime_E.setObjectName("grafikpertime_E")
        self.gridLayout_7.addWidget(self.grafikpertime_E, 0, 0, 1, 1)
        self.grafikresetbtn = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafikresetbtn.sizePolicy().hasHeightForWidth())
        self.grafikresetbtn.setSizePolicy(sizePolicy)
        self.grafikresetbtn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(52, 170, 34);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grafikresetbtn.setObjectName("grafikresetbtn")
        self.gridLayout_7.addWidget(self.grafikresetbtn, 1, 0, 1, 1)
        self.grafikcontiunebtn = QtWidgets.QPushButton(self.frame_9)
        self.grafikcontiunebtn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(13, 19, 122);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.grafikcontiunebtn.setObjectName("grafikcontiunebtn")
        self.gridLayout_7.addWidget(self.grafikcontiunebtn, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 2, 2, 1, 1)
        self.verticalLayout_10.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.grafik_Panell_page)
        self.com_test_page = QtWidgets.QWidget()
        self.com_test_page.setObjectName("com_test_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.com_test_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.com_test_page)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.frame_7)
        self.groupBox.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    \n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(170, 54, 54);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 16px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setHorizontalSpacing(9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(650, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 1)
        self.baudrat_comborade = QtWidgets.QComboBox(self.groupBox)
        self.baudrat_comborade.setObjectName("baudrat_comborade")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.baudrat_comborade.addItem("")
        self.gridLayout_5.addWidget(self.baudrat_comborade, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 3, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 16px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.baglandi_text = QtWidgets.QLabel(self.groupBox)
        self.baglandi_text.setText("")
        self.baglandi_text.setObjectName("baglandi_text")
        self.gridLayout_5.addWidget(self.baglandi_text, 4, 1, 1, 1)
        self.baglanmadi_text = QtWidgets.QLabel(self.groupBox)
        self.baglanmadi_text.setText("")
        self.baglanmadi_text.setObjectName("baglanmadi_text")
        self.gridLayout_5.addWidget(self.baglanmadi_text, 4, 2, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMouseTracking(False)
        self.frame_6.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    \n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(170, 54, 54);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    border-style: inset;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_8.addWidget(self.frame_6)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.com_test_page)
        self.horizontalLayout_11.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.main_bodY_contents)
        self.verticalLayout.addWidget(self.main_frame)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setStyleSheet("background-color: rgb(56, 66, 85);")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.footer_left_frame = QtWidgets.QFrame(self.footer_frame)
        self.footer_left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_left_frame.setObjectName("footer_left_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.copright = QtWidgets.QLabel(self.footer_left_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.copright.setFont(font)
        self.copright.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.copright.setStyleSheet("color: rgb(255, 255, 255);")
        self.copright.setObjectName("copright")
        self.horizontalLayout_7.addWidget(self.copright)
        self.horizontalLayout_6.addWidget(self.footer_left_frame)
        self.footer_center_frame = QtWidgets.QFrame(self.footer_frame)
        self.footer_center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_center_frame.setObjectName("footer_center_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_center_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.footer_center_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.footer_center_frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/feather/feather_beyaz/pil.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.footer_center_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.footer_center_frame)
        self.footer_right_frame = QtWidgets.QFrame(self.footer_frame)
        self.footer_right_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.footer_right_frame.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:rgb(56, 60, 97);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 14px;\n"
"    border-color: beige;\n"
"    font: bold 15px;\n"
"    min-width: 0em;\n"
"    padding:1px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(92, 98, 159);\n"
"    border-style: inset;\n"
"}")
        self.footer_right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_right_frame.setObjectName("footer_right_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(16)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.instagrm_btn = QtWidgets.QPushButton(self.footer_right_frame)
        self.instagrm_btn.setStyleSheet("")
        self.instagrm_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/3955024.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagrm_btn.setIcon(icon9)
        self.instagrm_btn.setIconSize(QtCore.QSize(32, 32))
        self.instagrm_btn.setObjectName("instagrm_btn")
        self.horizontalLayout_8.addWidget(self.instagrm_btn)
        self.info_btn = QtWidgets.QPushButton(self.footer_right_frame)
        self.info_btn.setStyleSheet("border:none;")
        self.info_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/feather/feather_beyaz/604573.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_btn.setIcon(icon10)
        self.info_btn.setIconSize(QtCore.QSize(32, 32))
        self.info_btn.setObjectName("info_btn")
        self.horizontalLayout_8.addWidget(self.info_btn)
        self.horizontalLayout_6.addWidget(self.footer_right_frame, 0, QtCore.Qt.AlignRight)
        self.size_grip = QtWidgets.QFrame(self.footer_frame)
        self.size_grip.setMinimumSize(QtCore.QSize(0, 30))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 30))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_6.addWidget(self.size_grip, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_close_side_bar_btn.setText(_translate("MainWindow", "MENÜ "))
        self.yazi.setText(_translate("MainWindow", "GÖKLEREN AGV \n"
"KONTROL MERKEZİ"))
        self.com_test_page_btn.setText(_translate("MainWindow", "   COM SETTİNGS   "))
        self.home_page_buton.setText(_translate("MainWindow", "  ANA SAYFA       "))
        self.grafik_panel_btn.setText(_translate("MainWindow", "   GRAFİK PANEL "))
        self.gorev_page_buton.setText(_translate("MainWindow", "  GÖREV SİSTEMİ"))
        self.map_page_btn.setText(_translate("MainWindow", " HARİTALAMA      "))
        self.label_9.setText(_translate("MainWindow", "HIZ : 32 m/dk"))
        self.label_10.setText(_translate("MainWindow", "ARAÇ KONUMU"))
        self.label_11.setText(_translate("MainWindow", "EN SO OKUNAN \n"
"QR KOD KONUMU"))
        self.label_12.setText(_translate("MainWindow", "GÖREV ANLIK"))
        self.label_14.setText(_translate("MainWindow", "MAP LİVE"))
        self.label_15.setText(_translate("MainWindow", "BATARYA : %94"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_6.setText(_translate("MainWindow", "    X = >>"))
        self.label_7.setText(_translate("MainWindow", "    Y  => >"))
        self.mapx.setText(_translate("MainWindow", "0000"))
        self.mapy.setText(_translate("MainWindow", "0000"))
        self.RESETbtmapping.setText(_translate("MainWindow", "RESET"))
        self.hedef_Combobox.setItemText(0, _translate("MainWindow", "A NOKTASI"))
        self.hedef_Combobox.setItemText(1, _translate("MainWindow", "B NOKTASI"))
        self.hedef_Combobox.setItemText(2, _translate("MainWindow", "C NOKTASI"))
        self.hedef_Combobox.setItemText(3, _translate("MainWindow", "D NOKTASI"))
        self.hedef_Combobox.setItemText(4, _translate("MainWindow", "BAŞLANGIÇ NOKTASI"))
        self.Gorev_combobox.setItemText(0, _translate("MainWindow", "TRANSİT"))
        self.Gorev_combobox.setItemText(1, _translate("MainWindow", "YÜK AL"))
        self.Gorev_combobox.setItemText(2, _translate("MainWindow", "YÜK BIRAK"))
        self.label_22.setText(_translate("MainWindow", "HEDEF : >>>"))
        self.row_count_input.setPlaceholderText(_translate("MainWindow", " SENARYO ADET"))
        self.gorev_send_btn.setText(_translate("MainWindow", "GÖNDER"))
        self.label_23.setText(_translate("MainWindow", "GÖREV : >>>"))
        self.grv_hata_msg.setText(_translate("MainWindow", "..."))
        item = self.grv_list.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.grv_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "HEDEF"))
        item = self.grv_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GÖREV"))
        __sortingEnabled = self.grv_list.isSortingEnabled()
        self.grv_list.setSortingEnabled(False)
        self.grv_list.setSortingEnabled(__sortingEnabled)
        self.sayac_show_text.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.sisteme_gonder_btn.setText(_translate("MainWindow", "SİSTEME GÖNDER"))
        self._upbtn.setText(_translate("MainWindow", "YUKARI"))
        self._downbtn.setText(_translate("MainWindow", "AŞAĞI"))
        self.grv_list_temizle_btn.setText(_translate("MainWindow", "TEMİZLE"))
        self.grafikpertimesayac.setText(_translate("MainWindow", "0"))
        self.grafikstopbtn.setText(_translate("MainWindow", "STOP"))
        self.grafiktpertime_A.setText(_translate("MainWindow", "+>>"))
        self.grafikpertime_E.setText(_translate("MainWindow", "<<-"))
        self.grafikresetbtn.setText(_translate("MainWindow", "RESET"))
        self.grafikcontiunebtn.setText(_translate("MainWindow", "CONTIUNE"))
        self.groupBox.setTitle(_translate("MainWindow", "PORT SETTİNGS"))
        self.label_4.setText(_translate("MainWindow", "Select Baudrate :"))
        self.label.setText(_translate("MainWindow", "Select Port Name :"))
        self.label_5.setText(_translate("MainWindow", "Situation :"))
        self.baudrat_comborade.setCurrentText(_translate("MainWindow", "110"))
        self.baudrat_comborade.setItemText(0, _translate("MainWindow", "110"))
        self.baudrat_comborade.setItemText(1, _translate("MainWindow", "300"))
        self.baudrat_comborade.setItemText(2, _translate("MainWindow", "600"))
        self.baudrat_comborade.setItemText(3, _translate("MainWindow", "1200"))
        self.baudrat_comborade.setItemText(4, _translate("MainWindow", "2400"))
        self.baudrat_comborade.setItemText(5, _translate("MainWindow", "4800 "))
        self.baudrat_comborade.setItemText(6, _translate("MainWindow", "9600"))
        self.baudrat_comborade.setItemText(7, _translate("MainWindow", "14400"))
        self.baudrat_comborade.setItemText(8, _translate("MainWindow", "17200"))
        self.baudrat_comborade.setItemText(9, _translate("MainWindow", "38400"))
        self.baudrat_comborade.setItemText(10, _translate("MainWindow", "57600"))
        self.baudrat_comborade.setItemText(11, _translate("MainWindow", "115200"))
        self.baudrat_comborade.setItemText(12, _translate("MainWindow", "128000"))
        self.baudrat_comborade.setItemText(13, _translate("MainWindow", "256000"))
        self.pushButton.setText(_translate("MainWindow", "DİSCONNECT"))
        self.pushButton_2.setText(_translate("MainWindow", "CONNECT"))
        self.copright.setText(_translate("MainWindow", "HUMA AR-GE ©2022  All rights reserved"))
        self.label_8.setText(_translate("MainWindow", "%94"))
        self.label_3.setText(_translate("MainWindow", "32 m/dk"))
import icons_rc
