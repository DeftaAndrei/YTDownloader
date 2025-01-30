import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import yt_dlp

def download_audio(url):
    try:
        downloads_path = str(Path.home() / "Downloads")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{downloads_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Audio descărcat cu succes în folderul Downloads."
    except Exception as e:
        return f"Eroare: {str(e)}"

def download_video(url):
    try:
        downloads_path = str(Path.home() / "Downloads")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{downloads_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Videoclip descărcat cu succes în folderul Downloads."
    except Exception as e:
        return f"Eroare: {str(e)}"

def start_audio_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Eroare", "Introduceți un URL valid.")
        return

    messagebox.showinfo("Descărcare", "Descărcarea audio a început. Așteptați...")
    result = download_audio(url)
    messagebox.showinfo("Rezultat", result)

def start_video_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Eroare", "Introduceți un URL valid.")
        return

    messagebox.showinfo("Descărcare", "Descărcarea video a început. Așteptați...")
    result = download_video(url)
    messagebox.showinfo("Rezultat", result)

# Crearea interfeței grafice
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x250")
root.configure(bg="#f2f2f2")

# Etichetă și câmp pentru URL
url_label = tk.Label(root, text="Introduceți URL-ul videoclipului YouTube:", bg="#f2f2f2", font=("Arial", 12))
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Butoane pentru descărcare
audio_button = tk.Button(root, text="Descarcă doar audio", command=start_audio_download, bg="#4CAF50", fg="white", font=("Arial", 10), padx=10, pady=5)
audio_button.pack(pady=10)

video_button = tk.Button(root, text="Descarcă videoclip complet", command=start_video_download, bg="#008CBA", fg="white", font=("Arial", 10), padx=10, pady=5)
video_button.pack(pady=10)

# Rularea interfeței grafice
root.mainloop()
