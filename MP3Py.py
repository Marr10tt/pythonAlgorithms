#functionality modules
import vlc
import time
import threading

#gui modules
import tkinter
from tkinter import *
from tkinter import ttk #use for table to display songs

#thread creation template
class mediaThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    vlcInstance = vlc.Instance()
    #media player instance
    player = vlcInstance.media_player_new()
    player.audio_set_volume(50)

    #function to play media
    def mediaPlayerPlay(self, fileName):
        media = self.vlcInstance.media_new(fileName)
        self.player.set_media(media)
        
        self.player.play()
        time.sleep(0.5)
    
    def mediaPlayerPause(self):
        self.player.pause()
    
    def mediaPlayerVolUp(self):
        currentVolume = self.player.audio_get_volume()
        if currentVolume < 100:
            self.player.audio_set_volume(currentVolume+10)
    
    def mediaPlayerVolDown(self):
        currentVolume = self.player.audio_get_volume()
        if currentVolume > 0:
            self.player.audio_set_volume(currentVolume-10)

    def run(self):
        print ("Starting " + self.name)




def __main__():
    def GUI():
        screen = tkinter.Tk()
        screen.geometry("1440x845")
        screen.title("musipy")
        screen.config(bg="#333b40")
        screen.resizable(False, False)

        #a background to display all media player related items (image, sliders, pause, play, etc)
        mediaPlayerBG = tkinter.Frame(bg="#5a6268", height=845, width=400)
        mediaPlayerBG.place(relx=0.14, rely=0.5, anchor=CENTER)

        #a frame for the music functionality (pause, play, etc)
        mediaControlsBG = tkinter.Frame(mediaPlayerBG, bg="#495056", height=335, width=400)
        mediaControlsBG.place(relx=0.5, rely=0.6, anchor=N)

        #functionality test
        musicThread = mediaThread(1, "Music thread", 1)
        playButton = tkinter.Button(mediaControlsBG, text="PLAY", command=lambda:[musicThread.mediaPlayerPlay("01 Kalimba.mp3")]).place(relx=0.5, rely=0.5, anchor=CENTER)
        pauseButton = tkinter.Button(mediaControlsBG, text="PAUSE", command=musicThread.mediaPlayerPause).place(relx=0.5, rely=0.6, anchor=CENTER)
        volUp = tkinter.Button(mediaControlsBG, text="VOLUME UP", command=musicThread.mediaPlayerVolUp).place(relx=0.7, rely=0.55, anchor=CENTER)
        volDown = tkinter.Button(mediaControlsBG, text="VOLUME DOWN", command=musicThread.mediaPlayerVolDown).place(relx=0.3, rely=0.55, anchor=CENTER)

        screen.mainloop()
    
    GUI()

__main__()