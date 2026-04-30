'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''

# import cv2 by running "pip install opencv-python" into terminal.
import cv2
# imported 'time' to help make everything more readable, i use "t" in place of time to make it easier to type (considering how much i use it here for readability)
import time as t
# tkinter is a python library (standard) i use that lets you create and track the state of different Widget UI
import tkinter as tk
from tkinter import font
# randomise the question order with random, i use "r" for short so i can use the variable called "random"
import random as r

# ========================================================================================================================
# Instructions on how to run the quiz.  
# 1. run "pip install opencv-python" in your terminal
# 2. copy the file directory of the photo that was attatched and change the backslashes "\" and replace them with the forward slash "/"
chris = cv2.imread("G:/My Drive/11DTSD/L1-DTSD-AS92004/Chris.jpg")
# ^ Grabs the file directory (i will attatch the images as necessary) grab the root of the downloaded image by right clicking the file, clicking "copy file directory" and changing the 
# backslashes used "\" to forward slashes "/")
# ========================================================================================================================


#defining questions and possible answers
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

# tk.Tk initialises the root (the window itself)
root = tk.Tk
# Defines the title (The top of the window's name)
root.title("Chris Wood Quiz")
# 
root.geometry