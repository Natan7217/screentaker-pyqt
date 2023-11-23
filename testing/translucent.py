import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Полупрозрачный QLabel")
        self.setGeometry(100, 100, 800, 600)
        # Создаем QLabel для текста
        label = QLabel(self)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, 800, 50)  # Устанавливаем размер и позицию QLabel
        label.setFont(QFont("Arial", 20, QFont.Bold))  # Задаем шрифт и стиль
        label.setText("Opened")  # Устанавливаем текст
        label.setStyleSheet("background-color: rgba(255, 255, 255, 128)")  # Задаем цвет фона с прозрачностью


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
