import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
import random

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(900,400,350,300) #x y width height
        self.setWindowTitle("My EuroJackpot Generator")
        self.initUI()

    def initUI(self):
        #label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hier ihre Zahlen:")
        self.label.move(10,0)
    
        #label2
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("")
        self.label1.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Black))
        self.label1.move(10,40)

        #button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Generiere Zahlen")
        self.button.move(10,200)
        self.button.clicked.connect(self.clickedbutton1)
    
    def clickedbutton1(self):
        self.gennumbers()
        self.label1.setText(self.mylottonumbers + ' ' + self.euronumbers) ###
        self.updatelabel1()

    def updatelabel1(self):
        self.label1.adjustSize()
    
    def gennumbers(self):
        self.mylottonumbers= []
        self.euronumbers= []
        #Generate Lottonumbers
        for x in range (5):
            self.randnumb = random.randint(1, 49)
            if self.randnumb not in self.mylottonumbers:
                self.mylottonumbers.append(self.randnumb)
            else:
                self.randnumbifexi = random.randint(1, 49)
                self.mylottonumbers.append(self.randnumbifexi)
            self.mylottonumbers.sort()
        self.mylottonumbers = ' '.join(str(e) for e in self.mylottonumbers) ### Convert the integers for settext
        
        # Generate Euronumbers
        for x in range (2):
            self.randnumb = random.randint(1, 10)
            if self.randnumb not in self.euronumbers:
                self.euronumbers.append(self.randnumb)
            else:
                self.randnumbifexi = random.randint(1, 10)
                self.euronumbers.append(self.randnumbifexi)
            self.euronumbers.sort()
        self.euronumbers = ' '.join(str(e) for e in self.euronumbers) ### Convert the integers for settext

def window():
    #main_window
    app = QApplication(sys.argv)
    win = MyWindow()

    #show_main_window
    win.show()
    sys.exit(app.exec_())
window()
