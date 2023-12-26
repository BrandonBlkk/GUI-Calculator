from tkinter import *

# Create the main application window
root = Tk()
root.title("Calculator")

# Define a font for the buttons
font = ("arial", 9)
input_font = ("arial", 11)

# Create an Entry widget with specified font and width
user_input = Entry(root,font= input_font, width= 57)
user_input.grid(row= 0, column= 0, columnspan= 4, padx= 10, pady= 10)

# Function to handle button click for numbers
def button_click(new_number):
    curent_num = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, str(curent_num) + str(new_number))

# Function to handle button click for clear   
def button_clear():
    user_input.delete(0, END)

# Functions to handle button click for operators    
def button_add():
    global fst_num
    global choice
    choice = "addition"
    fst_num = int(user_input.get())
    user_input.delete(0, END)

def button_sub():
    global fst_num
    global choice
    choice = "subtraction"
    fst_num = int(user_input.get())
    user_input.delete(0, END)
    
def button_multi():
    global fst_num
    global choice
    choice = "multiplication"
    fst_num = int(user_input.get())
    user_input.delete(0, END)
    
def button_div():
    global fst_num
    global choice
    choice = "division"
    fst_num = int(user_input.get())
    user_input.delete(0, END)

def button_equal():
    sec_num = user_input.get()
    user_input.delete(0, END)
    # Make condition depends on user choice
    if choice == "addition":
        user_input.insert(0, round(fst_num + int(sec_num), 2))
    if choice == "subtraction":
        user_input.insert(0, round(fst_num - int(sec_num), 2))
    if choice == "multiplication":
        user_input.insert(0, round(fst_num * int(sec_num), 2))
    if choice == "division":
        user_input.insert(0, round(fst_num / int(sec_num), 2))

# Creating and placing buttons on the grid with specified properties
label_0 = Button(root, text= "0", padx= 50, font = font, pady= 20, command= lambda: button_click(0))
label_0.grid(row= 4, column= 0)
label_1 = Button(root, text= "1", padx= 50, font = font, pady= 20, command= lambda: button_click(1))
label_1.grid(row= 3, column= 0)
label_2 = Button(root, text= "2", padx= 50, font = font, pady= 20, command= lambda: button_click(2))
label_2.grid(row= 3, column= 1)
label_3 = Button(root, text= "3", padx= 50, font = font, pady= 20, command= lambda: button_click(3))
label_3.grid(row= 3, column= 2)
label_4 = Button(root, text= "4", padx= 50, font = font, pady= 20, command= lambda: button_click(4))
label_4.grid(row= 2, column= 0)
label_5 = Button(root, text= "5", padx= 50, font = font, pady= 20, command= lambda: button_click(5))
label_5.grid(row= 2, column= 1)
label_6 = Button(root, text= "6", padx= 50, font = font, pady= 20, command= lambda: button_click(6))
label_6.grid(row= 2, column= 2)
label_7 = Button(root, text= "7", padx= 50, font = font, pady= 20, command= lambda: button_click(7))
label_7.grid(row= 1, column= 0)
label_8 = Button(root, text= "8", padx= 50, font = font, pady= 20, command= lambda: button_click(8))
label_8.grid(row= 1, column= 1)
label_9 = Button(root, text= "9", padx= 50, font = font, pady= 20, command= lambda: button_click(9))
label_9.grid(row= 1, column= 2)
label_clear = Button(root, text= "clear", font = font, padx= 40, pady= 20, command= lambda: button_clear())
label_clear.grid(row= 4, column= 1)
label_add = Button(root, text= "+", font = font, padx= 50, pady= 20, command= button_add)
label_add.grid(row= 4, column= 3)
label_sub = Button(root, text= "-", font = font, padx= 50, pady= 20, command= button_sub)
label_sub.grid(row= 3, column= 3)
label_multi = Button(root, text= "*", font = font, padx= 50, pady= 20, command= button_multi)
label_multi.grid(row= 2, column= 3)
label_div = Button(root, text= "/", font = font, padx= 51, pady= 20, command= button_div)
label_div.grid(row= 1, column= 3)
label_equal = Button(root, text= "=", font = font, padx= 49, pady= 20, command= button_equal)
label_equal.grid(row= 4, column= 2)

# Start the Tkinter event loop, allowing the GUI to respond to user inputs and events
root.mainloop()