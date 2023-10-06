import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sc
import ytdl
import constants as cs

OPATH = ''

class gui:
    def __init__(self):
        self.window = tk.Tk()
        self.name = 'Internet Media Downloader'
        self.width = 700
        self.height = 200
        self.bg_color = cs.BACKGROUND
        self.download_type = tk.StringVar()
        self.link_type = tk.StringVar()
        self.link = tk.StringVar()
        self.resolution = tk.StringVar()

        # Labels
        self.entry_label = tk.Label(
            self.window,
            text='Link Here',
            bg=self.bg_color,
            font=('calibre',20,'bold')
        )
        self.download_type_label = tk.Label(
            self.window,
            text='Download Type',
            bg=self.bg_color,
            font=('calibre',15)
        )
        self.link_type_label = tk.Label(
            self.window,
            text='Link Type',
            bg=self.bg_color,
            font=('calibre',15)
        )

        # Buttons
        self.entry = tk.Entry(
            self.window,
            width=50,
            textvariable=self.link
        )
        self.download_button = tk.Button(
            self.window,
            bg=self.bg_color,
            text="Download",
            command=self.download_link
        )
        self.mp3 = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text='mp3',
            variable=self.download_type,
            value='mp3'
        )
        self.mp4 = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text='mp4',
            variable=self.download_type,
            value='mp4'
        )
        self.yt = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text='YouTube',
            variable=self.link_type,
            value='YouTube'
        )
        self.sc = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text='Soundcloud',
            variable=self.link_type,
            value='Soundcloud'
        )

    def initialize_window(self):
        self.window.title(self.name)
        self.window.configure(bg=self.bg_color)
        self.window.minsize(self.width, self.height)
        self.window.maxsize(self.width, self.height)

    def set_initial_values(self):
        self.link_type.set('YouTube')
        self.download_type.set('mp3')
        self.resolution.set('720p')

    def position(self):
        self.entry_label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.download_button.grid(row=0, column=2)
        self.download_type_label.grid(row=1, column=0)
        self.mp3.grid(row=2, column=0)
        self.mp4.grid(row=3, column=0)
        self.link_type_label.grid(row=1, column=1)
        self.yt.grid(row=2, column=1)
        self.sc.grid(row=3, column=1)


    def print_message(self, download_status):
        if download_status:
            print("Download Successful")
            messagebox.showinfo("Download Successful", "Enjoy Your File")
        else:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR", "Could not download file")


    def download_link(self):
        self.window.directory = filedialog.askdirectory()
        if not self.window.directory:
            self.window.directory = OPATH

        if self.link_type.get() == 'Soundcloud':
            print("Downloading Soundcloud Video")
            self.print_message(sc.download(self.link.get(), self.window.directory))
        else:
            print("Downloading YouTube Video")
            self.print_message(ytdl.Download(self.link.get(), self.download_type.get(), opath=self.window.directory))