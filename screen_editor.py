# Importing PyQt5
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QMouseEvent, QCursor, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab


class EditScreenWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QPoint()
        self.end = QPoint()
        self.setWindowOpacity(0.3)
        QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()
        print('Capture the screen...')

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(QColor('black'), 3))
        qp.setBrush(QColor(128, 128, 255, 128))
        qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
