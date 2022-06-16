#functionality modules
import vlc
import time

#gui modules
import tkinter
from tkinter import *

#template music player function
def template():

    vlcInstance = vlc.Instance()

    player = vlcInstance.media_player_new()

    media = vlcInstance.media_new("01 Kalimba.mp3")

    player.set_media(media)

    player.play()

    time.sleep(0.5)

    duration = player.get_length()

    print(duration)

    time.sleep(duration)

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
        playButton = tkinter.Button(mediaControlsBG, text="PLAY", command=template).place(relx=0.5, rely=0.5, anchor=CENTER)

        screen.mainloop()
    
    GUI()

__main__()