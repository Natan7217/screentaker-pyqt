import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen


class ScreenshotLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.screenshot = QPixmap()  # Placeholder for the screenshot

    def setScreenshot(self, screenshot):
        self.screenshot = screenshot

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.screenshot)

        # Draw a rectangle on the screenshot
        pen = QPen(QColor(255, 0, 0))  # Red color for the rectangle border
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(100, 100, 200, 150)  # Adjust coordinates and size of the rectangle as needed


class ScreenshotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Screenshot with Rectangle')
        self.central_widget = ScreenshotLabel(self)
        self.setCentralWidget(self.central_widget)
        self.showFullScreen()

        self.take_screenshot()

    def take_screenshot(self):
        # Take a screenshot of the entire desktop
        screenshot = QApplication.primaryScreen().grabWindow(0)
        self.central_widget.setScreenshot(screenshot)
        self.central_widget.repaint()


def main():
    app = QApplication(sys.argv)
    window = ScreenshotApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
