#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pytube import YouTube

# output_path = 'C:/Users/f0958/Downloads'



def yt_ask_url():
    links_len = input("How many video you want to download? ")
    links_len = int(links_len)
    links_list = []

    for i in range(links_len):
        link = input("Youtube Url(%s):" % str(i + 1))
        if len(link) == 0:
            continue
        links_list.append(link)
    return links_list

def yt_ask_output_path():
    output_path = input("Where you want to storage videos? ")
    return output_path

def yt_download(links_list, output_path):
    for i in range(len(links_list)):
        yt = YouTube(links_list[i])
        title = yt.title
        title = ''.join(e for e in title if e.isalnum())
        # title = ""
        print("Title:", title, ", URL:", links_list[i])
        yt_highest_quality = yt.streams.get_highest_resolution()
        yt_highest_quality.download(output_path)
    return "Done"


def main():
    while True:
        links_list = yt_ask_url()
        output_path = yt_ask_output_path()

        print("Downloading...")
        yt_download(links_list, output_path)
        print("All finished\n")

        re_run = ""
        while re_run not in ["Y", "N"]:
            re_run = input("Download another?(Y/N)").upper()

        if re_run != "Y":
            break


if __name__ == '__main__':
    main()