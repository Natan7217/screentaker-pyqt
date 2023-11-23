from PIL import ImageGrab, Image

"""grab_image = ImageGrab.grab(
    bbox=None,
    include_layered_windows=False,
    all_screens=False,
    xdisplay=None
)
grab_image.show()"""
from io import BytesIO
import win32clipboard
from PIL import Image


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


filepath = 'C:\\Users\\naran\\OneDrive\\Документы\\GitHub\\screentaker-pyqt\\images\\images\\bg.jpg'
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)

"""For MacOS:

import os
os.system("open tmp.png") #Will open in Preview.
For most GNU/Linux systems with X.Org and a desktop environment:

import os
os.system("xdg-open tmp.png")
For Windows:

import os
os.system("powershell -c tmp.png")
"""
