'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''
import customtkinter as tk
import random as rnd
from PIL import Image as img
import requests as req
from io import BytesIO as IO

tk.set_appearance_mode("dark")
# Im defining all my variables that need to be predetermined here
p = 20
score = 0
correct = 0
decimal = 0
countqd = -1
countq = 0
counta = 0
acheck = 0
responses = []
errors = []
quiz_data = []
# the image url i can use for my http request
reqdata = "https://upload.wikimedia.org/wikipedia/commons/6/67/Chris_Wood_%28cropped%29.jpg"
# these are the responses for the score you get (/8)
funresponses = {0: "ZERO ball knowledge", 
                0.125: "near to no knowledge on Chris Wood", 
                0.25: "a small amount of knowledge on Chris Wood", 
                0.375: "the normal amount of knowledge someone should have on Chris Wood", 
                0.5: "above average knowledge on Chris Wood. Wow!", 
                0.625: "an exceptional amount of knowledge on Chris Wood! Congrats!", 
                0.75: "near-perfect knowledge of Chris Wood! Do you know him personally!?", 
                0.875: "a ludicrous level of ball knowledge! Congratulations.", 
                1: "too much knowledge on Chris Wood. You must be cheating!"}
# the questions. i use brackets here in my list so that later on in the code when i use rnd.shuffle it preserves the position of question:answer
raw_questions = [
    ("What player is this?", 
     ["Chris Wood", "Mohammed Salah", "Cole Palmer"]), 
    ("Which Premier League club did Chris Wood join from Leeds United in 2017?", 
     ["Burnley", "Liverpool", "Derby County"]), 
    ("At what age did Chris Wood make his debut for the New Zealand senior national team (the All Whites)", 
     ["17", "23", "21"]),
    ("Wood became the first New Zealander to achieve what feat in the English Premier League?", 
     ["Score a hat-trick", "Get more than 10 assists", "Move to LaLiga"]), 
    ("Before his professional career, which club did Wood play for in Auckland before moving to Hamilton at age 11?", 
     ["Onehunga Sports", "Gurkha FC", "Auckland United"]), 
    ("Which city was Chris Wood born in?", 
     ["Auckland", "Christchurch", "Hamilton"]), 
    ("Which team did Chris Wood represent at the 2020 Tokyo Olympics?", 
     ["New Zealand", "Australia", "Cook Islands"]), 
    ("As of late 2024, which club has Chris Wood established himself as the all-time leading goalscorer for in the Premier League?", 
     ["Nottingham Forest", "Everton", "Leeds United"])
]
# here i grab two values and input them into seperate variables, the questions (q_text) and answers (answs)
for q_text, answs in raw_questions:
    correct_ans = answs[0]
    shuffled = list(answs)
    rnd.shuffle(shuffled)
    # I thought it would make my life easier if instead of using the raw questions every time i need to pull a part of the quiz, i make it into quiz data where i can easily grab question, option, and correct answer.
    quiz_data.append({"question": q_text, "options": shuffled, "correct": correct_ans})

rnd.shuffle(quiz_data)
# custom tkinter is used to initialise my window/master 'root'
root = tk.CTk()
# fullscreen
root.attributes("-fullscreen", True)
# 1000*1000 incase fullscreen fails for some reason
root.geometry("1000x1000")

# now to make sure my checkboxes (technically called 'radiobuttons') are checked or unchecked i use a "binary" variable 1 or 0
check = tk.IntVar(value=0)
# getting the screen width so i can make the text wrap to the screens resolution incase user is on something thats not 1920*1080
width = root.winfo_screenwidth()
# text wrapper
wrapping = width - width / 5
# you can make a font in ctk BEFORE using it in text which makes my life easier but i only ended up using it for the image load error :/
roboto = tk.CTkFont(family="Roboto", size=20, weight="bold")

# clearscreen function goes through all ctk widgets and destroys
def clsc():
    for widget in root.winfo_children(): 
        widget.destroy()

