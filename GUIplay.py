import random
from tkinter import *
window=Tk()
window.geometry("400x300")
window.title("Rock_peper-scissors game")
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""
def choice_to_number(choice):#dictionary each choice with a value
    rps={"rock":0,"paper":1,"scissor":2}
    return rps[choice]
def number_to_choice(number):
    rps={0:"rock",1:"paper",2:"scissor"}
    return rps[number]
def random_comuter_choice():
    return random.choice(["rock","paper","scissor"])#the computer choice 
def result(human_choice,comp_choice):
    global USER_SCORE#global is used for variable defined outside the function
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if user == comp:
       print("same input, play again")
    elif((user-comp)%3==1):#IF REMINDER ==1 THE USER WIN
       print("you win")
       USER_SCORE+=1
    else:
       print("computer win")
       COMP_SCORE+=1
    text_area=Text(master=window,height=12,width=30,bg="#FFFF99")       
    text_area.grid(column=0,row=4)
    answer="Your choice{c} \n The computers choice {cc} \n Your score {s} \n comuters score {ss}".format(c=USER_CHOICE,cc= COMP_CHOICE,s=USER_SCORE,ss=COMP_SCORE)
    text_area.insert(END,answer)
def rock():
    global USER_CHOICE#global is used for variable defined outside the function
    global COMP_CHOICE
    USER_CHOICE="rock"
    COMP_CHOICE=random_comuter_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE#global is used for variable defined outside the function
    global COMP_CHOICE
    USER_CHOICE="paper"
    COMP_CHOICE=random_comuter_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE#global is used for variable defined outside the function
    global COMP_CHOICE
    USER_CHOICE="scissor"
    COMP_CHOICE=random_comuter_choice()
    result(USER_CHOICE,COMP_CHOICE)
button1=Button(text="rock",bg="skyblue",command=rock)       
button1.grid(column=1,row=0)
button2=Button(text="paper",bg="skyblue",command=paper)       
button2.grid(column=1,row=1)
button3=Button(text="scissor",bg="skyblue",command=scissor)       
button3.grid(column=1,row=2)
window.mainloop()