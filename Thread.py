
import sys
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSlot, QThread, Qt, pyqtSignal

class Thread(QThread):
    changePixmap=pyqtSignal(QImage)
    def run(self):
        cap=cv2.VideoCapture(0)
        while True:
            ret, frame=cap.read()
            if ret:
                rgbImage=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch=rgbImage.shape
                bytesPerLine=ch*w
                convertToQtFormat=QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p=convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)