from PyQt5.QtWidgets import *
from  motion_capture import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
import os



class Window1(QWidget):
    def _init_(self):
        QWidget._init_(self)
        
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        files=os.listdir('motion_data')
        for i in files:
           self.listwidget.insertItem(0, i) 
       
        self.listwidget.clicked.connect(self.clicked)
        layout.addWidget(self.listwidget)

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())


class Window(QtWidgets.QMainWindow):
    def _init_(self):
        QtWidgets.QWidget._init_(self)
        uic.loadUi("FrontPage.ui", self)
        # click logic for button

        self.Camera_btn.clicked.connect(self.capture_live)
        self.BrouseVideo_btn.clicked.connect(self.Browse_File)
        self.PreviousVideo_btn.clicked.connect(self.show_saved_content)
        self.Setting_btn.clicked.connect(self.clicked)
        

        

   
    def browse_file(self):

        fname,ftype = QFileDialog.getOpenFileName(self, 'Select a video', './','Video (*.mp4 *.avi)')
        motion_capture_video(fname)


    def capture_live(self):
        # print("clicked")
        motion_capture 


    def show_saved_content(self) :
        #files=os.listdir('motion_data')
        app1 = QApplication(sys.argv)
        screen = Window1()
        screen.show()
        app1.exec()

            

        



    def clicked(self):
        print("other one")

        

if __name__ == "main_":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    #sys.exit(app.exec_())
    app.exec()