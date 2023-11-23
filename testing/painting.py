import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.path = []
        self.drawing = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.path = [event.pos()]

    def mouseMoveEvent(self, event):
        if self.drawing and event.buttons() & Qt.LeftButton:
            self.path.append(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        for i in range(1, len(self.path)):
            painter.drawLine(self.path[i - 1], self.path[i])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.drawing_widget = DrawingWidget()
        layout.addWidget(self.drawing_widget)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clearDrawing)
        layout.addWidget(clear_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Path Drawing App')
        self.show()

    def clearDrawing(self):
        self.drawing_widget.path = []
        self.drawing_widget.update()


def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
