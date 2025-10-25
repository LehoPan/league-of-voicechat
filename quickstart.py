#Import the required Libraries
from email.policy import default
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image  

team = 0 #blue X and Y coordinates
role = 0 #row 3, jungle 

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")


def get_team():
    global entry
    team= int(entry.get())

    if team == 1:
        win['background'] = '#538AD9'
        label.configure(text = "[2]Top, [3]Jungle, [4]Mid, [5]Adc, [6]Support")
    else:
        win['background'] = '#D55B3F'
        label.configure(text = "[2]Top, [3]Jungle, [4]Mid, [5]Adc, [6]Support")

    #Create a Button to validate Entry Widget
    role_button = Button(win, text= "Okay",width= 20, command= get_role)
    role_button.pack(pady=20)


    team_button.destroy()
    entry.delete(0, END)

def get_role():
    global entry
    role= int(entry.get())
    canvas = Canvas(win, width = 100, height = 100)      
    canvas.pack() 

    match role:
        case 2:
            role_name = "Top"
            img = ImageTk.PhotoImage(Image.open("Assets/top_icon.png"))     
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            entry.delete(0, END)
            return
        case 3:
            role_name = "Jungle"
            img = ImageTk.PhotoImage(Image.open("Assets/jungle_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            entry.delete(0, END)
            return
        case 4:
            role_name = "Mid"
            img = ImageTk.PhotoImage(Image.open("Assets/mid_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            entry.delete(0, END)
            return
        case 5:
            role_name = "Adc"
            img = ImageTk.PhotoImage(Image.open("Assets/adc_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            entry.delete(0, END)
            return
        case _:
            role_name = "Support"
            img = ImageTk.PhotoImage(Image.open("Assets/supp_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            entry.delete(0, END)
            return
        
    

#Initialize a Label to display the User Input
label=Label(win, text="Enter 0 for red team, 1 for blue team", font=("Courier 10 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
team_button = Button(win, text= "Okay",width= 20, command= get_team)
team_button.pack(pady=20)

win.mainloop()