# this the function used for the chris wood image, 
# i found it'd be annoying to have to place your file directory in every time someone wanted to use my code so i though i could send an http request to the image link and grab the image then 
# use bytes IO to load the image directly onto the users RAM, 
# then i could load it from the users ram by getting the raw binary data and inputting that into pillows image function, then displaying using a ctk label.
def imgreq(url):
    # wikipedia actually blocks bot http requests so i sent user headers to have some sort of auth
    headers = {'User-Agent': 'Mozilla/5.0'}
    # this is the response from the http request
    urlresp = req.get(url, headers=headers)
    # using bytes io to convert it into raw binary data
    imgdata = IO(urlresp.content)

    # im pretty sure it was starting the img reading later than when it should so i set the image data to be seeked at the start
    imgdata.seek(0)
    # uses pillow to compile the binary data to the users ram
    imgobj = img.open(imgdata)
    # returns the info to ctk
    return tk.CTkImage(dark_image=imgobj, size=(450, 716))

# returns the submit button to clickable once a radiobutton has been activated
def available():
    submitbutton.configure(state="normal")

# the function command that gets executed once the user has submitted
def submit():
    # defines variables globally
    global countq
    global correct
    global score
    global decimal
    # defining the selected input, i use selected index when im indexing something to the selected radiobutton
    selindex = check.get() - 1
    seltext = quiz_data[countq-1]["options"][selindex] 
     
    # gets correct answer by indexing to the correct answwer and comparing to selected answer.
    if seltext == quiz_data[countq-1]["correct"]:
        correct += 1
    
    # countq is the question number makes sure that the quiz is still going
    if countq < len(quiz_data):
        check.set(0)
        clsc()
        draw()
    # however if the quiz ISN'T going then we run the end message
    else: 
        clsc()
        score = int((correct / len(quiz_data)) * 100)
        decimal = correct / len(quiz_data)
        # calculates the score and displays with the funresponses
        flabel = tk.CTkLabel(root, 
                             text=f"You got {score}% correct!, thats {correct}/{len(quiz_data)}! - You have {funresponses[decimal]}", 
                             font=("Roboto Medium", 25))
        flabel.pack(padx=p, pady=p)
        flabel.place(relx=0.5, rely=0.5, anchor="center")

# the actual main meat of the code (i had to put this into a function because it needed to be used in the submit function to redraw the page)
def draw():
    # defines variables globally
    global countq
    global submitbutton
    # current data for the options.
    c_data = quiz_data[countq]
    quick = c_data
    # shuffles the options so the order is randomised each time
    rnd.shuffle(quick["options"])
    # adds to the question number.
    countq += 1
    # question label
    qlabel = tk.CTkLabel(root, 
                         text=f"Chris Wood Quiz:\nQuestion {countq}: {c_data['question']}", 
                         font=("Roboto Medium", 38), 
                         wraplength=wrapping)
    qlabel.pack(padx=p, pady=p)
    # okay so i had an issue where because the alignment of the options were centered, the length of the answers would push the buttons unevenly
    # so i thought that if i create a transparent frame to the left of the answers then aligned the answers it would be inline
    # now i COULD just use a grid frame but i would have to rewrite LITERALLY everything which i already did more than once and i aint doin allat
    square = tk.CTkFrame(root, width=840, height=100, corner_radius=0, fg_color="transparent")
    square.pack(pady=p, padx=p, side="left")

    # this is cool if i use enumerate i can get the option number AND the answer itself
    for i, option in enumerate(quick["options"]):
        # i used valued as i+1 because that would make it 1 2 3 instead of 0 1 2 which is easier to manage
        rb = tk.CTkRadioButton(master=root, text=option, variable=check, value=i+1, command=available)
        rb.pack(padx=p, pady=10, anchor="w")
    # defining the submit button and when i draw it i actually START it disabled so when the command "available" is executed it goes to active state
    submitbutton = tk.CTkButton(root, text="Submit Answer", command=submit, state="disabled")
    # placing instead of packing so i can keep it generally "central"
    submitbutton.place(relx=0.5, rely=0.4, anchor="center")
    
    # this checks if we are on the what player is this question with chris wood's image
    if c_data["question"] == "What player is this?":
        try:
            # send the http request
            chrisimg = imgreq(reqdata)
            # in ctk you use a label because you can load the image attribute to it which is cool
            ilabel = tk.CTkLabel(root, text="", image=chrisimg)
            ilabel.pack(pady=p, padx=p)
        # however if i get an error it will display as a red error message which helped ALOT when figuring out why wikipedia couldnt load my image
        except Exception as err:
            elabel = tk.CTkLabel(root, 
                                 text=f"There was an error loading the image: {err}", 
                                 font=roboto, text_color="#8B0000", 
                                 wraplength=wrapping-20)
            elabel.pack(padx=p, pady=p)
# draws for the first time
draw()
# keeps the window open
root.mainloop()