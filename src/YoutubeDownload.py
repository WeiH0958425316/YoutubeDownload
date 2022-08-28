from pytube import YouTube

# from sys import argv

output_path = 'C:/Users/f0958/Downloads'

def yt_download():
    while True:
        # links_len = argv[1]
        links_len = input("How many video you want to download? ")
        links_len = int(links_len)
        links_list = []

        for i in range(links_len):
            link = input("Youtube Url(%s):" % str(i + 1))
            if len(link) == 0:
                continue
            links_list.append(link)
        # print(links_list)

        print("Downloading...")
        for i in range(len(links_list)):
            yt = YouTube(links_list[i])
            title = yt.title
            title = ''.join(e for e in title if e.isalnum())
            # title = ""
            print("Title:", title, ", URL:", links_list[i])
            yt_highest_quality = yt.streams.get_highest_resolution()
            yt_highest_quality.download(output_path)

        print("All finished\n")
        re_run = ""
        while re_run not in ["Y", "N"]:
            re_run = input("Download another?(Y/N)").upper()

        if re_run != "Y":
            break

if __name__ == '__main__':
    yt_download()