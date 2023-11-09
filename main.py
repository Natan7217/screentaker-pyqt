# Importing PyQt5
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QVBoxLayout, QWidget,
    QCheckBox, QSystemTrayIcon,
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QMessageBox)
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent, QFont
from PyQt5.QtCore import Qt, QPoint, QObject, pyqtSlot
from PyQt5.QtWidgets import QAction
# Importing widgets
from about_program import AboutScreenTakerDialog
from full_screen_image import Img
from setting_hotkeys import HotkeyConfigDialog
from splashscreen import SplashScreen
# Importing stylesheets
from stylesheets import vertical_scroll_bar_stylesheet, horizontal_scroll_bar_stylesheet
# Importing "standard" libraries
from typing import Optional, Union
from io import BytesIO
from PIL import Image
import win32clipboard
import os
import sys
import pathlib
import ctypes
import platform


def linux_distribution() -> Optional[Union[tuple[str, str, str], str]]:
    try:
        return platform.linux_distribution()
    except AttributeError:
        return "N/A"


def send_to_clipboard(clip_type, data) -> None:
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp']
SCREENS_FOLDER_PATH = f"{pathlib.Path(__file__).parent.absolute()}\\images\\screens"
OPERATING_SYSTEM = platform.system() if linux_distribution() == "N/A" else "Linux"


