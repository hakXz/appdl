import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
from yt_dlp import YoutubeDL


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("500x450")
        self.resizable(False, False)

        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="MP4")
        self.resolution_var = tk.StringVar()
        self.fps_var = tk.StringVar()
        self.path_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Idle")

        self.available_formats = {}

        self.build_ui()

    def build_ui(self):
        padding = {"padx": 10, "pady": 5}

        tk.Label(self, text="Video URL (YouTube / Twitter)").pack(anchor="w", **padding)
        tk.Entry(self, textvariable=self.url_var, width=60).pack(**padding)

        tk.Button(self, text="Fetch Formats", command=self.fetch_formats).pack(**padding)

        tk.Label(self, text="Format").pack(anchor="w", **padding)
        ttk.Combobox(
            self,
            textvariable=self.format_var,
            values=["MP4", "MP3"],
            state="readonly"
        ).pack(**padding)

        self.res_label = tk.Label(self, text="Resolution (YouTube)")
        self.res_label.pack(anchor="w", **padding)
        self.resolution_box = ttk.Combobox(self, textvariable=self.resolution_var, state="readonly")
        self.resolution_box.pack(**padding)

        self.fps_label = tk.Label(self, text="FPS")
        self.fps_label.pack(anchor="w", **padding)
        self.fps_box = ttk.Combobox(self, textvariable=self.fps_var, state="readonly")
        self.fps_box.pack(**padding)

        tk.Label(self, text="Download Location").pack(anchor="w", **padding)
        tk.Entry(self, textvariable=self.path_var, width=40).pack(side="left", padx=10)
        tk.Button(self, text="Browse", command=self.select_path).pack(side="left")

        tk.Button(self, text="Download", command=self.start_download).pack(pady=15)
        tk.Label(self, textvariable=self.status_var).pack(pady=10)

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def is_x_url(self, url: str) -> bool:
        return "twitter.com" in url or "x.com" in url

    def fetch_formats(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Invalid URL")
            return

        # X için format seçimi yok
        if self.is_x_url(url):
            self.resolution_box["values"] = []
            self.fps_box["values"] = []
            self.resolution_var.set("")
            self.fps_var.set("")
            self.status_var.set("X detected (auto quality)")
            return

        self.status_var.set("Fetching formats...")

        def task():
            try:
                ydl_opts = {
                    "quiet": True,
                    "skip_download": True,
                }

                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    formats = info.get("formats", [])

                resolutions = set()
                fps_map = {}

                for f in formats:
                    if f.get("vcodec") != "none" and f.get("height"):
                        res = f"{f['height']}p"
                        resolutions.add(res)
                        fps_map.setdefault(res, set())
                        if f.get("fps"):
                            fps_map[res].add(str(int(f["fps"])))

                resolutions = sorted(resolutions, key=lambda x: int(x.replace("p", "")))
                self.available_formats = fps_map

                self.resolution_box["values"] = resolutions
                self.resolution_var.set(resolutions[0] if resolutions else "")
                self.update_fps()
                self.status_var.set("Idle")
            except Exception:
                self.status_var.set("Error")
                messagebox.showerror("Error", "Failed to fetch formats")

        threading.Thread(target=task, daemon=True).start()
        self.resolution_var.trace_add("write", lambda *_: self.update_fps())

    def update_fps(self):
        res = self.resolution_var.get()
        fps_list = sorted(self.available_formats.get(res, []), key=int)
        self.fps_box["values"] = fps_list
        self.fps_var.set(fps_list[0] if fps_list else "")

    def start_download(self):
        url = self.url_var.get().strip()
        path = self.path_var.get().strip()

        if not url or not path:
            messagebox.showerror("Error", "Missing URL or download path")
            return

        self.status_var.set("Downloading...")
        threading.Thread(target=self.download, daemon=True).start()

    def download(self):
        try:
            common_opts = {
                "outtmpl": os.path.join(self.path_var.get(), "%(title)s.%(ext)s"),
                "merge_output_format": "mp4",
            }

            url = self.url_var.get()

            if self.is_x_url(url):
                ydl_opts = {
                    **common_opts,
                    "format": "best",
                }

            elif self.format_var.get() == "MP3":
                ydl_opts = {
                    **common_opts,
                    "format": "bestaudio/best",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                }

            else:
                res = self.resolution_var.get().replace("p", "")
                ydl_opts = {
                    **common_opts,
                    "format": f"bestvideo[ext=mp4][height<={res}]+bestaudio[ext=m4a]",
                }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_var.set("Completed")
        except Exception as e:
            self.status_var.set("Error")
            messagebox.showerror("Error", f"Download failed\n{e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
