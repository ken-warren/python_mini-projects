# load the required libraries
from tkinter import *
from time import strftime

# define the windows your clock will be in
myWindow = Tk()
myWindow.title('My Clock')

# Format
def time():
    myTime = strftime('%H: %M: %S: %p')
    clock.config(text = myTime)
    clock.after(1000, time)
    
clock = Label(myWindow, font = ('san francisco', 40, 'bold'),
              background='dark green',
              foreground='white')
clock.pack(anchor = 'center')
time()

mainloop()