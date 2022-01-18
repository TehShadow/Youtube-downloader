from os import path
from time import sleep
from tkinter import BooleanVar, Button,  Checkbutton, Entry, Label, OptionMenu,  StringVar, Tk
from tkinter.constants import FALSE, TRUE
from ydownload import Video
import threading
FONT_NAME = "Courier"
quality_choices = {"1080p","720p","480p","360p"}
DEFAULT_SAVE = R"G:\Videos"
thread_list = []

def worker():
    passVideoData()
    sleep(10)

def StartThread():
    try:
        x = threading.Thread(target=worker)
        thread_list.append(x)
        x.start()
    except:
        print("Something went wrong")

def passVideoData():
    if(path_to_save_box == ""):
       path_to_save = DEFAULT_SAVE
    else:
        path_to_save = path_to_save_box.get()
    data = Video()
    sound_test=sound.get()
    url=url_box.get()
    quality=tkvar.get()
    data.url = url
    data.sound = sound_test
    data.quality = quality
    data.path_to_save = path_to_save
    data.download()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Youtube Downloader")

url_Label = Label(text="Download URL:",highlightthickness=0,font=(FONT_NAME,12,"bold"))
url_Label.grid(column=0,row=1)

url_box = Entry(width=35)
url_box.grid(column=1,row=1,columnspan=1)

path_to_save_label = Label(text="Path to save file:",highlightthickness=0,font=(FONT_NAME,12,"bold"))
path_to_save_label.grid(column=0,row=2)

path_to_save_box = Entry(width=35)
path_to_save_box.grid(column=1,row=2,columnspan=1)

tkvar = StringVar()
tkvar.set("720p")
popupMenu = OptionMenu(window, tkvar, *quality_choices)
Label(window, text="Choose a quality: ").grid(row = 3, column = 0)
popupMenu.grid(row = 3, column = 1)


sound = BooleanVar()
sound_only = Checkbutton(window,text="Sound_only",variable=sound,onvalue=TRUE,offvalue=FALSE)
sound_only.grid(row=3 , column=2)

download_btn = Button(text="Download",command=StartThread,width=20)
download_btn.grid(column=1,row=4)

window.mainloop()
