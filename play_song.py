import time as t
import play_note

def raft_song():

    play_note.long_note('7')
    play_note.long_note('6')
    play_note.long_note('7')
    play_note.long_note('3')
    play_note.long_note('5')
    play_note.long_note('6')

    t.sleep(1.2)

    play_note.long_note('7')
    play_note.long_note('6')
    play_note.long_note('7')
    play_note.long_note('3')
    play_note.long_note('5')
    play_note.long_note('6')

    t.sleep(1.2)

    play_note.long_note('7')
    play_note.long_note('6')
    play_note.long_note('5')
    play_note.long_note('3', length = 2000)

    t.sleep(1.2)

    play_note.long_note('7')
    play_note.long_note('6')
    play_note.long_note('5')
    play_note.long_note('3', length = 2000)


def chinese():
    length = 150
    length2 = 350

    play_note.short_note('7', length=length)
    play_note.short_note('7', length=length)
    play_note.short_note('7', length=length)
    play_note.short_note('7', length=length)
    play_note.short_note('6', length=length2)
    play_note.short_note('6', length=length2)
    play_note.short_note('5', length=length2)
    play_note.short_note('5', length=length2)
    play_note.long_note('6', length=1500)


def test():
    play_note.long_notes('2', '3', '5', '6', '9')

def minecraft():
    short_length = 800
    long_length = 1200

    play_note.long_notes('1', '0', length=long_length, tone=-1)
    play_note.long_notes('2', '9', length=short_length, tone=-1)
    play_note.long_notes('4', '8', length=long_length, tone=-1)
    play_note.long_notes('3', '9', length=long_length, tone=-1)

    t.sleep(0.3)

    play_note.long_notes('1', '0', length=long_length, tone=-1)
    play_note.long_notes('2', '9', length=short_length, tone=-1)
    play_note.long_notes('4', '8', length=long_length, tone=-1)
    play_note.long_notes('4', '7', length=long_length, tone=-1)


songs = {
    "raft": raft_song,
    "chinese": chinese,
    "minecraft": minecraft,
    "test": test
}