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

def getfiles(self):
        parent_dir = os.getcwd()
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File', parent_dir, '*.txt')
        try:
            file = open(self.fileName, 'r')
        except:
            return
        self.source_code = file.read()
        self.textBrowser.setText(self.fileName)
        self.label.setText(self.source_code)
        self.ParseButton.setEnabled(False)
        self.TokensButton.setEnabled(False)
        self.TreeButton.setEnabled(False)
        self.ScanButton.setEnabled(True)
        self.CodeButton.setEnabled(True)

    def parse_hand(self):
        self.parser = Parser(self.token_list)
        try:
            self.syntax_tree = self.parser.program()
        except IndexError:
            self.parser.index -= 1
            self.parser.accept = False
        except ValueError:
            self.parser.accept = False
        self.status = self.parser.accept
        self.show_popup_parser()

    def show_popup_parser(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parser Information")
        var_text = "Code is Accepted."
        var_icon = QMessageBox.Information
        if not (self.status == True):
            var_text = f"token number {self.parser.index} have error, which is node: {self.token_list[self.parser.index]['tokenvalue']}"
            var_icon = QMessageBox.Critical
        else:
            self.TreeButton.setEnabled(True)
        msg.setText(var_text)
        msg.setIcon(var_icon)
        msg.exec_()

    def code_hand(self):
        self.label.setText(self.source_code)

    def tokens_hand(self):
        texto = ""
        for i in range(len(self.token_list)):
            value1, value2 = self.token_list[i].values()
            texto += str(i)
            texto += '\t'
            texto += str(value2)
            texto += '\t'
            texto += str(value1)
            texto += str('\n')
        self.label.setText(texto)

    def scan_hand(self):
        self.token_list = self.scanner(self.fileName)
        self.show_popup_scanner()
        self.label.setText(self.source_code)
        self.ParseButton.setEnabled(True)
        self.TokensButton.setEnabled(True)

    def show_popup_scanner(self):
        msg = QMessageBox()
        msg.setWindowTitle("Scanner Information")
        msg.setText("A tokens.csv is created in current directory")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def tree_hand(self):
        dot = Graph(comment='lolo')
        traverse_obj = Traverse(dot)
        traverse_obj.traverse(self.syntax_tree)
        self.my_graph = traverse_obj.dot

        # saving source code
        self.my_graph.format = "png"
        self.my_graph.render("Graph", view=False)  # view = True so will open picture
        # plot image Graph.png
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def scanner(self, source_code_file_name):
        all_tokens = []
        special_symbols = ['+', '-', '*', '/', '=', '<', '(', ')', ';']

        for line in io.StringIO(self.source_code):
            i = 0
            token_str = ''
            state = 'START'
            while i < len(line):
                if ((line[i] in special_symbols) and (state != 'INCOMMENT') and (state != 'INASSIGN')):
                    if token_str != '':
                        all_tokens.append(token_str)
                        token_str = ''
                    state = 'DONE'
                    all_tokens.append(line[i])
                elif state == 'START':
                    if (line[i] == (' ' or '/t')):
                        state = 'START'

                    elif (line[i] == '{'):
                        state = 'INCOMMENT'
                        token_str += line[i]

                    elif (line[i] == ':'):
                        state = 'INASSIGN'
                        token_str += line[i]

                    elif ((line[i].isdigit()) or (line[i] == '.')):
                        state = 'INNUM'
                        token_str += line[i]

                    elif (line[i].isalpha()):
                        state = 'INID'
                        token_str += line[i]
                    else:
                        state = 'DONE'

                elif state == 'INCOMMENT':
                    if (line[i] == '}'):
                        state = 'START'
                        token_str += line[i]
                        all_tokens.append(token_str)
                        token_str = ''
                    else:
                        token_str += line[i]

                elif state == 'INASSIGN':
                    if (line[i] == '='):
                        state = 'DONE'
                        token_str += line[i]
                    else:
                        state = 'DONE'

                elif state == 'INNUM':
                    if ((line[i].isdigit()) or (line[i] == '.')):
                        state = 'INNUM'
                        token_str += line[i]
                    else:
                        state = 'DONE'
                        i -= 1


                elif state == 'INID':
                    if (line[i].isalpha()):
                        state = 'INID'
                        token_str += line[i]
                    else:
                        state = 'DONE'
                        i -= 1

                elif state == 'DONE':
                    if token_str != '':
                        all_tokens.append(token_str)
                        token_str = ''
                    state = 'START'
                    i -= 1

                i += 1
            if token_str != '':
                all_tokens.append(token_str)
                token_str = ''

        token_list = []
        list_negative = [':=', '<', '=', '(', '+', '*', '-', '/', 'if', 'write', 'until']

        flag = False
        for i, token in enumerate(all_tokens):
            r = token.replace('.', '', 1)
            if flag == True:
                flag = False
                continue
            if token == ':=':
                token_list.append({'tokentype': 'ASSIGN', 'tokenvalue': token})

            elif token == ';':
                token_list.append({'tokentype': 'SEMICOLON', 'tokenvalue': token})

            elif token == '<':
                token_list.append({'tokentype': 'LESSTHAN', 'tokenvalue': token})

            elif token == '=':
                token_list.append({'tokentype': 'EQUAL', 'tokenvalue': token})

            elif token == '+':
                token_list.append({'tokentype': 'PLUS', 'tokenvalue': token})

            elif token == '-':
                if (all_tokens[i - 1] in list_negative):
                    try:
                        if all_tokens[i + 1].isalpha():
                            token_list.append({'tokentype': 'IDENTIFIER', 'tokenvalue': all_tokens[i] + all_tokens[i + 1]})
                        else:
                            token_list.append({'tokentype': 'NUMBER', 'tokenvalue': all_tokens[i] + all_tokens[i + 1]})
                        flag = True
                    except:
                        token_list.append({'tokentype': 'MINUS', 'tokenvalue': token})
                else:
                    token_list.append({'tokentype': 'MINUS', 'tokenvalue': token})

            elif token == '*':
                token_list.append({'tokentype': 'MULT', 'tokenvalue': token})

            elif token == '/':
                token_list.append({'tokentype': 'DIV', 'tokenvalue': token})

            elif token == '(':
                token_list.append({'tokentype': 'OPENBRACKET', 'tokenvalue': token})

            elif token == ')':
                token_list.append({'tokentype': 'CLOSEDBRACKET', 'tokenvalue': token})

            elif token == 'if':
                token_list.append({'tokentype': 'IF', 'tokenvalue': token})

            elif token == 'then':
                token_list.append({'tokentype': 'THEN', 'tokenvalue': token})

            elif token == 'else':
                token_list.append({'tokentype': 'ELSE', 'tokenvalue': token})

            elif token == 'end':
                token_list.append({'tokentype': 'END', 'tokenvalue': token})

            elif token == 'repeat':
                token_list.append({'tokentype': 'REPEAT', 'tokenvalue': token})

            elif token == 'until':
                token_list.append({'tokentype': 'UNTIL', 'tokenvalue': token})

            elif token == 'read':
                token_list.append({'tokentype': 'READ', 'tokenvalue': token})

            elif token == 'write':
                token_list.append({'tokentype': 'WRITE', 'tokenvalue': token})

            elif token.isalpha():
                token_list.append({'tokentype': 'IDENTIFIER', 'tokenvalue': token})

            elif r.isdigit():
                token_list.append({'tokentype': 'NUMBER', 'tokenvalue': token})

            else:
                pass

        # gui to write
        file = open('tokens.csv', 'w')
        writer = csv.DictWriter(file, fieldnames=['tokentype', 'tokenvalue'])
        writer.writeheader()
        writer.writerows(token_list)
        file.close()

        return token_list


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())