'''
1. First we install the module Tkinter it's used for make GUI in python
2. After that we will install the Time Module - from time import strftime
3. After that we will create a root window like = root = tk.Tk() 
4. After that we will create the Title of our code
5. after that we will create a function that's name time()
6. and we use font calibri'''

import tkinter as tk
from time import strftime

#after we will create a root window
root = tk.Tk()
#after that we will create the Title of our code
root.title("Digital Clock")

#after that we will create a function 
def time():
    string = strftime("%H:%M:%S %p \n %D") # H-Hour, M-minute, S- second, P-am/pm and \n means next line and %D means date
    label.config(text = string)
    label.after(1000, time) # 1000 milliseconds = 1 second
#after that we will create a label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='gray', foreground='black')
#after that we will pack the label
label.pack(anchor='center')

#after that call the function 
time()
#after that we will start the main loop
root.mainloop()
