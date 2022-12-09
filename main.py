# Wordle cheater program by Aiden C
# Built for Comp Sci 12/1/2022

# --------------------- ATTENTION: For Debuging Set To True
debugistrue = True

# Importing
import sorters
from sorters import *
import tkinter
from tkinter import *
import time
import math

# Defining Window
master = Tk()
master.configure(bg="#121213")
master.geometry("400x675")
master.title("Wordle Solver")

# Prereqs for tkinter
pixeler = tkinter.PhotoImage(width=1, height=1)
clonehandlerlist = []

# Define non-changing tkinter widgets
Label(master, text="Wordle Bot", font="Verdana 35 bold", fg="white", bg="#121213").place(relx=0.5, y=5, anchor=N)
watermark = Label(master, text="Wordle Solver By Aiden C For Comp Sci 2022", font="Verdana 7", fg="white", bg="#121213")
Frame(master, bg="#3a3a3c").place(relx=0.5, y=75, relwidth=1, height=2, anchor=N)
finishbutton = Button(master, width=25, height=25, font="Verdana 20 bold", bg="#121213", activebackground="#121213", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: finish())
instructions = Label(master, text="Use the keyboard to type in your first word \n Click the gray squares until they match wordle!", fg="white", font="Verdana 10 bold", bg="#121213")

# Read text file
with open('fivewords.txt') as words:
    allwords = words.readlines()
allwords = [x.strip().lower() for x in allwords]

# Pre-Defining Computer Analysis Variables
badletters = []
letters = ["", "", "", "", ""]
yellowletters = ["", "", "", "", ""]

# Pre-Defining user input variables
userinput = []
charmap = ["0", "0", "0", "0", "0"]

# Pre-Defining Global Variables
entry = 0
nextplace = True
tutorialsteps = "bbg"
runningani = False

# Function to play tutorial hide animation
def hidetutorial():
    global tutorialsteps
    global entry
    if (not "b" in tutorialsteps) and (entry == 0):
        tutorialsteps = "ggb"
        rrgb = 255
        grgb = 255
        brgb = 255
        frames = 50
        for p in range(0, frames):
            instructions.config(fg="#%s" % (sorters.rgb_to_hex((rrgb, grgb, brgb))))
            master.update()
            time.sleep(0.01)
            rrgb = rrgb - int(((255 - 18) / frames))
            grgb = grgb - int(((255 - 18) / frames))
            brgb = brgb - int(((255 - 19) / frames))
        instructions.config(fg="#121213")

# Optional debug function for debugging - prints all important variables
def debug():
    global letters
    global letters
    global yellowletters
    global userinput
    global charmap
    global allwords
    global debugistrue
    debugistrue = True
    print("Green Letters: " + str(letters))
    print("Yellow Letters: " + str(yellowletters))
    print("Grey Letters: " + str(badletters))
    print("Current Input: " + str(userinput))
    print("Mapped Colors: " + str(charmap))
    if len(allwords) < 50:
        print("All Words: " + str(allwords))

# Function to read the user's input
def readcharmap():
    global badletters
    global yellowletters
    global letters
    global userinput
    global charmap
    viewdnum = 0
    for char in charmap:
        if char == "0":
            if userinput[viewdnum] not in letters:
                badletters.append(userinput[viewdnum])
        if char == "1":
            print(viewdnum)
            yellowletters[viewdnum] = (yellowletters[viewdnum] + userinput[viewdnum])
        if char == "2":
            letters[viewdnum] = userinput[viewdnum]
        viewdnum += 1
    print(yellowletters)

# Function to change color of UI boxes in gui
def changecolor(box):
    global clonehandlerlist
    global charmap
    global boxes
    global tutorialsteps

    # Since this is part of the tutorial, I need to update the tutorial steps completed variable
    tutorialsteps = tutorialsteps[0] + "g" + tutorialsteps[2]

    if charmap[box] == "0":
        boxes[box].config(bg="#b59f3b", activebackground="#b59f3b")
        charmap[box] = "1"
    elif charmap[box] == "1":
        boxes[box].config(bg="#538d4e", activebackground="#538d4e")
        charmap[box] = "2"
    elif charmap[box] == "2":
        boxes[box].config(bg="#3a3a3c", activebackground="#3a3a3c")
        charmap[box] = "0"

    hidetutorial()