class MainPage(QMainWindow):
    def __init__(self, tray_icon, application_icon):
        super(QMainWindow, self).__init__()
        self.tray_icon: QSystemTrayIcon = tray_icon
        self.app_icon: QIcon = application_icon
        loadUi("main.ui", self)
        self.setWindowTitle("ScreenTaker v1.0")
        # self.setMinimumSize()
        self.setWindowIcon(QIcon(f"{pathlib.Path(__file__).parent.absolute()}\\images\\images\\icon.png"))
        # Setting icon in the Windows taskbar, for linux I don't check it :O
        if OPERATING_SYSTEM == "Windows":
            my_app_id = 'natandev.screentaker'  # arbitrary app name (id)
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
        elif OPERATING_SYSTEM == "Linux":
            pass  # maybe I'll check it

        self.scroll_content = QWidget()
        self.scrollArea.setWidget(self.scroll_content)
        self.scrollArea.setWidgetResizable(True)
        self.content_layout = QVBoxLayout(self.scroll_content)

        all_files = os.listdir(SCREENS_FOLDER_PATH)
        image_files = [file for file in all_files if os.path.splitext(file)[-1].lower() in IMG_EXTENSIONS]
        self.pictures = [os.path.join(SCREENS_FOLDER_PATH, file) for file in image_files]
        for curr_num, image_path in enumerate(self.pictures):
            layout = QVBoxLayout()
            pixmap = QPixmap(image_path)
            image_label = QLabel()
            image_label.setAccessibleName(image_path)

            image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
            image_label.mousePressEvent = lambda event, cur_num=curr_num: self.open_full_screen_image(event, cur_num)

            image_label.setContextMenuPolicy(Qt.CustomContextMenu)
            image_label.customContextMenuRequested.connect(self.image_context_menu)

            text_label = QLabel(image_path.split(os.path.sep)[-1])
            text_label.setFont(QFont("Arial", 12))
            text_label.setStyleSheet("color: rgb(255, 255, 255)")
            text_label.setToolTip(f"<font color='black'>{image_path}</font>")
            layout.addWidget(image_label)
            layout.addWidget(text_label)
            self.content_layout.addLayout(layout)

        self.scrollArea.verticalScrollBar().setStyleSheet(vertical_scroll_bar_stylesheet)
        self.scrollArea.horizontalScrollBar().setStyleSheet(horizontal_scroll_bar_stylesheet)
        # self.textBrowser.raise_()
        self.create_menu_connects()

    def create_menu_connects(self):
        menu_bar = self.menuBar()

        help_action = QAction(self.style().standardIcon(QStyle.SP_TitleBarContextHelpButton), "&Help", self)
        hotkeys_action = QAction("Горячие клавиши", self)
        menu_bar.insertMenu(self.all_screen, )
        menu_bar.addAction(hotkeys_action)
        menu_bar.addAction(help_action)
        help_action.triggered.connect(self.open_about_program)
        hotkeys_action.triggered.connect(self.open_hotkey_setting)
        self.about_program.triggered.connect(self.open_about_program)

    def open_about_program(self):
        about_program_dialog = AboutScreenTakerDialog(self)
        about_program_dialog.exec_()

    def open_hotkey_setting(self):
        hotkey_config_dialog = HotkeyConfigDialog(self)
        hotkey_config_dialog.exec_()

    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "ScreenTaker",
            "Приложение свёрнуто в трей",
            self.app_icon,
            msecs=2000
        )

    def open_full_screen_image(self, event: QMouseEvent, curr_pic_num) -> None:
        if event.button() == Qt.LeftButton:
            try:
                widget = Img(curr_pic_num, self.pictures)
                widget.exec()
            except Exception as e:
                print(e)

    def image_context_menu(self, pos: QPoint) -> None:
        context_menu = QMenu(self)

        open_menu = QMenu("Открыть", self)
        open_menu.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        copy_menu = QMenu("Копировать", self)
        copy_menu.setIcon(self.style().standardIcon(QStyle.SP_FileLinkIcon))

        delete_action = QAction('Удалить изображение', self)
        # trash_icon = QImage(f"{pathlib.Path(__file__).parent.absolute()}\\images\\icons\\cil_x.png")
        # trash_icon.invertPixels(QImage.InvertRgba)
        # QIcon(QPixmap.fromImage(trash_icon))
        delete_action.setObjectName(self.sender().accessibleName())
        delete_action.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        delete_action.triggered.connect(self.delete_image_confirmation)

        open_file = QAction('Файл', self)
        open_file.setObjectName(self.sender().accessibleName())
        open_file.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        open_file.triggered.connect(self.open_file_event)

        open_folder = QAction('Папку', self)
        open_folder.setObjectName(f"{os.path.sep}".join(self.sender().accessibleName().split(os.path.sep)[:-1]))
        open_folder.setIcon(self.style().standardIcon(QStyle.SP_DirIcon))
        open_folder.triggered.connect(self.open_folder_event)

        copy_image = QAction('Изображение', self)
        copy_image.setObjectName(self.sender().accessibleName())
        copy_image.triggered.connect(self.image_to_clipboard)

        copy_size_image = QAction('Размеры изображения', self)

        separator = QAction(self)
        separator.setSeparator(True)

        copy_path_folder = QAction('Путь к папке', self)
        copy_path_folder.setObjectName(f"{os.path.sep}".join(self.sender().accessibleName().split(os.path.sep)[:-1]))
        copy_path_folder.triggered.connect(self.text_to_clipboard)

        copy_path_file = QAction('Путь к файлу', self)
        copy_path_file.setObjectName(self.sender().accessibleName())
        copy_path_file.triggered.connect(self.text_to_clipboard)

        copy_name_file = QAction('Имя файла', self)
        copy_name_file.setObjectName(self.sender().accessibleName().split(os.path.sep)[-1].split(".")[0])
        copy_name_file.triggered.connect(self.text_to_clipboard)

        copy_name_file_with_ext = QAction('Имя файла с расширением', self)
        copy_name_file_with_ext.setObjectName(self.sender().accessibleName().split(os.path.sep)[-1])
        copy_name_file_with_ext.triggered.connect(self.text_to_clipboard)

        open_menu.addActions([open_file, open_folder])
        copy_menu.addActions([copy_image, copy_size_image, separator, copy_path_folder,
                              copy_path_file, copy_name_file, copy_name_file_with_ext])

        context_menu.addMenu(open_menu)
        context_menu.addMenu(copy_menu)
        context_menu.addAction(delete_action)
        context_menu.exec_(self.sender().mapToGlobal(pos))

    def open_file_event(self):
        if OPERATING_SYSTEM == "Windows":
            try:
                path_img = self.sender().objectName()
                path_img_list = path_img.split(os.path.sep)[:-1]
                img_file, extension = path_img.split(os.path.sep)[-1].split(".")
                path_img_list.append('"' + img_file + '".' + extension)
                os.system('start ' + f"{os.path.sep}".join(path_img_list))
                #  Not recommended to use Popen / Не рекомендуется использовать Popen; представлен рабочий вариант с ним
                # subprocess.Popen(['rundll32', 'shimgvw.dll,ImageView_Fullscreen',
                #                   f"{os.path.sep}".join(path_img_list)])  # path_img_list: list (that contains
                #                                                                                  the path)
                # or subprocess.Popen(['start', f"{os.path.sep}".join(path_img_list)])
            except Exception as e:
                print(f"Error: {e}")
        elif OPERATING_SYSTEM == "Linux":  # Not tested
            # OPERATING_SYSTEM can return a specific Linux distribution
            # Just need to change the constant a little
            os.system("xdg-open " + self.sender().objectName())
        elif OPERATING_SYSTEM == "Darwin":  # macOS  # Not tested
            os.system("open " + self.sender().objectName())

    def open_folder_event(self):
        if OPERATING_SYSTEM == "Windows":
            try:
                os.system('start ' + self.sender().objectName())
            except Exception as e:
                print(f"Error: {e}")

    def image_to_clipboard(self):
        if OPERATING_SYSTEM == "Windows":
            image = Image.open(self.sender().objectName())
            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()
            send_to_clipboard(win32clipboard.CF_DIB, data)
        elif OPERATING_SYSTEM == "Linux":  # Not added
            pass

    def text_to_clipboard(self):
        if OPERATING_SYSTEM == "Windows":
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(self.sender().objectName(), win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()
        elif OPERATING_SYSTEM == "Linux":  # Not added
            pass

    def delete_image_confirmation(self):
        confirmation = QMessageBox.question(self, 'Подтверждение удаления',
                                            'Вы уверены, что хотите удалить эту картинку?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.delete_image(self.sender())
        else:
            pass  # Maybe add later | Потом добавлю в следующей версии

    def delete_image(self, sender: QObject):
        if os.path.isfile(sender.objectName()):
            os.remove(sender.objectName())
        deleted_image_path = None
        for i in range(self.content_layout.count()):
            image_layout = self.content_layout.itemAt(i).layout()
            if image_layout and image_layout.itemAt(0).widget().accessibleName() == sender.objectName():
                deleted_image_path = image_layout.itemAt(0).widget().accessibleName()
                image_layout.itemAt(0).widget().deleteLater()
                image_layout.itemAt(1).widget().deleteLater()
                image_layout.deleteLater()
                break
        for i in range(len(self.pictures)):
            if self.pictures[i] == deleted_image_path:
                self.pictures.pop(i)
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    # splash.blockSignals(True)  # Trying to block signals so the splash doesn't crash, but it doesn't work :(
    if not os.path.exists("images/screens"):
        os.makedirs("images/screens")
    app_icon = QIcon(f"{pathlib.Path(__file__).parent.absolute()}\\images\\images\\icon.png")
    system_tray = QSystemTrayIcon(app_icon, parent=app)
    system_tray.setToolTip("ScreenTaker v1.0")
    main_window = MainPage(system_tray, app_icon)
    show_action = QAction("Show")
    quit_action = QAction("Exit")
    hide_action = QAction("Hide")
    show_action.triggered.connect(main_window.show)
    hide_action.triggered.connect(main_window.hide)
    quit_action.triggered.connect(qApp.quit)
    tray_menu = QMenu()
    tray_menu.addAction(show_action)
    tray_menu.addAction(hide_action)
    tray_menu.addAction(quit_action)
    tray_menu.addAction(quit_action)
    system_tray.setContextMenu(tray_menu)
    splash.close()
    system_tray.show()
    main_window.show()
    sys.exit(app.exec_())
