"""imageviewer.py
Image Viewer by Aaron Langley Jun 2018
this is simple image viewer that display an image in a window frame sized
for the image
"""

import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess

#generate base window
window = tk.Tk()
window.title("Image Viewer")
window.geometry("400x400")

#adds canvas
canvas = tk.Canvas(window, width = 400, height = 400)
canvas.pack()

#adds button to select file to display
path_button = tk.Button(window,text = "...", command = browse())
path_button.pack(side = tk.LEFT)

#when path_button is clicked
path_button.bind('<Button-1')

#test image path variable
path = '/home/aaron/Programs/cat0.jpeg'

#allows tkinter to open picture
img = ImageTk.PhotoImage(Image.open(path))

#label for photo displayed
panel = tk.Label(canvas, image = img)

#add panel to window
panel.pack(side = "bottom", fill = "both", expand = "yes")


window.mainloop()
