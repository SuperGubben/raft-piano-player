import play_song
import time as t


def main():
    songs = []
    for song in play_song.songs:
        songs.append(song)
    
    songNumber = 1
    for song in songs:
        print(f"{songNumber}. {song.capitalize()}")
        songNumber += 1
    
    try:
        songToPlayNumber = int(input("Choose song: ")) - 1
    except:
        print("invalid input")
        main()
    
    if songToPlayNumber in range(0, len(songs)+1):
        t.sleep(2)
        songToPlay = play_song.songs[songs[songToPlayNumber]]
        songToPlay() # play the song
        main()
    else:
        print("invalid input")
        main()


main()