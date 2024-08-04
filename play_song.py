import time as t
import play_note

def raft_song():

    play_note.hold_note('7')
    play_note.hold_note('6')
    play_note.hold_note('7')
    play_note.hold_note('3')
    play_note.hold_note('5')
    play_note.hold_note('6')

    t.sleep(1.2)

    play_note.hold_note('7')
    play_note.hold_note('6')
    play_note.hold_note('7')
    play_note.hold_note('3')
    play_note.hold_note('5')
    play_note.hold_note('6')

    t.sleep(1.2)

    play_note.hold_note('7')
    play_note.hold_note('6')
    play_note.hold_note('5')
    play_note.hold_note('3', length = 2000)

    t.sleep(1.2)

    play_note.hold_note('7')
    play_note.hold_note('6')
    play_note.hold_note('5')
    play_note.hold_note('3', length = 2000)


def chinese():
    length = 200
    length2 = 400

    play_note.hold_note('7', length=length, instant=True)
    play_note.hold_note('7', length=length, instant=True)
    play_note.hold_note('7', length=length, instant=True)
    play_note.hold_note('7', length=length, instant=True)
    play_note.hold_note('6', length=length2, instant=True)
    play_note.hold_note('6', length=length2, instant=True)
    play_note.hold_note('5', length=length2, instant=True)
    play_note.hold_note('5', length=length2, instant=True)
    play_note.hold_note('6', length=1500)





songs = {
    "raft": raft_song,
    "chinese": chinese
}