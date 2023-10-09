import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sc
import ytdl
import constants as cs

class gui:
    def __init__(self):
        self.window = tk.Tk()
        self.name = 'Internet Media Downloader'
        self.width = cs.WIDTH
        self.height = cs.HEIGHT
        self.bg_color = cs.BACKGROUND
        self.download_type = tk.IntVar()
        self.link_type = tk.IntVar()
        self.link = tk.StringVar()
        self.resolution = tk.StringVar()

        # Labels
        self.entry_label = tk.Label(
            self.window,
            text='Link Here',
            bg=self.bg_color,
            font=(cs.FONT,20,'bold')
        )
        self.download_type_label = tk.Label(
            self.window,
            text='Download Type',
            bg=self.bg_color,
            font=(cs.FONT,15)
        )
        self.link_type_label = tk.Label(
            self.window,
            text='Link Type',
            bg=self.bg_color,
            font=(cs.FONT,15)
        )
        self.resolution_label = tk.Label(
            self.window,
            text='Resolution',
            bg=self.bg_color,
            font=(cs.FONT,15)
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
            text=cs.download_type.mp3.name,
            variable=self.download_type,
            value=cs.download_type.mp3.value
        )
        self.mp4 = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text=cs.download_type.mp4.name,
            variable=self.download_type,
            value=cs.download_type.mp4.value
        )
        self.yt = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text=cs.link_type.YouTube.name,
            variable=self.link_type,
            value=cs.link_type.YouTube.value
        )
        self.sc = tk.Radiobutton(
            self.window,
            bg=self.bg_color,
            text=cs.link_type.Soundcloud.name,
            variable=self.link_type,
            value=cs.link_type.Soundcloud.value
        )
        self.dropdown = tk.OptionMenu(
            self.window,
            self.resolution,
            *cs.options
        )

    def initialize_window(self):
        self.window.title(self.name)
        self.window.configure(bg=self.bg_color)
        self.window.minsize(self.width, self.height)
        self.window.maxsize(self.width, self.height)

    def set_initial_values(self):
        self.link_type.set(cs.link_type.YouTube.value)
        self.download_type.set(cs.download_type.mp3.value)
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
        self.resolution_label.grid(row=1, column=2)
        self.dropdown.grid(row=2, column=2)


    def print_message(self, download_status):
        if download_status == cs.error_types.SUCCESS:
            print("Download Successful")
            messagebox.showinfo("Download Successful", "Enjoy Your File")
        elif download_status == cs.error_types.VIDEO_BLOCKED:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR YOUTUBE", "Video/Audio is blocked either due to Age Restriction or Copyright Protection")
        elif download_status == cs.error_types.BAD_STREAM:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR YOUTUBE", "Could not download, but could access; Try again with different resolution")
        elif download_status == cs.error_types.INVALID_LINK:
            print("Link Invalid")
            messagebox.showerror("ERROR", "Invalid link; Submit a better link")
        elif download_status == cs.error_types.UNKNOWN:
            print("Download Unsuccessful")
            messagebox.showerror("ERROR", "Could not download video/audio for unknown reasons")
        elif download_status == cs.error_types.PLAYLIST_INCOMPLETE:
            print("Download partially successful")
            messagebox.showerror("ERROR", "Playlist download is partially complete; skipped some files due to a variety of reasons")


    def download_link(self):
        self.window.directory = filedialog.askdirectory()
        if not self.window.directory:
            self.window.directory = cs.OPATH

        if self.link_type.get() == cs.link_type.Soundcloud.value:
            print("Downloading Soundcloud Video")
            self.print_message(sc.download(self.link.get(), self.window.directory))
        else:
            print("Downloading YouTube Video")
            self.print_message(ytdl.Download(self.link.get(), self.download_type.get(), quality=self.resolution.get(), opath=self.window.directory))