# Importing PyQt5
from PyQt5.QtCore import Qt, QSize, pyqtSlot
from PyQt5.QtGui import QPixmap, QMouseEvent, QWheelEvent, QFont
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
# Importing standard libraries
import os


class Img(QDialog):
    def __init__(self, curr_pic: int, pics: list, parent=None):
        super().__init__(parent)
        self.pictures = pics
        self.curr_pic_num = curr_pic
        self.setFixedSize(self.screen().size())
        layout = QVBoxLayout()
        self.label = QLabel(self)
        pixmap = QPixmap(pics[curr_pic])
        self.original_pixmap = pixmap.copy()  # For resizing image / Копируем изображение для его масштабирования
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)
        # self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(self.label)

        self.label_size = QSize(pixmap.width(), pixmap.height())
        self.label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.label.resize(pixmap.width(), pixmap.height())

        self.text_label = QLabel(self)
        self.text_label.setAlignment(Qt.AlignCenter)
        screen_size = self.screen().size()
        self.text_label.setGeometry(0, 0, screen_size.width(), 50)  # Устанавливаем размер и позицию QLabel /
        # Setting the size and position of the QLabel
        self.text_label.setFont(QFont("Arial", 20, QFont.Bold))  # Задаем шрифт и стиль / Set the font and style
        # Устанавливаем текст / Setting the text
        self.text_label.setText(f"{curr_pic + 1}/{len(pics)} {pixmap.width()}×{pixmap.height()} "
                                f"{pics[curr_pic].split(os.path.sep)[-1]}")
        self.text_label.setStyleSheet("background-color: rgba(255, 255, 255, 128)")  # Задаем цвет фона с
        # полупрозрачностью / Set the background color with translucency

        """
        self.background_label = QLabel(self)  # Попытка поставить фон с сеткой
        self.background_label.setGeometry(0, 0, self.screen().size().width(), self.screen().size().height())

        pixmap = QPixmap(f"{pathlib.Path(__file__).parent.absolute()}\\images\\images\\grid-bg.jpg")
        self.background_label.setPixmap(pixmap)  # Trying to set background
        """

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)

    def mousePressEvent(self, mouse_event: QMouseEvent) -> None:  # Closing image view / Закрытие окна
        if mouse_event.button() == Qt.LeftButton or mouse_event.button() == Qt.RightButton:
            self.close()

    def keyPressEvent(self, k) -> None:   # Closing image view / Закрытие окна
        if k.key() == Qt.Key_Escape or k.key() == Qt.Key_Meta:
            self.close()

    @pyqtSlot()
    def zoom(self, delta) -> None:  # Zooming image / Масштабирование изображения
        if delta < 0 and self.label_size.width() >= self.original_pixmap.size().width():  # Zooming out
            self.label_size = QSize(int(self.label_size.width() // 1.05), int(self.label_size.height() // 1.05))
        elif delta > 0 and self.label_size.width() <= 1920:  # Zooming in
            self.label_size = QSize(int(self.label_size.width() * 1.05), int(self.label_size.height() * 1.05))
        pixmap = self.original_pixmap.scaled(self.label_size.width(), self.label_size.height(),
                                             Qt.KeepAspectRatioByExpanding)
        self.label.setPixmap(pixmap)
        self.update()  # Updating image / Обновляем изображение

    def wheelEvent(self, wheel_event: QWheelEvent) -> None:  # Scrolling pictures & zooming /
        # Событие для масштабирования и передвижения между изображениями
        if wheel_event.modifiers() & Qt.ControlModifier:  # Zoom in/out | Приближение/Отдаление картинки
            self.zoom(wheel_event.angleDelta().y())
        elif Qt.ControlModifier:  # Changing the image / Меняем картинку на следующую
            self.change_image(wheel_event.angleDelta().y())

    @pyqtSlot()
    def change_image(self, delta) -> None:  # Changing the image / Меняем картинку на следующую
        if delta < 0 and self.curr_pic_num + 1 < len(self.pictures):
            self.curr_pic_num = self.curr_pic_num + 1
            pixmap = QPixmap(self.pictures[self.curr_pic_num])
            self.original_pixmap = pixmap.copy()  # For resizing image / Копируем изображение для его масштабирования
            self.label_size = pixmap.size()
            self.label.setPixmap(pixmap)
            self.text_label.setText(f"{self.curr_pic_num + 1}/{len(self.pictures)} {pixmap.width()}×{pixmap.height()} "
                                    f"{self.pictures[self.curr_pic_num].split(os.path.sep)[-1]}")
            self.update()  # Updating changes / Обновляем изменения
        elif delta > 0 and self.curr_pic_num > 0:
            self.curr_pic_num = self.curr_pic_num - 1
            pixmap = QPixmap(self.pictures[self.curr_pic_num])
            self.original_pixmap = pixmap.copy()  # For resizing image / Копируем изображение для его масштабирования
            self.label_size = pixmap.size()
            self.label.setPixmap(pixmap)
            self.text_label.setText(f"{self.curr_pic_num + 1}/{len(self.pictures)} {pixmap.width()}×{pixmap.height()} "
                                    f"{self.pictures[self.curr_pic_num].split(os.path.sep)[-1]}")
