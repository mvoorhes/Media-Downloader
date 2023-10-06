import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sc
import ytdl

# Constants
BACKGROUND = 'blue'

# Create & initialize window
window = tk.Tk()
window.title('Internet Media Downloader')
window.configure(bg=BACKGROUND)
window.geometry("700x200")
window.minsize(700, 200)
window.maxsize(700, 200)

# Variables to change
dType = tk.StringVar()
lType = tk.StringVar()
link = tk.StringVar()

OPATH = 'Videos'

def download_link():
    temp = link.get()
    dt = dType.get()
    lt = lType.get()

    window.directory = filedialog.askdirectory()
    print(window.directory)
    if not window.directory:
        window.directory = OPATH
        print("Using default directory: ", window.directory)


    if lt == 'Soundcloud':
        print("Downloading Soundcloud Link")
        if sc.download(temp, window.directory):
            print("Download Successful")
            messagebox.showinfo("Download Successful", "Enjoy Your Audio")
        else:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR", "Could not download audio")
    else:
        print("Downloading Youtube Link")
        if ytdl.Download(temp, dt, opath=window.directory):
            print("Download Successful")
            messagebox.showinfo("Download Successful", "Enjoy Your Video")
        else:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR", "Could not download video")

# Labels
entry_label = tk.Label(
    window, 
    text = 'Link Here',
    bg=BACKGROUND,
    font=('calibre',20,'bold')
)
download_type = tk.Label(
    window,
    text='Download Type',
    bg=BACKGROUND,
    font=('calibre',15)
)
link_type = tk.Label(
    window,
    text='Link Type',
    bg=BACKGROUND,
    font=('calibre',15)
)

# Inputs
entry = tk.Entry(
    window,
    width=50,
    textvariable=link
)
button = tk.Button(
    window,
    bg=BACKGROUND,
    text="Download",
    command=download_link
)
option_mp3 = tk.Radiobutton(
    window,
    bg=BACKGROUND,
    text="mp3",
    variable=dType,
    value='mp3'
)
option_mp4 = tk.Radiobutton(
    window,
    bg=BACKGROUND,
    text='mp4',
    variable=dType,
    value='mp4'
)
option_yt = tk.Radiobutton(
    window,
    bg=BACKGROUND,
    text='YouTube',
    variable=lType,
    value='YouTube'
)
option_sc = tk.Radiobutton(
    window,
    bg=BACKGROUND,
    text='Soundcloud',
    variable=lType,
    value='Soundcloud'
)

# Positioning Everything
entry_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
download_type.grid(row=1, column=0)
option_mp3.grid(row=2, column=0)
option_mp4.grid(row=3, column=0)
link_type.grid(row=1, column=1)
option_yt.grid(row=2, column=1)
option_sc.grid(row=3, column=1)

window.mainloop()