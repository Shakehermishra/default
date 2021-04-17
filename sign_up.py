from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Sign Up",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Username/Email:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_1 = Label(root, text="Password:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_1 = Label(root, text="Confirm Password:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)
var = IntVar()

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("Signed Up successfully!!")