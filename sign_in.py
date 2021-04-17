from tkinter import *
def main_screen():
    mainscreen = Tk()   # create a GUI window 
    mainscreen.geometry("800x800") # set the configuration of GUI window 
    mainscreen.title(" Log In") # set the title of GUI window
# create a Form label 
Label(text="Login Window", bg="blue", width="30", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack()
# create Login Button 
Button(text="Login", height="2", width="30").pack() 
Label(text="").pack() 

# create a Sign in button
Button(text="Sign In", height="2",width="30").pack()
mainscreen.mainloop() # start the GUI

main_screen() # call the main_account_screen() function