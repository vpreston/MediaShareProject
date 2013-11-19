#!/usr/bin/env python
# combine.py - combination of ShowGPL, About, Close scripts

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
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,\
                         QMessageBox,  QIcon

__version__ = '0.0.3'
from ui_combine import Ui_MainWindow
import qrc_combine

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionShow_GPL.triggered.connect(self.showGPL)
        self.action_About.triggered.connect(self.about)        
        iconToolBar = self.addToolBar("iconBar.png") 
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        self.actionShow_GPL.setIcon(QIcon(":/showgpl.png"))
        self.action_About.setIcon(QIcon(":/about.png"))
        self.action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        self.actionShow_GPL.setStatusTip("Show GPL Licence")
        self.action_About.setStatusTip("Pop up the About dialog.")
        self.action_Close.setStatusTip("Close the program.")
#------------------------------------------------------        
        iconToolBar.addAction(self.actionShow_GPL)
        iconToolBar.addAction(self.action_About)
        iconToolBar.addAction(self.action_Close)
        
    def showGPL(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('COPYING.txt').read())
        
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b> About this program </b> v %s
                <p>Copyright &copy; 2010 Joe Bloggs. 
                All rights reserved in accordance with
                GPL v2 or later - NO WARRANTIES!
                <p>This application can be used for 
                displaying OS and platform details.
                <p>Python %s -  PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
