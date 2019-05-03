###############Acronym Creator by Aaron Langley June 2018#######################
"""This programs strips the first letter of a multi-word string and generates
a new string from those letters in uppercaseself. A GUI was later added using
tkinter.
"""
import tkinter as tk

#create a window for function
window = tk.Tk()
window.title("Acronym Creator")
window.geometry("200x200")

phrase = tk.StringVar()
acronym = ""

#this function prompts user for phrase and generates a capital acronym
def create_acronym():
    acronym = ""

    #turns string uppercase
    phrase = phrase.upper()

    #convert string into a list
    list = phrase.split()

    #cycle through the list
    for word in list:
        acronym += word[0]

    return acronym

#entry label
label1 = tk.Label(window, text = "Enter your phrase here")
label1.pack()

#entry_field
entry = tk.Entry(window, textvariable = phrase)
entry.pack()

#entry buttom
button1 = tk.Button(window, text = "Go", command = create_acronym )
button1.pack()

#output label
label2 = tk.Label(window, text = "You acronym:")
label2.pack()

#entry_field
output = tk.Entry(window, textvariable = acronym)
output.pack()

window.mainloop()
