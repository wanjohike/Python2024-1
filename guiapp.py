#Libraries that we use to create a GUI
# TKinter, wxPython, PyGTK, PyQT
# Widets and tools to create a user interface

# TK - TK interface
# helloword application
import tkinter as tk

root = tk.Tk()
# the main window of tkinter is called root, however use any other name

root.geometry('480x240')
root.resizable(False,False) # fixed size
root.title('Tkinter Example')
# create a widget to display the text hello world
hello = tk.Label(root, text = 'Hello World')
hello.pack() #this embeds the label to the main window

ok = tk.Button(root, text= 'OK', command=lambda: root.quit())
ok.pack()

# Change the position of the exit button
ipdadx = 5
ipdady = 5
expand=True

# adding an image to a button


root.mainloop() #the main loop ensures that the main window remain visible on the screen
