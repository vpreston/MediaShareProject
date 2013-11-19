#!/usr/bin/env python
# about.py - display about box with info on platform etc.

# Copyright (c) 2010-2011 Algis Kabaila. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

import sys
import platform

import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,  QMessageBox

from ui_about import Ui_MainWindow

__version__ = '0.0.1'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.aboutButton.clicked.connect(self.about)
               
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b>Platform Details</b> v %s
                <p>Copyright &copy; 2010 Al Kabaila. 
                All rights reserved in accordance with
                GPL v2 or later - NO WARRANTIES!
                <p>This application can be used for 
                displaying platform details.
                <p>Python %s -  PySide version %s - Qt version %s on %s""" % (__version__, 
                platform.python_version(), PySide.__version__,  PySide.QtCore.__version__,
                platform.system()))
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    
