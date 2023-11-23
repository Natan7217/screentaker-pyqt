import time
import ctypes
import win32api
import win32con


def screen_off():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)


def screen_on():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
    move_cursor()


def move_cursor():
    x, y = (0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)


# screen_on()
# time.sleep(3)
# screen_off()
