import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
from random import sample

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
        self.label1.setText(self.mylottonumbers2_sortet + ' ' + self.myeurojacknumbers2_sortet) ###
        self.updatelabel1()

    def updatelabel1(self):
        self.label1.adjustSize()

    def gennumbers(self):
        #Generate 5 LottoNumbers
        self.mylottonumbers2 = sample(range(1, 49),5)
        self.mylottonumbers2_sortet = sorted(self.mylottonumbers2)
        self.mylottonumbers2_sortet = ' '.join(str(e) for e in self.mylottonumbers2_sortet) ### Convert the integers for settext
        #Generate 2 EuroNumbers
        self.myeurojacknumbers2 = sample(range(1, 10),2)
        self.myeurojacknumbers2_sortet = sorted(self.myeurojacknumbers2)    
        self.myeurojacknumbers2_sortet = ' '.join(str(e) for e in self.myeurojacknumbers2_sortet) ### Convert the integers for settext

def window():
    #main_window
    app = QApplication(sys.argv)
    win = MyWindow()

    #show_main_window
    win.show()
    sys.exit(app.exec_())
window()
