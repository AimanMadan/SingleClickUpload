import tkinter as tk
import os

root = tk.Tk()

#Window size
root.geometry("300x500")
#titlebar
root.title("Beat Stars Single Click")


title = tk.Label(root, text = "Single click upload", font=('Ariel', 13))
title.pack(padx=20, pady=20)

wav_drop = tk.Label(root, text = "Drop .wav file below", font=('Ariel', 11))
wav_drop.pack(padx=20, pady=10)

stem_drop = tk.Label(root, text = "Drop .zip or .rar file below", font=('Ariel', 11))
stem_drop.pack(padx=20, pady=10)


track_title = tk.Entry(root, font=('Ariel', 11))
track_title.pack()

root.mainloop()
