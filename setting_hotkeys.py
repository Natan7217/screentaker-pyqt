from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QLabel, QPushButton, QMessageBox
from stylesheets import hotkey_dialog_stylesheet
import json
import keyboard


class HotkeyConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Конфигурация горячих клавиш")
        self.setGeometry((self.screen().size().width() - 500) // 2, (self.screen().size().height() - 600) // 2,
                         500, 600)
        self.layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_content = QDialog(self)
        self.scroll_content_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        self.layout.addWidget(self.scroll_area)

        # Hotkey configuration data (name and default hotkey) / Считываем json с горячими клавишами и
        # названиями действий
        with open("config.json", "r", encoding='utf-8') as f:
            self.hotkeys = json.load(f)

        self.hotkey_buttons = []
        # Create hotkey buttons for each action  | Создание кнопок для смены горячих клавиш для каждого действия
        for hotkey_data in self.hotkeys:
            label = QLabel(hotkey_data['name'], self.scroll_content)
            button = QPushButton(f"Установить горячие клавиши (Сейчас: {hotkey_data['hotkey']})", self.scroll_content)
            button.clicked.connect(lambda _, idx=hotkey_data: self.set_hotkey(idx))
            self.scroll_content_layout.addWidget(label)
            self.scroll_content_layout.addWidget(button)
            self.hotkey_buttons.append(button)

        save_button = QPushButton("Сохранить", self)  # Save button | Создание кнопки сохранения
        save_button.clicked.connect(self.save_config)
        self.layout.addWidget(save_button)

        self.setStyleSheet(hotkey_dialog_stylesheet)

    def set_hotkey(self, hotkey_data):
        # Set hotkey for the selected action / Получаем горячую клавишу и устанавливаем ее
        hotkey = keyboard.read_hotkey(suppress=False)
        self.sender().setText(f"Поменять (Было: {hotkey_data['hotkey']} Сейчас: {hotkey})")
        hotkey_data["hotkey"] = hotkey

    def save_config(self):
        # Save the hotkeys to a JSON file / Сохраняем горячие клавиши в json
        config_data = [{"name": hotkey_data["name"], "hotkey": hotkey_data["hotkey"]} for hotkey_data in self.hotkeys]
        for i in range(len(self.hotkey_buttons)):
            self.hotkey_buttons[i].setText(f"Установить горячие клавиши (Сейчас: {config_data[i]['hotkey']})")
        with open("config.json", "w", encoding='utf-8') as config_file:
            json.dump(config_data, config_file, indent=4)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Изменения будут применены при перезапуске")
        msg_box.setText("Изменения успешно сохранены. Пожалуйста, перезапустите приложение, чтобы они вступили в силу.")
        msg_box.exec_()
