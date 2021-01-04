from ctypes import windll

import win32


from ctypes import windll

width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)
print(width, height)

windll.user32.SetCursorPos(x, y)