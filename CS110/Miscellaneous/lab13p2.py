# lab 13 part 2
# main header in part 1

import webbrowser
from time import sleep

# Song class
class Song():
    # Constructor
    def __init__(self, title, url, duration):
        self.title = title
        self.url = url
        self.duration = duration

    # Methods
    def printInfo(self):
        print(self.title, '-', self.duration, '(' + self.url + ')')

    def play(self):
        webbrowser.open(self.url)
        time = self.duration.split(":")
        total_seconds = int(time[0]) * 60 + int(time[1])
        sleep(total_seconds)

# Playlist Manager class
class PlaylistManager():
    # Constructor
    def __init__(self):
        self.song_list = []

    #Methods
    def addSong(self, title, url, duration):
        song = Song(title, url, duration)
        self.song_list.append(song)

    def printAll(self):
        for i in range(len(self.song_list)):
            print(str(i + 1) + '.', end = ' ')
            self.song_list[i].printInfo()

    def playAll(self):
        for i in self.song_list:
            i.play()



# Test functions
def testSongPrintInfo():
    s1 = Song("Help","https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    s1.printInfo()

def testSongPlay():
    s1 = Song("Help", "https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    s1.play()

def testprintAll():
    plistm = PlaylistManager()
    plistm.addSong("Help","https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    plistm.addSong("Help", "https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    plistm.printAll()

def testplayAll():
    plistm = PlaylistManager()
    plistm.addSong("10 sec", "https://www.youtube.com/watch?v=rUWxSEwctFU", "0:09")
    plistm.addSong("Help", "https://www.youtube.com/watch?v=2Q_ZzBGPdqE", "02:19")
    plistm.playAll()

# Mian function
def main():
    # Instantiate PlaylistManager
    playlistMgr = PlaylistManager()
    keepGoing = ""
    while(keepGoing != "DONE"):

        # Ask for info about song
        title = input("Song title: ")
        url = input("YouTube video: ")
        duration = input("Video duration (MM:SS): ")

        playlistMgr.addSong(title,url,duration)

        keepGoing = input("Add another song? YES to continue, DONE to end: ")

    # Print all songs
    playlistMgr.printAll()

    # Play all songs
    playlistMgr.playAll()

# Calling main
if __name__ == "__main__":
    main()