# Function I got off of the internet to clone widgets (I barely know how it works)
def clone(widget):
    parent = widget.nametowidget(widget.winfo_parent())
    cls = widget.__class__

    clone = cls(parent)
    for key in widget.configure():
        clone.configure({key: widget.cget(key)})
    return clone

# Function to animate the pressing of the next button
def newwordani(prev, char):
    global userinput
    global entry
    global boxes
    global clonehandlerlist

    # Handle animations for creating box clones
    tempxconfig = []
    for f in range(0, 5):
        tempxconfig.append(clone(boxes[f]))
    for x in range(0, 5):
        clonehandlerlist.append(tempxconfig[x])
    for u in range(0, 5):
        tempxconfig[u].config(command=lambda: None, text=str(prev[u]))
        tempxconfig[u].place(x=(master.winfo_width() / 2 - ((u - 2) * -75)), y=100 + ((entry - 1) * 75), anchor=N)
        if char[u] == "0":
            tempxconfig[u].config(bg="#3a3a3c", activebackground="#3a3a3c")
        elif char[u] == "1":
            tempxconfig[u].config(bg="#b59f3b", activebackground="#b59f3b")
        elif char[u] == "2":
            tempxconfig[u].config(bg="#538d4e", activebackground="#538d4e")

    # New boxes animation
    for k in range(0, 75):
        for h in range(0, 5):
            boxes[h].place(y=((100 + ((entry - 1) * 75)) + k))
            master.update()
            time.sleep(0.0001)
    for i in range(0, 5):
        boxes[i].config(text=userinput[i])
        for j in range(1, 30):
            boxes[i].config(font=("Verdana %s bold" % j))
            master.update()
            time.sleep(0.001)

    # Animation to show the checkmark button
    if (entry == 1):
        rrgb = 18
        grgb = 18
        brgb = 19
        frames = 20
        for p in range(0, frames):
            finishbutton.config(bg="#%s" % (sorters.rgb_to_hex((rrgb, grgb, brgb))), activebackground="#%s" % (sorters.rgb_to_hex((rrgb, grgb, brgb))))
            master.update()
            time.sleep(0.01)
            rrgb = rrgb + int(((83 - 18) / frames))
            grgb = grgb + int(((141 - 18) / frames))
            brgb = brgb + int(((78 - 19) / frames))
        finishbutton.config(text="✓")

# Defining changing GUI widgets
box1 = Button(master, width=60, height=60, font="Verdana 30 bold", bg="#3a3a3c", activebackground="#3a3a3c", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: changecolor(0))
box2 = Button(master, width=60, height=60, font="Verdana 30 bold", bg="#3a3a3c", activebackground="#3a3a3c", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: changecolor(1))
box3 = Button(master, width=60, height=60, font="Verdana 30 bold", bg="#3a3a3c", activebackground="#3a3a3c", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: changecolor(2))
box4 = Button(master, width=60, height=60, font="Verdana 30 bold", bg="#3a3a3c", activebackground="#3a3a3c", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: changecolor(3))
box5 = Button(master, width=60, height=60, font="Verdana 30 bold", bg="#3a3a3c", activebackground="#3a3a3c", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: changecolor(4))
nextbutton = Button(master, text="Next", width=200, height=50, font="Verdana 30 bold", bg="#538d4e", activebackground="#538d4e", activeforeground="lightgrey", highlightthickness=0, bd=0, fg="white", compound="center", padx=0, pady=0, image=pixeler, command=lambda: nextfunc())

# Function to dynamically move widgets upon GUI window size change
def resize():
    global nextplace
    for i in range(0, 5):
        boxes[i].place(x=(master.winfo_width() / 2 - ((i - 2) * -75)), anchor=N)

    for f in range(0, len(clonehandlerlist)):
        clonehandlerlist[f].place(x=(master.winfo_width() / 2 - (((f - ((math.ceil((f + 1) / 5) - 1) * 5)) - 2) * -75)), anchor=N)

    if nextplace:
        nextbutton.place(y=(master.winfo_height() - 80), x=(master.winfo_width() / 2), anchor=N)

    watermark.place(relx=0.5, y=(master.winfo_height() - 5), anchor=S)

    if entry >= 1:
        finishbutton.place(x=(master.winfo_width() / 2), y=(master.winfo_height() - 123), anchor=N)

    instructions.place(x=(master.winfo_width() / 2), y=180, anchor=N)

