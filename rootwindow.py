
from tkinter import *

# Create a function to close current window and open a new window
def open_new_window():
    # Close current window
    root.destroy()
    
    # Create new window
    new_window = Tk()
    new_window.title("New Window")
    label = Label(new_window, text="This is a new window.")
    label.pack()
    new_window.mainloop()

# Create the main window
root = Tk()
root.title("Main Window")
label = Label(root, text="This is the main window.")
label.pack()

# Create a button to open a new window
button = Button(root, text="Open New Window", command=open_new_window)
button.pack()

# Start the event loop
root.mainloop()