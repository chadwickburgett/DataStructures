"""
Name            : finalGuiBurgett.py
Author          : Chadwick Burgett
Created         : 04/24/2021
Course          : CIS 152 Data structures
Version         : 1.0
Copyright       : This is my own original work based on
                specifications issued by our instructor
                and ideas I researched on several different
                internet sites.
Description     : This is the GUI for the finalShotsSystemBurgett program. This
creates the basic GUI that is used for the program.
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access to
my program.
"""
from programs import finalShotsSystemBurgett as final
from tkinter import *


def sel():
    try:
        answer = text1.get()
        int_answer = int(answer)
        selection = final.user_input(var.get(), int_answer, people, shot)

    except:
        selection = "Invalid input"
    label.config(text=selection)


people = final.PriorityQueue()
shot = final.ShotsStack()
root = Tk()
var = IntVar()
root.geometry("600x600")
root.title("Welcome")
label1 = Label(root, text="Vaccine Tracking System", fg="Black", bg="White", relief="groove", font=("arial", 16, "bold"))
label1.pack()
welcome_label = Label(root, text="This system tracks the amount of people or shots left in the vaccine system", fg="Black", font=("arial", 12))
welcome_label.pack()
label_blank = Label(root, text=" ")
label_blank.pack()
label_blank2 = Label(root, text=" ")
label_blank2.pack()
label2 = Label(root, text="Please click shot or people and enter the amount below:", fg="Black", font=("arial", 12,))
label2.place(x=100, y=75)
text1 = Entry(root, textvariable=IntVar())
text1.place(x=250, y=120)
R1 = Radiobutton(root, text="Shot", variable=var, value=1)
R1.place(x=175, y=110)
R2 = Radiobutton(root, text="People", variable=var, value=2)
R2.place(x=175, y=130)

button1 = Button(root, text="Add", fg="black", bg="lightgray", relief=RIDGE, font=("arial", 16, "bold"), command=sel)
button1.place(x=225, y=175)

label = Label(root)
label.place(x=175, y=225)
root.mainloop()
