'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''
import customtkinter as tk
tk.set_appearance_mode("dark")
count = -1
count2 = 0
count3 = 0
responses = []
questions = ["What player is this", 
             "Which Premier League club did Chris Wood join from Leeds United in 2017?", 
             "At what age did Chris Wood make his debut for the New Zealand senior national team (the All Whites)", 
             "Wood became the first New Zealander to achieve what feat in the English Premier League?", 
             "Before his professional career, which club did Wood play for in Auckland before moving to Hamilton at age 11?", 
             "Which city was Chris Wood born in?", 
             "Which team did Chris Wood represent at the 2020 Tokyo Olympics?", 
             "As of late 2024, which club has Chris Wood established himself as the all-time leading goalscorer for in the Premier League?"]
answers = [{1: ["Mohammed Salah", "Chris Wood", "Cole Palmer"]}, 
           {2: ["Liverpool", "Burnley", "Derby County"]}, 
           {3: ["22", "18", "21"]}, 
           {4: ["Get more than 10 assists", "Score a hat-trick", "Move to LaLiga"]}, 
           {5: ["Gurkha FC", "Onehunga Sports", "Auckland United"]}, 
           {6: ["Christchurch", "Auckland", "Hamilton"]}, 
           {7: ["Australia", "New Zealand", "Cook Islands"]}, 
           {8: ["Everton", "Nottingham Forest", "Leeds United"]}, ]
root = tk.CTk()
root.geometry("1000x1000")
check = tk.IntVar(value=0)

def submit():
    global option
    option = check.get()
    print(option)
    return option

while count < 9:

    count += 1
    count2 += 1
    count3 = 0
    label = tk.CTkLabel(root, text=f"Chris Wood Quiz:\nQuestion {count2}: {questions[count2]}", font=("Roboto Medium", 38))
    label.pack(padx=20, pady=20)
    cb = tk.CTkRadioButton(master=root, text=f"{answers[count][count2][count3]}", variable=check, value=1)
    cb.pack(padx=20, pady=20)
    count3 += 1
    cb2 = tk.CTkRadioButton(master=root, text=f"{answers[count][count2][count3]}", variable=check, value=2)
    cb2.pack(padx=20, pady=20)
    count3 += 1
    cb3 = tk.CTkRadioButton(master=root, text=f"{answers[count][count2][count3]}", variable=check, value=3)
    cb3.pack(padx=20, pady=20)
    count3 += 1

    submitbutton = tk.CTkButton(root, text="Submit Answer", command=submit)
    submitbutton.pack(pady=30)
    
    responses.append(str(submit()))

    root.mainloop()