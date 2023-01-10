import tkinter as tk
import os
import fnmatch

from pygame import mixer


canvas = tk.Tk()
canvas.title("Patrimoine Player")
canvas.geometry("500x500")
canvas.config(bg='white')

rootpath = "C:\\Users\OzLaptops\Music\demo"
pattern = "*.mp3"

mixer.init()

prec_img=tk.PhotoImage(file="prev.png")
stop_img=tk.PhotoImage(file="stop.png")
play_img=tk.PhotoImage(file="play.png")
pause_img=tk.PhotoImage(file="pause.png")
next_img=tk.PhotoImage(file="next.png")


def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+ listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def suiv():

    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)

    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def prec():

    prec_song = listbox.curselection()
    prec_song = prec_song[0]-1
    prec_song_name = listbox.get(prec_song)

    label.config(text=prec_song_name)

    mixer.music.load(rootpath + "\\" + prec_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(prec_song)
    listbox.select_set(prec_song)

def pause():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"


listbox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('poppin', 14'))
listbox.pack(padx=15, pady=15)

label = tk.label(canvas, text="", bg='white', fg='black', font=('poppin', 18))
label.pack(pady=15)



top = tk.Frame(canvas, bg='white')
top.pack(padx=10, pady=5, anchor='center')



precButton = tk.Button(canvas, text="prec", image=prec_img, bg='white', borderwidth=0, command=prec)
precButton.pack(pady=15, in_=top, side=LEFT)

stopButton = tk.Button(canvas, text="stop", image=stop_img, bg='white', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side=LEFT)

playButton = tk.Button(canvas, text="play", image=play_img, bg='white', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side=LEFT)

pauseButton = tk.Button(canvas, text="pause", image=pause_img, bg='white', borderwidth=0, command=pause)
pauseButton.pack(pady=15, in_=top, side=LEFT)

nextButton = tk.Button(canvas, text="next", image=next_img, bg='white', borderwidth=0, command=suiv)
nextButton.pack(pady=15, in_=top, side=LEFT)


for root, dirs, files in os.walk(rootpath):

    for filename in fnmatch.filter(files,pattern):

        listbox.insert('end', filename)

canvas.mainloop()