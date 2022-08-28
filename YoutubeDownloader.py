#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# GUI
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import YoutubeDownloader as yt

# Basic window
root_window = tk.Tk()
root_window.geometry("550x120")
root_window.resizable(False, False)
root_window.title("Youtube Video Downloader")

# Some function
url_label = tk.Label(root_window, text='Youtube URL:')
url_label.grid(row=0, column=0)
url_entry = tk.Entry(root_window, width=50)
url_entry.grid(row=0, column=1)

output_label = tk.Label(root_window, text='Output path:')
output_label.grid(row=1, column=0)
output_entry = tk.Entry(root_window, width=50)
output_entry.grid(row=1, column=1)

def choose_file():
    dirname = fd.askdirectory(title='Choose directory')
    output_entry.insert('0', dirname)

choose_file_button = tk.Button(
    root_window,
    text='Choose',
    command=choose_file
)
choose_file_button.grid(row=1, column=3)



from pytube import YouTube

def yt_download():
    links_list = [url_entry.get()]
    output_path = output_entry.get()
    for i in range(len(links_list)):
        yt = YouTube(links_list[i])
        title = yt.title
        title = ''.join(e for e in title if e.isalnum())
        # title = ""
        print("Title:", title, ", URL:", links_list[i])
        yt_highest_quality = yt.streams.get_highest_resolution()
        yt_highest_quality.download(output_path)        
    tk.messagebox.showinfo(title = 'Done!', message = "OK")

    
start_button = tk.Button(root_window, text="Download", command=yt_download)
start_button.grid(row=2, column=0, columnspan=2)
close_button = tk.Button(root_window, text="Close the window", command=root_window.quit)
close_button.grid(row=3, column=0, columnspan=2)

# Run it
root_window.mainloop() 


