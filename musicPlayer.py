import tkinter as tk
from tkinter import filedialog
import pygame
import threading

paused = False  # Flag to control music pause/unpause, initially set to False

def play_music(mp3File):
  pygame.mixer.init()
  pygame.mixer.music.load(mp3File)
  pygame.mixer.music.play()
  play_pause_button.config(text="⏸️", command=pause_music)

def pause_music():
    global paused
    if pygame.mixer.music.get_busy():  # Check if music is playing
        pygame.mixer.music.pause()
        paused = True
        play_pause_button.config(text="▶️", command=unpause_music)  # Update after pause
    else:
        print("No music is currently playing.")  # Inform user

def unpause_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        play_pause_button.config(text="⏸️", command=pause_music)  # Update after unpause

def toggle_play_pause():
    if paused:
        unpause_music()
    else:
        pause_music()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        play_music(file_path)

# Tkinter setup
root = tk.Tk()
root.title("Music Player")

# Buttons
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)

play_pause_button = tk.Button(root, text="▶️", command=toggle_play_pause)
play_pause_button.pack(pady=5)

# Start thread to manage music
pygame.init()

root.mainloop()
