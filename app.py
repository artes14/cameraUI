import sys
import cv2
import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot, QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_start.triggered.connect(self.TE)
        self.action_About.triggered.connect(self.about)

    def TE(self):
        dialog=TEDialog(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About this UI",
            "<p>UI to use TE Q1:  </p>" 
            "<p>- PyQt  </p>"
            "<p>- Qt Designer  </p>"
            "<p>- Python   </p>",
        )



class TEDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/te.ui",self)
        self.TEXT.setText('press start to connect with te!')
        self.action_Exit.triggered.connect(self.close)
        self.start_btn.clicked.connect(self.startClicked)
        self.cap_btn.clicked.connect(self.capClicked)
        self.logic=1
        self.imgnum=0


    def startClicked(self):
        self.TEXT.setText('press Capture! to capture image')
        capture=cv2.VideoCapture(-1)
        # th=Thread(self)
        # th.changePixmap.connect(self.setImage)
        # th.start()
        # self.show()
        while(capture.isOpened()):
            ret, frame=capture.read()
            if ret==True:
                print('ret')
                self.displayImage(frame, 1)
                cv2.waitKey()
                if(self.logic==2):
                    cv2.imwrite('./images/cap_%s.png'%self.imgnum, frame)
                    self.logic=1
                    self.TEXT.setText('image saved as cap_%s.png'%self.imgnum)
                    imgdialog = imgDialog(self)
                    imgdialog.setimage(frame, 'cap_%s.png'%self.imgnum)
                    imgdialog.exec()
                    self.imgnum+=1
                else:
                    print("return not found")
        capture.release()
        cv2.destroyAllWindows()
    def setImage(self, image):
        self.imgLabel.setPixmap(QPixmap.fromImage(image))
    def capClicked(self):
        self.logic=2



    def displayImage(self, img, window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if(img.shape[2])==4:
                qformat=QImage.Format_RGBA888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(img, img.shape[1], img.shape[0], qformat)
        img=img.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

class imgDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/cap.ui",self)
    def setimage(self, img, name):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.label.setPixmap(QPixmap.fromImage(img))
        self.setWindowTitle(name)



if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec())