#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created: 2022/08/28
Version: 2022/08/28
@Author: Huang, Wei
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import src.YoutubeDownload as yt


# GUI
# Basic window
root_window = tk.Tk()
root_window.geometry("500x100")
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


def do_download():
    status = yt.yt_download([url_entry.get()], output_entry.get())
    tk.messagebox.showinfo(title = 'Done!', message = "OK")

start_button = tk.Button(root_window, text="Download", command=do_download)
start_button.grid(row=2, column=0, columnspan=2)
close_button = tk.Button(root_window, text="Close the window", command=root_window.quit)
close_button.grid(row=3, column=0, columnspan=2)

# Run it
root_window.mainloop() 



