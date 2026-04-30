'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''

# import cv2 by running "pip install opencv-python" into terminal.
import cv2
# imported 'time' to help make everything more readable, i use "t" in place of time to make it 
# easier to type (considering how much i use it here for readability)
import time as t
# tkinter is a python library (standard) i use that lets you create and track the state of different Widget UI
import tkinter as tk
from tkinter import font
# randomise the question order with random, i use "r" for short so i can use the variable called "random"
import random as r

# ========================================================================================================================
# Instructions on how to run the quiz.  
# 1. run "pip install opencv-python" in your terminal
# 2. copy the file directory of the photo that was attatched and change the backslashes "\" and 
# replace them with the forward slash "/"
chris = cv2.imread("G:/My Drive/11DTSD/L1-DTSD-AS92004/Chris.jpg")
# ^ Grabs the file directory (i will attatch the images as necessary) grab the root of the downloaded 
# image by right clicking the file, clicking "copy file directory" and changing the backslashes used "\" to forward slashes "/")
# ========================================================================================================================

# count counts the uh questions
count = -1
# rcount counts the uh responses
rcount = 0
# defining questions and possible answers
questions = [
    "Who is this?", 
    "What team, as of the 25/26 Premier League season, does Chris Wood play for", 
    "Where is chris wood from in New Zealand", 
    "How many goals does Chris Wood have over all competitions this season? (25/26)"]
responses = [
    {1: "Cole Palmer", 2: "Chris Wood", 3: "Bam Adebayo"}, 
    {1: "Manchester United", 2: "Nottingham Forest", 3: "Leeds United"},
    {1: "Tauranga", 2: "Auckland", 3: "Hamilton"},
    {1: "14", 2: "4", 3: "0"}
]

# tk.Tk initialises the root (the window or CONTAINER itself)
root = tk.Tk
# Defines the title (The top of the window's name)
root.title("Chris Wood Quiz")
# Defines the resolution
root.geometry("300x200")
while True:
    count += 1
    # Creates the text inside the window aka "label"
    label = tk.Label(root, text=f"{questions[count]}", font=("Arial", 24))
    # The pack method organises widgets (label in this case) into "blocks" or "boxes" so they dont 
    # collide before placing them in a window,
    # pady (padding, y axis) adds space above and below any widget
    label.pack(pady=15)

    # This should create the states for the checkboxes (e.g. 1 = checked 0 = unticked)
    state1 = tk.BooleanVar()
    state2 = tk.BooleanVar()
    state3 = tk.BooleanVar()
    rcount = 0
    # Creates the actual checkboxes text is the possible responses, then sets the state of the checkbox to 
    # the previous boolean defined
    cb1 = tk.Checkbutton(root, text=(f"{responses[count][rcount]}"), variable=state1)
    # anchor on pack method anchors the widget to "w" or west and padding is set to x axis
    cb1.pack(anchor="w", padx=20)
    rcount += 1
    cb2 = tk.Checkbutton(root, text=(f"{responses[count][rcount]}"), variable=state1)
    # anchor on pack method anchors the widget to "w" or west and padding is set to x axis
    cb2.pack(anchor="w", padx=20)
    rcount += 1
    cb3 = tk.Checkbutton(root, text=(f"{responses[count][rcount]}"), variable=state1)
    # anchor on pack method anchors the widget to "w" or west and padding is set to x axis
    cb3.pack(anchor="w", padx=20)
    rcount += 1