# Wordle Solver By Aiden C For Comp Sci 2022
# Built for Comp Sci on 12/1/22

# Import modules and load tkinter
import tkinter
from tkinter import *
master = Tk()
master.geometry("400x600")
master.title("Wordle Solver")

#Loading Text Box
textboxframe = Frame(master)
textboxframe.columnconfigure(0, weight=10)
textboxframe.grid_propagate(False)
textbox = Text(textboxframe, padx=10, wrap="none")
textbox.grid(sticky="we")

#Buttons

# Auto-Resize Handler
def resize():
    # Top Text Box Resize Handler
    textboxframe.config(width=(round(master.winfo_width())-20), height=round(master.winfo_height() / 3.5))
    textboxframe.place(y=10, x=10)
    textbox.config(pady=(round((master.winfo_height() / 7) - (master.winfo_height() / 12))), font=("Arial", (int(master.winfo_height() / 10))))


# Binding Resize To Resize Function
master.bind("<Configure>", lambda event: resize())

# Close Out Main Loop
mainloop()