import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import yt_dlp
import pyperclip

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
        return "Audio successfully downloaded to the Downloads folder."
    except Exception as e:
        return f"Error: {str(e)}"

def download_video(url):
    try:
        downloads_path = str(Path.home() / "Downloads")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{downloads_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Video successfully downloaded to the Downloads folder."
    except Exception as e:
        return f"Error: {str(e)}"

def start_audio_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    messagebox.showinfo("Download", "Audio download started. Please wait...")
    result = download_audio(url)
    messagebox.showinfo("Result", result)

def start_video_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    messagebox.showinfo("Download", "Video download started. Please wait...")
    result = download_video(url)
    messagebox.showinfo("Result", result)

def paste_url():
    url_entry.delete(0, tk.END)  # Clear the entry field
    url_entry.insert(0, pyperclip.paste())  # Paste the clipboard content

# Create the graphical interface
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("450x250")
root.configure(bg="#87CEEB")  # Light blue color for the background

# Set the application icon
icon_path = "Icon.jpg"
try:
    root.iconphoto(False, tk.PhotoImage(file=icon_path))
except Exception as e:
    messagebox.showwarning("Warning", f"Could not load icon: {str(e)}")

# Label and input field for URL
url_label = tk.Label(root, text="Enter the YouTube video URL:", bg="#87CEEB", font=("Arial", 12))
url_label.pack(pady=10)

url_frame = tk.Frame(root, bg="#87CEEB")
url_frame.pack(pady=5)

url_entry = tk.Entry(url_frame, width=40, font=("Arial", 10))
url_entry.pack(side=tk.LEFT, padx=5)

paste_button = tk.Button(url_frame, text="Paste", command=paste_url, bg="#FFC107", fg="black", font=("Arial", 10), padx=5, pady=2)
paste_button.pack(side=tk.RIGHT)

# Download buttons
audio_button = tk.Button(root, text="Download Audio Only", command=start_audio_download, bg="#4CAF50", fg="white", font=("Arial", 10), padx=10, pady=5)
audio_button.pack(pady=10)

video_button = tk.Button(root, text="Download Full Video", command=start_video_download, bg="#008CBA", fg="white", font=("Arial", 10), padx=10, pady=5)
video_button.pack(pady=10)

# Run the graphical interface
root.mainloop()

# The application allows the user to enter a YouTube video URL, and then download either the audio or the full video to the Downloads folder.