import ssl
import tkinter
import customtkinter
from yt_dlp import YoutubeDL
from pathlib import Path
import re

def startDownload():
    try:
        ytLink = link.get()
        ssl._create_default_https_context = ssl._create_unverified_context
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(Path.home() / "Downloads/%(title)s.%(ext)s"),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [on_progress_hook],
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(ytLink, download=True)
            title.configure(text=info_dict['title'], text_color="white")
            finishLabel.configure(text=f"Downloaded and converted to MP3!\nSaved as: {info_dict['title']}.mp3")
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        finishLabel.configure(text="Error downloading video", text_color="red")

def on_progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = re.sub(r'\x1b\[[0-9;]*m', '', d['_percent_str']).strip()
        pPercentage.configure(text=f"{percent_str}")
        pPercentage.update()

        try:
            progressBar.set(float(percent_str.strip('%')) / 100)
        except ValueError:
            pass

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert Youtube URL")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()