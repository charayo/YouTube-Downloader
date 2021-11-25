from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Ayodeji-youtube video downloader")
Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()
Label(root, text='by Ayodeji', font='arial 15 bold').pack()
link = StringVar()

Label(root, text='Oya Paste Copied Youtube Link Here:', font='arial 15').pack()
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=110)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=downloader).place(x=180,
                                                                                                            y=150)

root.mainloop()
