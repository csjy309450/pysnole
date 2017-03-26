#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import QApplication

from pyqterm import TerminalWidget

shell = {
    'python2.7': '/usr/bin/python2.7',
    'bash': '/bin/bash'
}

if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    win = TerminalWidget(command=shell['bash'], font_size=16)
    win.show()
    app.exec_()

