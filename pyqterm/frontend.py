# -*- coding: utf-8 -*-
import sys, os
import time

from PyQt4.QtCore import QRect, Qt, pyqtSignal, QByteArray
from PyQt4.QtGui import (
       QApplication, QClipboard, QWidget, QPainter, QFont, QBrush, QColor, 
       QPen, QPixmap, QImage, QContextMenuEvent)
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore

from .backend import Session




DEBUG = False



class TerminalWidget(QWidget):

    
    foreground_color_map = {
      0: "#000",
      1: "#b00",
      2: "#0b0",
      3: "#bb0",
      4: "#00b",
      5: "#b0b",
      6: "#0bb",
      7: "#bbb",
      8: "#666",
      9: "#f00",
      10: "#0f0",
      11: "#ff0",
      12: "#00f", # concelaed
      13: "#f0f",
      14: "#000", # negative
      15: "#fff", # default
      'default': "#fff",
    }
    background_color_map = {
      0: "#000",
      1: "#b00",
      2: "#0b0",
      3: "#bb0",
      4: "#00b",
      5: "#b0b",
      6: "#0bb",
      7: "#bbb",
      12: "#aaa", # cursor
      14: "#000", # default
      'default': "#000",
      15: "#fff", # negative
    }
    keymap = {
       Qt.Key_Backspace: chr(127),
       Qt.Key_Escape: chr(27),
       Qt.Key_AsciiTilde: "~~",
       Qt.Key_Up: "~A",
       Qt.Key_Down: "~B",
       Qt.Key_Left: "~D",
       Qt.Key_Right: "~C",
       Qt.Key_PageUp: "~1",
       Qt.Key_PageDown: "~2",
       Qt.Key_Home: "~H",
       Qt.Key_End: "~F",
       Qt.Key_Insert: "~3",
       Qt.Key_Delete: "~4",
       Qt.Key_F1: "~a",
       Qt.Key_F2: "~b",
       Qt.Key_F3:  "~c",
       Qt.Key_F4:  "~d",
       Qt.Key_F5:  "~e",
       Qt.Key_F6:  "~f",
       Qt.Key_F7:  "~g",
       Qt.Key_F8:  "~h",
       Qt.Key_F9:  "~i",
       Qt.Key_F10:  "~j",
       Qt.Key_F11:  "~k",
       Qt.Key_F12:  "~l",
    }


    session_closed = pyqtSignal()

    class Screen(object):
        def __init__(self, widget):
            self.widget = widget

        def draw(self, char):
            self.widget.update()

    def __init__(self, parent=None, command="/bin/bash", 
                 font_name="Monospace", font_size=18):
        super(TerminalWidget, self).__init__(parent)
        self.setFocusPolicy(Qt.WheelFocus)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_OpaquePaintEvent, True)

        self.setUI()
        self._session = None
        self._draw_screen = self.Screen(self)
        self.execute()

    def setUI(self):
        self.resize(600, 600)
        self.w_list = QtGui.QListWidget(self)
        self.w_list.setGeometry(0, 0, 600, 500)
        self.w_list.setAlternatingRowColors(True)

        self.w_edit = QtGui.QTextEdit(self)
        self.w_edit.setGeometry(0, 500, 600, 100)

        self.w_edit.textChanged.connect(self.On_textchanged)

    def On_textchanged(self):
        # a = str(self.w_edit.toPlainText())
        get_qtext = self.w_edit.toPlainText()
        if get_qtext.endsWith('\n'):
            # get_qtext.insert(get_qtext.count()-1,QtCore.QString('\r'))
            self.send(str(get_qtext))
            self.w_edit.clear()
        
    def execute(self, command="/bin/bash"):
        """
        启动终端进程
        :param command:
        :return:
        """
        ## 创建会话对象
        self._session = Session(cmd=command, parant_wid=self)
        self._session.stream.attach(self._draw_screen)

        self._session.start()
        self._screen = self._session.screen

            
    def send(self, s):
        self._session.write(s)

    def stop(self):
        self._session.stop()


    def setFont(self, font):
        super(TerminalWidget, self).setFont(font)
        self._update_metrics()


    def closeEvent(self, event):
        self._session.proc_bury()

    def update_screen(self):
        self.update()

    return_pressed = pyqtSignal()
