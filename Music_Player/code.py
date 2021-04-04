
# The * command means we are importing all stuffs from Tkinter.
from tkinter import *
import pygame
import os

from time import strftime
window = Tk()

#Below command will initialize songs in our music player
pygame.mixer.init()
n=0

def start_stop():
    global n
    n = n+1
    if n==1:
        song_name = songs_listbox.get()
        pygame.mixer.music.load(song_name)

        #If we want to repeat our song then use this command -> "pygame.mixer.music.play(-1)". 
        pygame.mixer.music.play(0)
    elif (n%2)==0:
        pygame.mixer.music.pause()
    
    elif(n%2)!=0:
        pygame.mixer.music.unpause()

l1 = Label(window, text ="MUSIC PLAYER", font ="times 20")
l1.grid(row=1, column=1)

#This code is for the buttons for start and stop.
b2 = Button(window, text='o', command=start_stop)
b2.grid(row=4, column=1)

songs_list = os.listdir()

#This command will show a list of all the songs from where we can choose our desired music to play!
songs_listbox = StringVar(window)

songs_listbox.set("Select Songs")
menu = OptionMenu(window, songs_listbox, *songs_list)
menu.grid(row=4, column=4)
window.mainloop()
