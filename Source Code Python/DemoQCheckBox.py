#!/usr/bin/python3

#########################################################
# Nama file: DemoQCheckBox.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(300, 300)
      self.setWindowTitle('Demo QCheckBox')
      
      self.label = QLabel()
      self.label.setText('Tentukan pilihan Anda:')
      
      self.perlCheck = QCheckBox()
      self.perlCheck.setText('Perl')      
      self.pythonCheck = QCheckBox()
      self.pythonCheck.setText('Python')
      self.rubyCheck = QCheckBox()
      self.rubyCheck.setText('Ruby')
      self.phpCheck = QCheckBox()
      self.phpCheck.setText('PHP')
      hbox1 = QHBoxLayout()
      hbox1.addWidget(self.perlCheck)
      hbox1.addWidget(self.pythonCheck)
      hbox1.addWidget(self.rubyCheck)
      hbox1.addWidget(self.phpCheck)
            
      self.okButton = QPushButton('&OK')
      self.exitButton = QPushButton('Keluar')
      hbox2 = QHBoxLayout()
      hbox2.addStretch()
      hbox2.addWidget(self.okButton)
      hbox2.addWidget(self.exitButton)
      
      layout = QVBoxLayout()
      layout.addWidget(self.label)
      layout.addLayout(hbox1)
      horizontalLine = QFrame();
      horizontalLine.setFrameShape(QFrame.HLine)
      horizontalLine.setFrameShadow(QFrame.Sunken)
      layout.addWidget(horizontalLine)
      layout.addLayout(hbox2)
      layout.addStretch()
      self.setLayout(layout)
      
      self.okButton.clicked.connect(self.okButtonClick)
      self.exitButton.clicked.connect(self.close)

   def okButtonClick(self):
      choices = []
      if self.perlCheck.isChecked(): choices.append('Perl')
      if self.pythonCheck.isChecked(): choices.append('Python')
      if self.rubyCheck.isChecked(): choices.append('Ruby')
      if self.phpCheck.isChecked(): choices.append('PHP')
      QMessageBox.information(self, 'Informasi', repr(choices))

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = MainForm()
   form.show()
   
   a.exec_()
