import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Helper function to ensure the destination folder exists
def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to organize files based on user input
def organize_files():
    # Get values from the input fields
    downloads_folder = downloads_folder_entry.get()
    videos_folder = videos_folder_entry.get()
    documents_folder = documents_folder_entry.get()
    pictures_folder = pictures_folder_entry.get()
    music_folder = music_folder_entry.get()
    
    # Get file extensions from the input fields
    video_extensions = set(video_ext_entry.get().replace(" ", "").split(","))
    document_extensions = set(doc_ext_entry.get().replace(" ", "").split(","))
    picture_extensions = set(pic_ext_entry.get().replace(" ", "").split(","))
    audio_extensions = set(audio_ext_entry.get().replace(" ", "").split(","))
    
    # Organize files in Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Move video files
        if any(filename.endswith(ext) for ext in video_extensions):
            ensure_directory_exists(videos_folder)
            shutil.move(file_path, os.path.join(videos_folder, filename))
        
        # Move document files
        elif any(filename.endswith(ext) for ext in document_extensions):
            ensure_directory_exists(documents_folder)
            shutil.move(file_path, os.path.join(documents_folder, filename))
        
        # Move picture files
        elif any(filename.endswith(ext) for ext in picture_extensions):
            ensure_directory_exists(pictures_folder)
            shutil.move(file_path, os.path.join(pictures_folder, filename))
        
        # Move audio files
        elif any(filename.endswith(ext) for ext in audio_extensions):
            ensure_directory_exists(music_folder)
            shutil.move(file_path, os.path.join(music_folder, filename))

    messagebox.showinfo("Success", "Files organized successfully!")

# Function to browse folder
def browse_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

# Setting up the GUI
root = tk.Tk()
root.title("Automatic File Organizer")

# Folder input fields
tk.Label(root, text="Downloads Folder:").grid(row=0, column=0, sticky="e")
downloads_folder_entry = tk.Entry(root, width=50)
downloads_folder_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(downloads_folder_entry)).grid(row=0, column=2)

tk.Label(root, text="Videos Folder:").grid(row=1, column=0, sticky="e")
videos_folder_entry = tk.Entry(root, width=50)
videos_folder_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(videos_folder_entry)).grid(row=1, column=2)

tk.Label(root, text="Documents Folder:").grid(row=2, column=0, sticky="e")
documents_folder_entry = tk.Entry(root, width=50)
documents_folder_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(documents_folder_entry)).grid(row=2, column=2)

tk.Label(root, text="Pictures Folder:").grid(row=3, column=0, sticky="e")
pictures_folder_entry = tk.Entry(root, width=50)
pictures_folder_entry.grid(row=3, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(pictures_folder_entry)).grid(row=3, column=2)

tk.Label(root, text="Music Folder:").grid(row=4, column=0, sticky="e")
music_folder_entry = tk.Entry(root, width=50)
music_folder_entry.grid(row=4, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(music_folder_entry)).grid(row=4, column=2)

# File extension input fields with default values
tk.Label(root, text="Video Extensions (e.g., .mp4, .mov):").grid(row=5, column=0, sticky="e")
video_ext_entry = tk.Entry(root, width=50)
video_ext_entry.insert(0, ".mp4, .mov, .avi, .mkv")  # Default video extensions
video_ext_entry.grid(row=5, column=1)

tk.Label(root, text="Document Extensions (e.g., .pdf, .docx):").grid(row=6, column=0, sticky="e")
doc_ext_entry = tk.Entry(root, width=50)
doc_ext_entry.insert(0, ".pdf, .docx, .txt, .pptx, .xlsx")  # Default document extensions
doc_ext_entry.grid(row=6, column=1)

tk.Label(root, text="Picture Extensions (e.g., .jpg, .png):").grid(row=7, column=0, sticky="e")
pic_ext_entry = tk.Entry(root, width=50)
pic_ext_entry.insert(0, ".jpg, .jpeg, .png, .gif, .bmp, .svg")  # Default picture extensions
pic_ext_entry.grid(row=7, column=1)

tk.Label(root, text="Audio Extensions (e.g., .mp3, .wav):").grid(row=8, column=0, sticky="e")
audio_ext_entry = tk.Entry(root, width=50)
audio_ext_entry.insert(0, ".mp3, .wav, .aac, .flac")  # Default audio extensions
audio_ext_entry.grid(row=8, column=1)

# Start Button
start_button = tk.Button(root, text="Start Organizing", command=organize_files)
start_button.grid(row=9, column=0, columnspan=3, pady=10)

root.mainloop()
