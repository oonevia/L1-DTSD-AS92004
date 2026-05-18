'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''
import customtkinter as tk
import random as rnd
from PIL import Image as img
import requests as req
from io import BytesIO as IO

tk.set_appearance_mode("dark")

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
reqdata = "https://upload.wikimedia.org/wikipedia/commons/6/67/Chris_Wood_%28cropped%29.jpg"

funresponses = {0: "ZERO ball knowledge", 
                0.125: "near to no knowledge on Chris Wood", 
                0.25: "a small amount of knowledge on Chris Wood", 
                0.375: "the normal amount of knowledge someone should have on Chris Wood", 
                0.5: "above average knowledge on Chris Wood. Wow!", 
                0.625: "an exceptional amount of knowledge on Chris Wood! Congrats!", 
                0.75: "near-perfect knowledge of Chris Wood! Do you know him personally!?", 
                0.875: "a ludicrous level of ball knowledge! Congratulations.", 
                1: "too much knowledge on Chris Wood. You must be cheating!"}

raw_questions = [
    ("What player is this?", ["Chris Wood", "Mohammed Salah", "Cole Palmer"]), 
    ("Which Premier League club did Chris Wood join from Leeds United in 2017?", ["Burnley", "Liverpool", "Derby County"]), 
    ("At what age did Chris Wood make his debut for the New Zealand senior national team (the All Whites)", ["17", "23", "21"]),
    ("Wood became the first New Zealander to achieve what feat in the English Premier League?", ["Score a hat-trick", "Get more than 10 assists", "Move to LaLiga"]), 
    ("Before his professional career, which club did Wood play for in Auckland before moving to Hamilton at age 11?", ["Onehunga Sports", "Gurkha FC", "Auckland United"]), 
    ("Which city was Chris Wood born in?", ["Auckland", "Christchurch", "Hamilton"]), 
    ("Which team did Chris Wood represent at the 2020 Tokyo Olympics?", ["New Zealand", "Australia", "Cook Islands"]), 
    ("As of late 2024, which club has Chris Wood established himself as the all-time leading goalscorer for in the Premier League?", ["Nottingham Forest", "Everton", "Leeds United"])
]

for q_text, answs in raw_questions:
    correct_ans = answs[0]
    shuffled = list(answs)
    rnd.shuffle(shuffled)
    quiz_data.append({"question": q_text, "options": shuffled, "correct": correct_ans})

rnd.shuffle(quiz_data)
 
root = tk.CTk()
root.attributes("-fullscreen", True)
root.geometry("1000x1000")

check = tk.IntVar(value=0)
width = root.winfo_screenwidth()
wrapping = width - width / 5
roboto = tk.CTkFont(family="Roboto", size=20, weight="bold")

def clsc():
    for widget in root.winfo_children(): 
        widget.destroy()

def imgreq(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    urlresp = req.get(url, headers=headers)
    imgdata = IO(urlresp.content)

    imgdata.seek(0)
    imgobj = img.open(imgdata)

    return tk.CTkImage(dark_image=imgobj, size=(450, 716))

def available():
    submitbutton.configure(state="normal")

def submit():
    global countq
    global correct
    global score
    global decimal
    selindex = check.get() - 1
    seltext = quiz_data[countq-1]["options"][selindex] 
     
    if seltext == quiz_data[countq-1]["correct"]:
        correct += 1
    
    if countq < len(quiz_data):
        check.set(0)
        clsc()
        draw()
    else: 
        clsc()
        score = int((correct / len(quiz_data)) * 100)
        decimal = correct / len(quiz_data)
        flabel = tk.CTkLabel(root, text=f"You got {score}% correct!, thats {correct}/{len(quiz_data)}! - You have {funresponses[decimal]}", font=("Roboto Medium", 25))
        flabel.pack(padx=p, pady=p)
        flabel.place(relx=0.5, rely=0.5, anchor="center")
 
def draw():
    global countq
    global submitbutton
    c_data = quiz_data[countq]
    quick = c_data
    rnd.shuffle(quick["options"])
    countq += 1
    
    qlabel = tk.CTkLabel(root, text=f"Chris Wood Quiz:\nQuestion {countq}: {c_data['question']}", font=("Roboto Medium", 38), wraplength=wrapping)
    qlabel.pack(padx=p, pady=p)

    square = tk.CTkFrame(root, width=840, height=100, corner_radius=0, fg_color="transparent")
    square.pack(pady=p, padx=p, side="left")

    for i, option in enumerate(quick["options"]):
        rb = tk.CTkRadioButton(master=root, text=option, variable=check, value=i+1, command=available)
        rb.pack(padx=p, pady=10, anchor="w")

    submitbutton = tk.CTkButton(root, text="Submit Answer", command=submit, state="disabled")
    submitbutton.place(relx=0.5, rely=0.4, anchor="center")
    
    if c_data["question"] == "What player is this?":
        try:
            chrisimg = imgreq(reqdata)
            ilabel = tk.CTkLabel(root, text="", image=chrisimg)
            ilabel.pack(pady=p, padx=p)
        except Exception as err:
            elabel = tk.CTkLabel(root, text=f"There was an error loading the image: {err}", font=roboto, text_color="#8B0000", wraplength=wrapping-20)
            elabel.pack(padx=p, pady=p)

draw()
root.mainloop()