'''Lucas Russell Damasceno - 11DSD Level 1 Internal.'''
import customtkinter as tk
tk.set_appearance_mode("dark")
count = -1
count2 = 0
count3 = 0
questions = ["test", "test2", "test3", "test4", "test5", "test6", "test7", "test8"]
answers = [{1: ["test", "test2", "test3"]}, {2: ["test", "test2", "test3"]}, {3: ["test", "test2", "test3"]}, {4: ["test", "test2", "test3"]}, {5: ["test", "test2", "test3"]}, {6: ["test", "test2", "test3"]}, {7: ["test", "test2", "test3"]}, {8: ["test", "test2", "test3"]}, ]
root = tk.CTk()
root.geometry("1000x1000")

while count < 9:

    count += 1
    count2 += 1
    count3 = 0
    label = tk.CTkLabel(root, text=f"Chris Wood Quiz: Question {count2}", font=("Roboto Medium", 38))
    label.pack(padx=20, pady=20)
    cb = tk.CTkCheckBox(master=root, text=f"{answers[count][count2][count3]}")
    cb.pack(padx=20, pady=20)
    count3 += 1
    cb2 = tk.CTkCheckBox(master=root, text=f"{answers[count][count2][count3]}")
    cb2.pack(padx=20, pady=20)
    count3 += 1
    cb3 = tk.CTkCheckBox(master=root, text=f"{answers[count][count2][count3]}")
    cb3.pack(padx=20, pady=20)
    count3 += 1
    root.mainloop()