# Function to run when the check-mark button is pressed - Define all characters as green and update colors
def finish():
    global charmap
    charmap = ["2", "2", "2", "2", "2"]
    nextbutton.config(text="Winner!")
    for i in range(0, 5):
        boxes[i].config(bg="#538d4e", activebackground="#538d4e")

# Function to run when the next button is pressed
def nextfunc():
    global entry
    global nextplace
    global allwords
    global badletters
    global yellowletters
    global letters
    global userinput
    global charmap
    global tutorialsteps
    global runningani
    debug()

    # Don't run the function twice at once because as wyatt proved it causes errors
    if not runningani:
        runningani = True

        # Return win if all blocks are green
        if (not "0" in charmap) and (not "1" in charmap):
            nextbutton.config(text="Winner!")

        # Go to next if they aren't
        elif (entry < 5) and (len(userinput) == 5):

            # If the tutorial isn't done yet, mark it as finshed and update GUI
            if tutorialsteps != "ggb":
                tutorialsteps = "ggg"
                hidetutorial()

            # Reset GUI and apply new word
            readcharmap()
            allwords = sortgrayyellowgreen(allwords, badletters, yellowletters, letters, debugistrue)
            prevuserimput = userinput
            prevcharmap = charmap
            yellowletters = ["", "", "", "", ""]
            userinput = []
            charmap = ["0", "0", "0", "0", "0"]
            entry += 1
            temptop = topword(allwords)
            for j in range(0, 5):
                userinput.append(temptop[j])
            for i in range(0, 5):
                boxes[i].config(bg="#3a3a3c", activebackground="#3a3a3c")
                boxes[i].config(text="")
            newwordani(prevuserimput, prevcharmap)

        # If the input isn't complete, play button vibrating animation
        elif nextplace:
            nextplace = False
            pos = 0
            for r in range(0, 20):
                pos += 1
                nextbutton.place(x=((master.winfo_width() / 2) + pos))
                master.update()
                time.sleep(0.001)
            for t in range(0, 2):
                for k in range(0, 40):
                    pos -= 1
                    nextbutton.place(x=((master.winfo_width() / 2) + pos))
                    master.update()
                    time.sleep(0.001)
                for k in range(0, 40):
                    pos += 1
                    nextbutton.place(x=((master.winfo_width() / 2) + pos))
                    master.update()
                    time.sleep(0.001)
            for r in range(0, 20):
                pos -= 1
                nextbutton.place(x=((master.winfo_width() / 2) + pos))
                master.update()
                time.sleep(0.001)
            nextbutton.place(x=(master.winfo_width() / 2))
            nextplace = True
        runningani = False

# Read and apply keypresses
def onKeyPress(event):
    global userinput
    global boxes
    global tutorialsteps

    #Another part of the tutorial, needs to update tutorial string
    tutorialsteps = "g" + tutorialsteps[1] + tutorialsteps[2]

    # .isalpha() determines if the key pressed is a letter or not
    if entry == 0:
        if (event.char).isalpha() and (len(userinput) <= 4):
            userinput.append(event.char)
        elif (event.char) == "\x08":
            userinput = userinput[:-1]
        elif (event.char) == "\r":
            nextfunc()
        for i in range(0, 5):
            if len(userinput) > i:
                boxes[i].config(text=str(userinput[i]))
            else:
                boxes[i].config(text="")
    elif (event.char) == "\r":
        nextfunc()

    hidetutorial()

# Array that defines box variable names for box cloning
boxes = [box1, box2, box3, box4, box5]

# Setting the initial y position of the first boxes
for i in range(0, 5):
    boxes[i].place(y=100)

# Binding tkinter listeners to functions
master.bind("<Configure>", lambda event: resize())
master.bind('<KeyPress>', onKeyPress)

# Start the gui!
mainloop()
