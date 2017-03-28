from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import sys
from pyqterm import TerminalWidget


class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # self.edit = QLineEdit(self)
        # self.edit.setGeometry(0, 0, 200, 30)
        # self.label = QLabel(self)
        # self.label.setGeometry(0, 31, 200, 200)
        # self.resize(205, 235)
        # self.edit.editingFinished.connect(self.On_editingFinished)
        # win = TerminalWidget(self)
        # win.resize(1000, 1000)
        self.resize(600, 600)
        self.w_list = QListWidget(self)
        self.w_list.setGeometry(0,0,600,500)
        self.w_list.setAlternatingRowColors(True)
        self.w_list.addItem(QListWidgetItem(QString('11111')))
        self.w_list.addItem(QListWidgetItem(QString('22222')))
        self.w_list.addItem(QListWidgetItem(QString('33333')))
        self.w_list.addItem(QListWidgetItem(QString('44444')))

        self.w_edit = QTextEdit(self)
        self.w_edit.setGeometry(0,500,600,100)

        self.w_edit.textChanged.connect(self.On_textchanged)

        self.show()

    def On_textchanged(self):
        # a = str(self.w_edit.toPlainText())
        get_qtext = self.w_edit.toPlainText()
        if get_qtext.endsWith('\n'):
            # print str(self.w_edit.toPlainText())
            self.w_list.addItem(QListWidgetItem(get_qtext.left(get_qtext.count()-1)))
            self.w_edit.clear()

    def On_editingFinished(self):
        get_cmd = str(self.edit.text())
        print get_cmd
        if get_cmd != '':
            output = os.popen(get_cmd)
            self.label.setText(output.read())

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    app.exec_()
