from .. import global_time
from win32con import KEYEVENTF_KEYUP
from win32api import keybd_event, MapVirtualKey
import time


def word_press(word, t=global_time):
    def key_press(key, t):
        vk_code = ord(key.upper())
        keybd_event(vk_code, MapVirtualKey(vk_code, 0), 0, 0)
        time.sleep(t)
        keybd_event(vk_code, MapVirtualKey(vk_code, 0), KEYEVENTF_KEYUP, 0)

    for char in word:
        key_press(char, t)
    key_press('\r', t)
