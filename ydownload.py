from pytube import YouTube
from tkinter import messagebox

class Video():
    def __ini__(self , url , sound , quality ,path_to_save):
        self.url = url
        self.path_to_save = path_to_save
        self.sound = sound
        self.quality = quality
    
    def download(self):
        try:
            print(self.sound)
            print(self.url)
            print(self.quality)
            print(self.path_to_save)
            yt = YouTube(self.url)
            if self.sound == True:
                yt.streams.filter(only_audio=True)
                data = yt.streams.get_by_itag(140)
            else:
                yt.streams.filter(file_extension="mp4")
                print(yt.streams.filter(file_extension="mp4"))
                if self.quality == "720p":
                    data = yt.streams.get_by_itag(22)
                elif self.quality == "1080p":
                    data = yt.streams.get_by_itag(137)
                elif self.quality == "360p":
                    data = yt.streams.get_by_itag(18)
                else:
                    data = yt.streams.get_by_itag(135)
                    
                
            data.download(output_path=self.path_to_save)
            messagebox.showinfo("Results",message=f"File : {yt.title}\nSuccefully downloaded at :{self.path_to_save}")
        except:
            messagebox.showinfo("Results",message="Something went wrong")
            print("Something went wrong")