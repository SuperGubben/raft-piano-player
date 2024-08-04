from pynput.keyboard import Key, Controller
import time as t

kb = Controller()

def play_note(key: str, length: int = 600, tone: int = 0, instant: bool = False):
    print(f"pressing {key} for {length}ms with tone {tone}")

    if tone == -1:
        kb.press(Key.space)
    if tone == 1:
        kb.press(Key.shift)

    kb.press(key)

    if not instant:
        t.sleep(length/1000)

    kb.release(key)

    kb.release(Key.space)
    kb.release(Key.shift)

    if instant:
        t.sleep(length/1000)