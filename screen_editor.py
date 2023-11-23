# Importing PyQt5
from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QPainter, QMouseEvent, QCursor, QColor, QPen, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFrame, QButtonGroup
import pathlib


class EditScreenWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, self.screen().size().width(), self.screen().size().height())
        self.setWindowTitle(' ')
        self.begin = QPoint()  # Starting point / Начальная точка
        self.end = QPoint()  # End point / Конечная точка
        self.central_widget = QLabel()
        self.setCentralWidget(self.central_widget)
        # Taking screenshot / Делаем снимок экрана
        self.screenshot = QApplication.primaryScreen().grabWindow(0)
        # Display the screenshot in the QLabel / Отображаем скриншот в QLabel
        self.central_widget.setPixmap(self.screenshot.scaled(self.size(), aspectRatioMode=Qt.IgnoreAspectRatio))
        buttons_area = QWidget(self)
        buttons_area.setFixedSize(70, 700)
        buttons_area.setStyleSheet(
            "background-color: rgba(255, 255, 255, 150);"
            "border-radius: 15px;"
        )
        # Создание action_layout для кнопок
        action_layout = QVBoxLayout(buttons_area)
        action_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        action_layout.setSpacing(10)
        action_layout.setContentsMargins(5, 5, 5, 5)  # Отступы внутри области с кнопками
        # Создание кнопок
        self.area_group = QButtonGroup()
        self.rect_area = QPushButton(
            QIcon(QPixmap(f"{pathlib.Path(__file__).parent.absolute()}\\images\\pyqt_icons\\rect_area.png"
                          ).scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)),
            "",
            buttons_area)
        self.rect_area.setAccessibleName("rect_area")
        self.rect_area.setFixedSize(50, 50)
        self.rect_area.setCheckable(True)
        self.rect_area.setChecked(True)
        self.area_group.addButton(self.rect_area)
        self.area_group.setId(self.rect_area, 1)
        self.ellipse_area = QPushButton(
            QIcon(QPixmap(f"{pathlib.Path(__file__).parent.absolute()}\\images\\pyqt_icons\\oval_area.png"
                          ).scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)),
            "", buttons_area)
        self.ellipse_area.setAccessibleName("ellipse_area")
        self.ellipse_area.setFixedSize(50, 50)
        self.ellipse_area.setCheckable(True)
        self.area_group.addButton(self.ellipse_area)
        self.area_group.setId(self.ellipse_area, 2)
        self.area_group.buttonClicked[int].connect(self.switch_area)
        # Add a separator line (QFrame)
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        button3 = QPushButton('Кнопка 3', buttons_area)
        button3.setFixedSize(50, 50)
        button4 = QPushButton('Кнопка 4', buttons_area)
        button4.setFixedSize(50, 50)
        button5 = QPushButton('Кнопка 5', buttons_area)
        button5.setFixedSize(50, 50)
        button6 = QPushButton('Кнопка 6', buttons_area)
        button6.setFixedSize(50, 50)
        button7 = QPushButton('Кнопка 7', buttons_area)
        button7.setFixedSize(50, 50)
        button8 = QPushButton('Кнопка 8', buttons_area)
        button8.setFixedSize(50, 50)
        button9 = QPushButton('Кнопка 9', buttons_area)
        button9.setFixedSize(50, 50)
        button10 = QPushButton('Кнопка 10', buttons_area)
        button10.setFixedSize(50, 50)
        button11 = QPushButton('Кнопка 11', buttons_area)
        button11.setFixedSize(50, 50)
        button12 = QPushButton('Кнопка 12', buttons_area)
        button12.setFixedSize(50, 50)
        button13 = QPushButton('Кнопка 13', buttons_area)
        button13.setFixedSize(50, 50)
        # Добавление кнопок в layout
        action_layout.addWidget(self.rect_area)
        action_layout.addWidget(self.ellipse_area)
        action_layout.addWidget(separator_line)
        action_layout.addWidget(button3)
        action_layout.addWidget(button4)
        action_layout.addWidget(button5)
        action_layout.addWidget(button6)
        action_layout.addWidget(button7)
        action_layout.addWidget(button8)
        action_layout.addWidget(button9)
        action_layout.addWidget(button10)
        action_layout.addWidget(button11)
        action_layout.addWidget(button12)
        action_layout.addWidget(button13)
        # Установка стилей для кнопок
        self.set_object_style(self.rect_area)
        self.set_object_style(self.ellipse_area)
        self.set_object_style(button3)
        self.set_object_style(button4)
        self.set_object_style(button5)
        self.set_object_style(button6)
        self.set_object_style(button7)
        self.set_object_style(button8)
        self.set_object_style(button9)
        self.set_object_style(button10)
        self.set_object_style(button11)
        self.set_object_style(button12)
        self.set_object_style(button13)
        # Расположение области с кнопками посередине справа
        screen_geometry = QApplication.desktop().screenGeometry()
        buttons_area.move(screen_geometry.width() - buttons_area.width() - 50,
                          screen_geometry.height() // 2 - buttons_area.height() // 2)
        # Changing cursor type / Изменяем тип курсора
        QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()

    def paintEvent(self, event):
        painter = QPainter()
        copy_screen = self.screenshot.copy()
        painter.begin(copy_screen)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.area_group.button(1).isChecked():
            painter.setPen(QPen(QColor('black'), 2, Qt.DashLine))
            painter.setBrush(QColor(128, 128, 255, 128))
            painter.drawRect(QRectF(self.begin, self.end))
        else:
            painter.setPen(QPen(QColor('black'), 2, Qt.DashLine))
            painter.drawRect(QRectF(self.begin, self.end))
            painter.setBrush(QColor(128, 128, 255, 128))
            painter.drawEllipse(QRectF(self.begin, self.end))
        painter.end()

        self.central_widget.setPixmap(copy_screen.scaled(self.size(), aspectRatioMode=1))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        QApplication.restoreOverrideCursor()
        self.close()
        self.area_group.button(1).setChecked(True)
        if event.button() == Qt.RightButton:
            return
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        print(x1, y1, x2, y2)

    def set_object_style(self, qt_object):
        qt_object.setStyleSheet(
            """QPushButton { 
                background-color: #E74C3C;
                border: 4px solid #2980b9;
                border-radius: 10px;
                color: white;
                padding: 10px 20px;
            }
            QPushButton:checked {
                /* Style for checked state */
                /* Стиль для checked состояния */
                background-color: #fa402d;
                border-color: #27ae60;
            }""")

    def switch_area(self, button_id: int):
        clicked_button = self.area_group.button(button_id)
        if clicked_button.isChecked():
            for button in self.area_group.buttons():
                if button != clicked_button:
                    button.setChecked(False)
                    return
