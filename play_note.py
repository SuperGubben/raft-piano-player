from pynput.keyboard import Key, Controller
import time as t

kb = Controller()

def hold_note(key: str, length: int = 600, tone: int = 0):
    print(f"pressing {key} for {length}ms with tone {tone}")

    if tone == -1:
        kb.press(Key.space)
    if tone == 1:
        kb.press(Key.shift)

    kb.press(key)

    t.sleep(length/1000)

    kb.release(key)

    kb.release(Key.space)
    kb.release(Key.shift)

def short_note(key: str, length: int = 600, tone: int = 0): #key: the key you want to play. length: how long you want to wait after playing another note. tone: high or low octave
    print(f"pressing {key} for {length}ms with tone {tone}")

    if tone == -1:
        kb.press(Key.space)
    if tone == 1:
        kb.press(Key.shift)

    kb.press(key)
    kb.release(key)

    kb.release(Key.space)
    kb.release(Key.shift)

    t.sleep(length/1000)