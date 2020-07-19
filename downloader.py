from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import *

root = Tk()
root.title('YouTube Downloader')
root.geometry('600x150')
root.iconbitmap('images/youtube-dl.ico')

lbl_entry = Label(root, text="Enter Url:").grid(row=0,column=0,padx=5,pady=5)
ent = ttk.Entry(root,width=60)
ent.grid(row=0,column=1,padx=10,pady=5)

def downloader():
    entry = ent.get()
    yt = YouTube(entry,)
    dl = yt.streams.first().download()
    if dl:
        lbl_percent.config(text="Please wait...",fg="red")
        messagebox.showinfo('Download Info','Download successful')
        lbl_percent.config(text="Completed!!",fg="green")
    else:
        messagebox.showerror('Download Info','Download Failed!!')
        

# def threader():
#     thread = Thread(target=downloader)
#     thread.start()

ttk.Button(root,text="Download",command=downloader).grid(row=0,column=2,padx=5,pady=10)
lbl_percent = Label(root,text="")
lbl_percent.grid(row=1,column=0,columnspan=2,padx=20,pady=5)

root.mainloop()

