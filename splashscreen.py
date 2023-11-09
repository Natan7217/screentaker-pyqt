# Importing PyQt5
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
# Importing standard libraries
import time
import pathlib


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap(f"{pathlib.Path(__file__).parent.absolute()}\\images\\images\\bg-with-logo.jpg")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.05)
            self.progressBar.setValue(i)
