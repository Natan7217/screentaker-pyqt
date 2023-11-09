vertical_scroll_bar_stylesheet = """
QScrollBar:vertical {
    border: none;
    background: rgb(45, 45, 68);
    width: 14px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {
    background-color: rgb(80, 80, 122);
    min-height: 30px;
    border-radius: 7px;
}
QScrollBar::handle:vertical:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::handle:vertical:pressed {
    background-color: rgb(185, 0, 92);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
    border: none;
    background-color: rgb(59, 59, 90);
    height: 15px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::sub-line:vertical:pressed {
    background-color: rgb(185, 0, 92);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
    border: none;
    background-color: rgb(59, 59, 90);
    height: 15px;
    border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:vertical:pressed {
    background-color: rgb(185, 0, 92);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
"""
horizontal_scroll_bar_stylesheet = """
QScrollBar:horizontal {
    border: none;
    background: rgb(45, 45, 68);
    height: 14px;
    margin: 0 15px 0 15px;
    border-radius: 0px;
}

QScrollBar::handle:horizontal {
    background-color: rgb(80, 80, 122);
    min-height: 30px;
    border-radius: 7px;
}
QScrollBar::handle:horizontal:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::handle:horizontal:pressed {
    background-color: rgb(185, 0, 92);
}

QScrollBar::add-line:horizontal {
    border: none;
    background-color: rgb(59, 59, 90);
    width: 15px;
    border-top-right-radius: 7px;
    border-bottom-right-radius: 7px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    margin: 0px 3px 0px 3px;
}

QScrollBar::add-line:horizontal:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:horizontal:pressed {
    background-color: rgb(185, 0, 92);
}

QScrollBar::sub-line:horizontal {
    border: none;
    background-color: rgb(59, 59, 90);
    width: 15px;
    border-top-left-radius: 7px;
    border-bottom-left-radius: 7px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    margin: 0px 3px 0px 3px;
}


QScrollBar::sub-line:horizontal:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::sub-line:horizontal:pressed {
    background-color: rgb(185, 0, 92);
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
"""

about_program_stylesheet = """
QDialog {
    background: qradialgradient(cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 0.7, stop: 0 white, stop: 1 #4CAF50);
    border: 2px solid #4CAF50;
    border-radius: 10px;
}
QLabel {
    font-size: 16px;
    margin-bottom: 10px;
}
QPushButton {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #45a049, stop: 1 #4CAF50);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
}
QPushButton:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4CAF50, stop: 1 #45a049);
}
"""

hotkey_dialog_stylesheet = """
QDialog {
    background-color: rgb(39, 39, 39);
}
QScrollArea, QLineEdit, QPushButton {
    background-color: #333;
    color: #fff;
    border: 1px solid #666;
    padding: 5px;
}
QPushButton {
    background-color: #4caf50;
    color: white;
    font-weight: bold;
    font-size: 12px;
    border: none;
    padding: 5px 15px;
}
QLabel {
    color: #fff;
    font-weight: bold;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #45a848;
}
"""
