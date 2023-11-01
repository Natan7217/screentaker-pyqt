import sys
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap("bg.jpg")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)


class MainPage(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("main.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    window = MainPage()
    window.show()

    splash.finish(window)
    app.exec_()
