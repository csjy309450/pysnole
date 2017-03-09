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
        win = TerminalWidget(self)
        win.resize(500, 1000)
        self.show()

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