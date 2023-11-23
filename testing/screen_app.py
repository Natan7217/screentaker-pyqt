from PIL import ImageGrab
import win32gui


toplist, winlist = [], []


def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


win32gui.EnumWindows(enum_cb, toplist)
firefox = [(hwnd, title) for hwnd, title in winlist if 'google' in title.lower()]
# just grab the hwnd for first window matching firefox
firefox = firefox[0]
hwnd = firefox[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox)
img.show()
