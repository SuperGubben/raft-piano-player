import asyncio
from pynput.keyboard import Key, Controller
import time as t

kb = Controller()

def long_note(key: str, length: int = 600, tone: int = 0, debug: bool = False):
    if debug:
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

def short_note(key: str, length: int = 600, tone: int = 0, debug: bool = False): #key: the key you want to play. length: how long you want to wait after playing another note. tone: high or low octave
    if debug:
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

def long_notes(*keys: str, length: int = 600, tone: int = 0, debug: bool = False):
    if debug:
        print(f"pressing {keys} for {length}ms with tone {tone}")
    
    if tone == -1:
        kb.press(Key.space)
    if tone == 1:
        kb.press(Key.shift)
    
    for key in keys:
        kb.press(key)
    
    t.sleep(length/1000)

    for key in keys:
        kb.release(key)

    kb.release(Key.space)
    kb.release(Key.shift)

def short_notes(*keys: str, length: int = 600, tone: int = 0, debug: bool = False):
    if debug:
        print(f"pressing {keys} for {length}ms with tone {tone}")
    
    if tone == -1:
        kb.press(Key.space)
    if tone == 1:
        kb.press(Key.shift)
    
    for key in keys:
        kb.press(key)
    
    for key in keys:
        kb.release(key)

    kb.release(Key.space)
    kb.release(Key.shift)

    t.sleep(length/1000)