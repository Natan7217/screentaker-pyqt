from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from stylesheets import about_program_stylesheet
import json

with open('info.json', 'r') as file:
    data = json.load(file)
    VERSION = data["version"]


class AboutScreenTakerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("О программе ScreenTaker")
        self.setGeometry((self.screen().size().width() - 450) // 2, (self.screen().size().height() - 250) // 2,
                         450, 250)
        self.setFixedSize(450, 250)

        layout = QVBoxLayout()

        about_label = QLabel("ScreenTaker - это программа для захвата скриншотов.")
        version_label = QLabel(f"Версия: {VERSION}")
        developer_label = QLabel("Разработчик: <a href='https://github.com/Natan7217'>@natandev</a>")
        developer_label.setOpenExternalLinks(True)
        website_label = QLabel("<a href='https://github.com/Natan7217/screentaker-pyqt'>Ссылка на проект</a>")
        website_label.setOpenExternalLinks(True)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)

        layout.addWidget(about_label)
        layout.addWidget(version_label)
        layout.addWidget(developer_label)
        layout.addWidget(website_label)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setStyleSheet(about_program_stylesheet)
