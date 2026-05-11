'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''
import customtkinter as tk
tk.set_appearance_mode("dark")
callback = False
countqd = -1
countq = 0
counta = 0
acheck = 0
responses = []
errors = []
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
root.attributes("-fullscreen", True)
root.geometry("1000x1000")
check = tk.IntVar(value=0)

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
def available():
    submitbutton.configure(state="normal")
def submit():
    global option
    option = check.get()
    print(option)
    global callback
    callback = True
    clear_screen()
    draw()
    return option


try:
    def draw():
        global countqd
        global countq
        global counta
        callback = False
        countqd += 1
        countq += 1
        counta = 0
        label = tk.CTkLabel(root, text=f"Chris Wood Quiz:\nQuestion {countq}: {questions[countq]}", font=("Roboto Medium", 38))
        label.pack(padx=20, pady=20)
        cb = tk.CTkRadioButton(master=root, text=f"{answers[countqd][countq][counta]}", variable=check, value=1, command=available)
        cb.pack(padx=20, pady=20)
        counta += 1
        cb2 = tk.CTkRadioButton(master=root, text=f"{answers[countqd][countq][counta]}", variable=check, value=2, command=available)
        cb2.pack(padx=20, pady=20)
        counta += 1
        cb3 = tk.CTkRadioButton(master=root, text=f"{answers[countqd][countq][counta]}", variable=check, value=3, command=available)
        cb3.pack(padx=20, pady=20)
        counta += 1

        global submitbutton
        submitbutton = tk.CTkButton(root, text="Submit Answer", command=submit, state="disabled")
        submitbutton.pack(pady=30)

        while callback == True:
            responses.append(str(submit()))
            print(responses)
    draw()
    root.mainloop()
except Exception as e:
    errors.append(e)
    for i in range(len(errors)):
        print(errors[i])