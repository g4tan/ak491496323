#In this program, we will import a built-in module called tkinter. Tkinter is used to created a dynamic GUI for users.
#I first declared root = Tk() to create a small GUI window when program ran, then I created an enter bar for me.
#The bar is named Entry(), it allows me to type in contents inside this created bar. Similar to Button(), it allows me to create
#buttons and add features on it. After I set up some "options" or we call properties of Entry() and Button(), we used either grid(), pack() or place(). Entry() has an option we need to add
# which is textvariable. If we dont add textvariable and use method StringVar(), the button cannot interact with the Entry() bar. I used the method grid()
#Notice grid(), place() and pack() have some similarities, but grid is easier for me to organize my button horizontally and vertically in
#the sense of making organized and formatted buttons. That is, grid() have the options to place my buttons in rows and colunmns. That is the reason
#why I picked grid() over place() and pack(). After set up my screen, I defined some functions for my buttons bc they do not have functionality to do operations.
#it is nice that button has a property called "command=", this property can call back my defined functions. Notice, if lambda function is not introduced, the number
#will display on the screen without clicking the button. If lambda function is introduced, then the screen will first display our global function 'expression' which
# is an empty space. After emtpy space is evluated, the empty space + whatever we input, we get our clicked button values. Lastly, I need to fix the rounding errors.
from tkinter import *

def Clickclick(number):
    global expression
    expression += str(number)
    textinput.set(expression)

def Clicktoclear():
    global expression
    expression = ' '
    textinput.set(expression)

def Clickequal():
    global expression
    calculation = eval(expression)
    textinput.set(calculation)

root = Tk()
expression = ' '
textinput = StringVar()
entry = Entry(root, width = 40, textvariable=textinput, bd = 15, justify = 'right').grid(columnspan = 4, ipadx= 40, ipady=10)


button_1 = Button(root, text= "1", padx = 50, pady = 20, command = lambda:Clickclick(1)).grid(row = 1, column = 0 )
button_2 = Button(root, text= "2", padx = 50, pady = 20, command = lambda:Clickclick(2)).grid(row = 1, column = 1)
button_3 = Button(root, text= "3", padx = 50, pady = 20, command = lambda:Clickclick(3)).grid(row = 1, column = 2)
button_add = Button(root, text= "+", padx = 60, pady = 20, command = lambda:Clickclick("+")).grid(row = 1, column = 3)
button_4 = Button(root, text= "4", padx = 50, pady = 20, command = lambda:Clickclick(4)).grid(row = 2, column = 0)
button_5 = Button(root, text= "5", padx = 50, pady = 20, command = lambda:Clickclick(5)).grid(row = 2, column = 1)
button_6 = Button(root, text= "6", padx = 50, pady = 20, command = lambda:Clickclick(6)).grid(row = 2, column = 2)
button_subtract = Button(root, text= "-", padx = 60, pady = 20, command = lambda:Clickclick("-")).grid(row = 2, column = 3)
button_7 = Button(root, text= "7", padx = 50, pady = 20, command = lambda:Clickclick(7)).grid(row = 3, column = 0)
button_8 = Button(root, text= "8", padx = 50, pady = 20, command = lambda:Clickclick(8)).grid(row = 3, column = 1)
button_9 = Button(root, text= "9", padx = 50, pady = 20, command = lambda:Clickclick(9)).grid(row = 3, column = 2)
button_division = Button(root, text= "/", padx = 60, pady = 20, command = lambda:Clickclick('/')).grid(row = 4, column = 3)
button_multiply = Button(root, text= "*", padx = 60, pady = 20, command = lambda:Clickclick('*')).grid(row = 3, column = 3 )
button_0 = Button(root, text= "0", padx = 110, pady = 20, command = lambda:Clickclick('0')).grid(row = 4, columnspan=2)
button_decimel = Button(root, text= ".", padx = 50, pady = 20, command = lambda:Clickclick('.')).grid(row = 4, column = 2)
button_equal =  Button(root, text= "=", padx = 170, pady = 20, command = lambda:Clickequal()).grid(row = 5, columnspan=3)
button_clear = Button(root, text= "Clear", padx = 50, pady = 20, command = lambda:Clicktoclear()).grid(row = 5, column= 3)
root.mainloop()
