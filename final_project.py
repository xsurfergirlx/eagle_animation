# import required modules 
import tkinter as tk 
from tkinter import *
from PIL import Image 
from PIL import ImageTk 


# bidirectional class
class bidirectional_iterator:
    def __init__(self):
        self.data = [frame_001, frame_002, frame_003, frame_004, frame_005, frame_006, frame_007, frame_008, frame_009, frame_010, frame_011]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            self.index = 0 # sets up the infinite scrolling, resets if index goes too high
        return self.data[self.index]

    def __reversed__(self):
        self.index -= 1
        if self.index == -1:
            self.index = 10 # sets up the infinite scrolling, resets if index goes too low
        return self.data[self.index]
  
DELAY = 0.001 
  
# adjust window 
window = Tk()  # create root window
window.title("Eagle Animation")
window.geometry("700x900") 
# setting the minimum size of the root window
window.minsize(700, 900)


# Configure all rows and columns to expand equally
num_rows = 2  # Number of rows
num_cols = 10  # Number of columns
for i in range(num_rows):
    window.grid_rowconfigure(i, weight=1)
for j in range(num_cols):
    window.grid_columnconfigure(j, weight=1)
# Assign higher weight to the display row and the last column
window.grid_rowconfigure(0, weight=2)  # Display row

panel = tk.Label(window)
panel.grid(row=0, column=1, columnspan=7)

  
# loading the images 
frame_001 = ImageTk.PhotoImage(Image.open("images/frame_001.png").resize((800, 800))) 
frame_002 = ImageTk.PhotoImage(Image.open("images/frame_002.png").resize((800, 800))) 
frame_003 = ImageTk.PhotoImage(Image.open("images/frame_003.png").resize((800, 800)))
frame_004 = ImageTk.PhotoImage(Image.open("images/frame_004.png").resize((800, 800))) 
frame_005 = ImageTk.PhotoImage(Image.open("images/frame_005.png").resize((800, 800))) 
frame_006 = ImageTk.PhotoImage(Image.open("images/frame_006.png").resize((800, 800))) 
frame_007 = ImageTk.PhotoImage(Image.open("images/frame_007.png").resize((800, 800))) 
frame_008 = ImageTk.PhotoImage(Image.open("images/frame_008.png").resize((800, 800))) 
frame_009 = ImageTk.PhotoImage(Image.open("images/frame_009.png").resize((800, 800))) 
frame_010 = ImageTk.PhotoImage(Image.open("images/frame_010.png").resize((800, 800))) 
frame_011 = ImageTk.PhotoImage(Image.open("images/frame_011.png").resize((800, 800))) 


# add frames to a list
frame_list = bidirectional_iterator()
frame_list_itr = iter(frame_list)


# set pause to false
is_paused = tk.BooleanVar()  # variable to hold the pause/resume state
is_paused.set(True)
img = frame_001
i = 0


# function to show the next image if not paused and then try again in 50
def show_next_image():
    if not is_paused.get():
        global img
        img = next(frame_list_itr)  # get the next image from the iterator   

        # load the image and display it
        panel.Image = img
        panel.configure(background="skyblue")
        panel["image"] = img

    window.after(50, show_next_image)


# function for setting button states when pause button active
def pause_image(): 
    is_paused.set(True)  
    enable_button(play_sequence)
    enable_button(forward_sequence)
    enable_button(rewind_sequence)
    disable_button(pause_sequence)


# function for setting button states when play button active
def play_image(): 
    is_paused.set(False)
    enable_button(pause_sequence)
    disable_button(play_sequence)
    disable_button(forward_sequence)
    disable_button(rewind_sequence)


# function for stop button just quits the screen
def stop_image():
    window.quit()


# function for fast forward button
def forward_image():
    global img
    img = next(frame_list_itr)  # get the next image from the iterator     

    # load the image and display it
    panel.Image = img
    panel["image"] = img


# function for rewind button
def rewind_image():
    global img
    img = reversed(frame_list_itr)  # get the previous image from the iterator     

    # load the image and display it
    panel.Image = img
    panel["image"] = img


def info_window():
    # Toplevel object which will 
    # be treated as a new window
    info_window = Toplevel(window)
 
    # sets the title of the new window
    info_window.title("Help")
 
    # sets the geometry of toplevel
    info_window.geometry("600x150")
    info_window.resizable(False,False)
 
    # Adding a new window to show help screen
    Label(info_window, 
          text ="Press play button to start the animation.\n"
                "Press pause button to pause the animation.\n"
                "Press rewind button to rewind by one frame.\n"
                "Press forward button to advance by one frame.\n"
                "Press stop button to exit the animation and close the window.",
                font="Ariel, 14").pack()


# function to disable a button
def disable_button(button):
    button.config(state=tk.DISABLED)

# function to enable a button
def enable_button(button):
    button.config(state=tk.NORMAL)

# select image for rewind button
rewind_button = PhotoImage(file="images/rewind_btn.png")
rewind_sequence = tk.Button(window, image=rewind_button, command=rewind_image)

# select image for play button
play_button = PhotoImage(file="images/play_btn.png")
play_sequence = tk.Button(window, image=play_button, command=play_image)


# select image for pause button
pause_button = PhotoImage(file="images/pause_btn.png")
pause_sequence = tk.Button(window, image=pause_button, command=pause_image)

# select image for stop button
stop_button = PhotoImage(file="images/stop_btn.png")
stop_sequence = tk.Button(window, image=stop_button, command=stop_image)

# select image for forward button
forward_button = PhotoImage(file="images/forward_btn.png")
forward_sequence = tk.Button(window, image=forward_button, command=forward_image)

# select image for info button
info_button = PhotoImage(file="images/info_btn.png")
info_sequence = tk.Button(window, image=info_button, command=info_window)


# display the components
rewind_sequence.grid(row=7, column=2)
play_sequence.grid(row=7, column=3)
pause_sequence.grid(row=7, column=4)
stop_sequence.grid(row=7, column=5)
forward_sequence.grid(row=7, column=6)
info_sequence.grid(row=7, column=7)

# show the first image
panel.Image = img
panel.configure(background="skyblue")
panel["image"] = img

enable_button(play_sequence)
disable_button(pause_sequence)

# start display loop
show_next_image()

window.mainloop() 