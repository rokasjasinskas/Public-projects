import keyboard
import os

def close_windows():
    os.system("pkill -f 'python'")

keyboard.add_hotkey("ctrl+alt+c", close_windows)
keyboard.wait()
