from turtle import done
import numpy as np
import cv2
from PIL import ImageGrab
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

#Import the required Libraries
from email.policy import default
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image  

def get_team():
    global team #blue X and Y coordinates
    global entry
    team= int(entry.get())

    if team == 1:
        win['background'] = '#538AD9'
        label.configure(text = "[2]Top, [3]Jungle, [4]Mid, [5]Adc, [6]Support")
    else:
        team = 0
        win['background'] = '#D55B3F'
        label.configure(text = "[2]Top, [3]Jungle, [4]Mid, [5]Adc, [6]Support")

    #Create a Button to validate Entry Widget
    role_button = Button(win, text= "Okay",width= 20, command= get_role)
    role_button.pack(pady=20)


    team_button.destroy()
    entry.delete(0, END)

def get_role():
    global entry
    global role #row 3, jungle 
    role= int(entry.get())
    canvas = Canvas(win, width = 100, height = 100)      
    canvas.pack() 

    match role:
        case 2:
            role_name = "Top"
            img = ImageTk.PhotoImage(Image.open("Assets/top_icon.png"))     
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            win.destroy()

            return
        case 3:
            role_name = "Jungle"
            img = ImageTk.PhotoImage(Image.open("Assets/jungle_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            win.destroy()

            return
        case 4:
            role_name = "Mid"
            img = ImageTk.PhotoImage(Image.open("Assets/mid_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            win.destroy()

            return
        case 5:
            role_name = "Adc"
            img = ImageTk.PhotoImage(Image.open("Assets/adc_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            win.destroy()

            return
        case _:
            role_name = "Support"
            role = 6
            img = ImageTk.PhotoImage(Image.open("Assets/supp_icon.png"))      
            canvas.create_image(20,20, anchor=NW, image=img)
            print(role, team)
            win.destroy()

            return
    
#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")
    

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

print(role, team)

kernel = np.ones((2, 2), np.uint8)

def getColorMask(img):
    # White mask
    lowerBound = np.array([0, 0, 255])
    upperBound = np.array([180, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, lowerBound, upperBound)

# minimap template
template = cv2.imread('Assets/FOV.png', 0)
h, w = template.shape
color = (255, 0, 0)


if team == 1:
    x = 7
    y = 8
else:
    x = 3
    y = 4

#location logging on spreadsheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("League Prox Database").sheet1

while True:
    img = ImageGrab.grab(bbox=(1640, 800, 1919, 1080)) #left_x, top_y, right_x, bottom_y
    img_np = np.array(img)
    frame = getColorMask(img_np)
    img_erosion = cv2.erode(frame, kernel, iterations=1)
    

    result = cv2.matchTemplate(img_erosion, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    location = max_loc

    # center of the rectangle
    screen_center = (int(location[0] + (w/2)), int(location[1] + (h/2)))

    # draw point of screen center
    cv2.circle(img_erosion, screen_center, 2, 255, -1)

    # draw the rectangle
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img_erosion, location, bottom_right, 255, 2)

    #sheet update
    sheet.update_cell(role, x, screen_center[0])
    sheet.update_cell(role, y, screen_center[1])


    cv2.imshow("frame", img_erosion)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

    time.sleep(2.5)
    
cv2.destroyAllWindows()