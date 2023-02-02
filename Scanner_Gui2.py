 PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QScrollArea, QWidget, QVBoxLayout, QLabel
import sys
import os
import csv
import io
from graphviz import Graph
from Traverse import *
from Parser import *

class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sTree = QtWidgets.QLabel(self.centralwidget)
        # self.sTree.setGeometry(QtCore.QRect(4, 5, 1111, 791))
        self.sTree.setGeometry(QtCore.QRect(0, 0, 1900, 975))
        self.sTree.setText("")
        self.sTree.setPixmap(QtGui.QPixmap("Graph.png"))
        self.sTree.setScaledContents(True)
        self.sTree.setObjectName("sTree")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.showMaximized()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('parser_icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 734)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BrowseButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseButton.setGeometry(QtCore.QRect(50, 50, 93, 28))
        self.BrowseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseButton.setObjectName("BrowseButton")
        self.BrowseButton.clicked.connect(self.getfiles)
        self.ScanButton = QtWidgets.QPushButton(self.centralwidget)
        self.ScanButton.setGeometry(QtCore.QRect(160, 120, 93, 28))
        self.ScanButton.setObjectName("ScanButton")
        self.ScanButton.setEnabled(False)
        self.ScanButton.clicked.connect(self.scan_hand)
        self.ParseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ParseButton.setGeometry(QtCore.QRect(330, 120, 93, 28))
        self.ParseButton.setObjectName("ParseButton")
        self.ParseButton.setEnabled(False)
        self.ParseButton.clicked.connect(self.parse_hand)
        self.CodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.CodeButton.setGeometry(QtCore.QRect(240, 210, 93, 28))
        self.CodeButton.setObjectName("CodeButton")
        self.CodeButton.setEnabled(False)
        self.CodeButton.clicked.connect(self.code_hand)
        self.TokensButton = QtWidgets.QPushButton(self.centralwidget)
        self.TokensButton.setGeometry(QtCore.QRect(420, 210, 93, 28))
        self.TokensButton.setObjectName("TokensButton")
        self.TokensButton.setEnabled(False)
        self.TokensButton.clicked.connect(self.tokens_hand)
        self.TreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.TreeButton.setGeometry(QtCore.QRect(500, 120, 121, 28))
        self.TreeButton.setObjectName("TreeButton")
        self.TreeButton.setEnabled(False)
        self.TreeButton.clicked.connect(self.tree_hand)
        self.label = ScrollLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(80, 295, 650, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 50, 550, 31))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tiny Language Parser"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.ScanButton.setText(_translate("MainWindow", "Scan"))
        self.ParseButton.setText(_translate("MainWindow", "Parse"))
        self.CodeButton.setText(_translate("MainWindow", "Show Code"))
        self.TokensButton.setText(_translate("MainWindow", "Show Tokens"))
        self.TreeButton.setText(_translate("MainWindow", "Draw Syntax Tree"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
