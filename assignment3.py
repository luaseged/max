from tkinter import *
root=Tk()
root.title("Quiz Game")
root.geometry("600x400")
root.configure(bg="orange")




info=("""
A lives in the corner’s house 
C is between E and G,
There is 1 house between D and F
F is neighbor of G and,
There are two houses between A and G.
""")

no1=("1. Who lives in the second corner?")
no2=("2. Who lives in the middle?")
no3=("3. Who lives between B and G?")
no4=("4. Who is the neighbor of A?")
no5=("5. How many houses are there between B and E?")


def check():
    next_butn.place(x=400, y=300)
    A = answer.get()
    if A == "D":
        correcting.configure(text="correct")
        correcting.place(x=230, y=225)

    elif A == "d":
        correcting.configure(text="correct")
        correcting.place(x=230, y=225)

    else:
        correcting.configure(text="incorrect", fg="red")
        correcting.place(x=230, y=225)
        correct_ans.configure(text="the correct answer is: 'D' ")
        correct_ans.place(x=200, y=260)

def check2():
    next_butn.place(x=400, y=300)
    B = answer2.get()
    if B == "G":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)

    elif B == "g":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)

    else:
        correcting.configure(text="incorrect", fg="red")
        correcting.place(x=230, y=225)
        correct_ans.configure(text="the correct answer is: 'G' ")
        correct_ans.place(x=200, y=260)

def check3():
    next_butn.place(x=400, y=300)

    C = answer3.get()
    if C == "F":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    elif C == "f":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    else:
        correcting.configure(text="incorrect", fg="red")
        correcting.place(x=230, y=225)
        correct_ans.configure(text="the correct answer is: 'F' ")
        correct_ans.place(x=200, y=260)

def check4():
    next_butn.place(x=400, y=300)

    D = answer4.get()
    if D == "E":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    elif D == "e":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    else:
        correcting.configure(text="incorrect", fg="red")
        correcting.place(x=230, y=225)
        correct_ans.configure(text="the correct answer is: 'E' ")
        correct_ans.place(x=200, y=260)


def check5():
    next_butn.place(x=400, y=300)
    E = answer5.get()
    if E == "3":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    elif E == "three":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    elif E == "Three":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    elif E == "THREE":
        correcting.configure(text="correct", fg="green")
        correcting.place(x=230, y=225)
    else:
        correcting.configure(text="incorrect", fg="red")
        correcting.place(x=230, y=225)
        correct_ans.configure(text="the correct answer is: '3' ")
        correct_ans.place(x=200, y=260)

def question():
    intro.configure(text=no1, font=("times new roma", 14, "bold"), fg="blue")
    answer.place(x=170, y=130)
    answer_butn.place(x=235, y=160)
    butn.configure(text="Instruction", command=order)
    butn.place(x=50, y=300)
    next_butn.place(x=400, y=300)
    quit_butn.place(x=1400, y=1300)
    quit_label.place(x=2150, y=1300)
    next_butn.place(x=2150, y=1300)


def question2():
    intro.configure(text=no2)
    answer2.place(x=170, y=130)
    answer.place(x=1170, y=1130)
    correct_ans.place(x=1200, y=1260)
    correcting.place(x=1230, y=1225)
    answer_butn.configure(command=check2)
    next_butn.configure(command=question3)
    next_butn.place(x=2150, y=1300)


def question3():
    intro.configure(text=no3)
    answer3.place(x=170, y=130)
    answer2.place(x=1170, y=1130)
    correct_ans.place(x=1200, y=1260)
    correcting.place(x=1230, y=1225)
    answer_butn.configure(command=check3)
    next_butn.configure(command=question4)
    next_butn.place(x=2150, y=1300)


def question4():
    intro.configure(text=no4)
    answer4.place(x=170, y=130)
    answer3.place(x=1170, y=1130)
    correct_ans.place(x=1200, y=1260)
    correcting.place(x=1230, y=1225)
    answer_butn.configure(command=check4)
    next_butn.configure(command=question5)
    next_butn.place(x=2150, y=1300)


def question5():
    intro.configure(text=no5)
    answer5.place(x=170, y=130)
    answer4.place(x=1170, y=1130)
    correct_ans.place(x=1200, y=1260)
    correcting.place(x=1230, y=1225)
    answer_butn.configure(command=check5)
    next_butn.configure(text="Finish", command=thanks)
    next_butn.place(x=2150, y=1300)

def thanks():
    intro.configure(text="thank you!!!", font=("algerian", 18, "bold"), fg="green")
    answer5.place(x=1170, y=1130)
    next_butn.configure(text="Quit", command=close)
    next_butn.place(x=200, y=220)
    butn.place(x=1170, y=1130)
    intro.place(x=200, y=100)
    answer_butn.place(x=1170, y=1130)
    correct_ans.place(x=1200, y=1260)
    correcting.place(x=1230, y=1225)



def view_info():
    intro.configure(text=info,font=("nyala", 14, "bold"), fg="black")




def close():
    quit()

def order():
    intro.configure(text=info, font=("nyala", 14, "bold"), fg="black")
    quit_label.place(x=330, y=355)
    intro.place(x=120, y=100)
    butn.configure(command=question)
    butn.configure(text="Go to question", width=14, fg="blue")
    butn.place(x=10, y=300)
    quit_butn.place(x=400, y=300)
    answer.place(x=1000, y=1000)
    answer2.place(x=1000, y=1000)
    answer3.place(x=1000, y=1000)
    answer4.place(x=1000, y=1000)
    answer5.place(x=1000, y=1000)
    answer_butn.place(x=1000, y=1000)
    next_butn.place(x=1400, y=1300)
    correcting.place(x=1230, y=1230)
    correct_ans.place(x=1230, y=1230)



def instruction():
    intro.configure(text="To begin press the button bellow \nand read game instruction.", font=("times new roman", 18))
    butn.configure(text="Instruction")
    butn.configure(command=order)




intro=Label(root, text="Hello and Welcome!!!\n This is simple quiz game", font=("algerian", 14, "bold"), fg="blue", bg="orange")
intro.place(x=120, y=160)

butn=Button(root, text="Click here",font=("nyala", 14, "bold"),width=8, fg="black", command=instruction )
butn.place(x=200, y=300)

answer=Entry(root, font=("algerian", 12))
answer.insert(0,"")

answer2=Entry(root, font=("algerian", 12))
answer2.insert(0,"")

answer3=Entry(root, font=("algerian", 12))
answer3.insert(0,"")

answer4=Entry(root, font=("algerian", 12))
answer4.insert(0,"")
answer5=Entry(root, font=("algerian", 12))
answer5.insert(0,"")



answer_butn=Button(root, text="Enter",font=("nyala", 15, "bold"), fg="black", command=check)

quit_butn = Button(root, text="Quit", font=("nyala", 15, "bold"), fg="red", command=close, width=15)

next_butn=Button(text="Next Question", command=question2, fg="blue",width=14,font=("nyala", 15, "bold"))

quit_label=Label(root, text=("If you don't understand the game\n         feel free to quit the game."), font=("nyala", 12, "bold"),fg="red", bg="orange")

correcting = Label(root, font=("nyala", 20), fg="green")
correct_ans = Label(root, font=("nyala", 12, "bold"), fg="black")

root.mainloop()