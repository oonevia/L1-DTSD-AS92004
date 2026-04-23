'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''

# import cv2 by running "pip install opencv-python" into terminal.
import cv2
# imported 'time' to help make everything more readable, i use "t" in place of time to make it easier to type (considering how much i use it here for readability)
import time as t
# tkinter is a python library (standard) i use that lets you create and track the state of different Widget UI
import tkinter as tk
# randomise the question order with random, i use "r" for short so i can use the variable called "random"
import random as r

# ========================================================================================================================
# Instructions on how to run the quiz.
# 1. run "pip install opencv-python" in your terminal
# 2. copy the file directory of the photo that was attatched and change the backslashes "\" and replace them with the forward slash "/"
chris = cv2.imread("C:/Users/russelldamascenol/Downloads/Chris.jpg")
# ^ Grabs the file directory (i will attatch the images as necessary) grab the root of the downloaded image by right clicking the file, clicking "copy file directory" and changing the backslashes used "\" to forward slashes "/")
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
# Here i define the tsate of the checkbox i created a condition where that gets the value of the cb (checkbox) state and decides wether the state of the cb is '1' checked or '0' unchecked.
def cbstate():
    print(f"Checkbox is: {"Checked" if state.get() == 1 else "Unchecked"}")
# tk.TK() Initialises the "root window" of the actual UI for the checkbox.
root = tk.Tk()
#This tk.IntVar will initialise the variable used to store the state of checkbox value (e.g. Checked '1' or Unchecked '0')
state = tk.IntVar()
    
print("Welcome to the Chris Wood quiz, New Zealands ONLY Premier League player.")
t.sleep(1.5)
print("\nYour first question:\nAn image of a player will be shown for 3 seconds, choose which player you think it is.")
t.sleep(5)
# Shows the image, the "3 Seconds!" names the window and the 'chris' variable contains the windows directory
cv2.imshow("3 Seconds!", chris)
# Waits 3000 miliseconds (3 Seconds)
cv2.waitKey(3000)
# Gets rid of the popup window.
cv2.destroyAllWindows()
t.sleep(0.3)

# using "tk.Checkbutton" - a function that creates built-in cb (checkbox) widgets - inside of a for loop i can apply the settings inside of brackets and define the cb
for i in range(len(questions)):
    print(questions[i])
    random = r.randint(1,3)
    cb = tk.Checkbutton(root, text=responses[i][random], variable=state, command=cbstate)
    cb.pack()
    root.mainloop()