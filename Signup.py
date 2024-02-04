from tkinter import *
from tkinter import messagebox

def sign_up():
    email_value = email.get()
    username_value = user.get()
    password_value = code.get()
    contact_value = contact.get()

    # Replace this with your authentication logic
    if username_value == "user" and password_value == "password" and email_value == "email" and contact_value == "contact":
        messagebox.showinfo("SignUp Successful", "Welcome, " + username_value + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username, password, email, or contact number")

def on_enter(e):
    e.widget.delete(0, 'end')

def on_leave(e):
    if e.widget.get() == '':
        e.widget.insert(0, e.widget.placeholder)

root = Tk()
root.title('SignUp')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='./images/login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Email Entry
email = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
email.place(x=30, y=80)
email.insert(0, 'Email')
email.placeholder = 'Email'
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

# Username Entry
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
user.place(x=30, y=130)
user.insert(0, 'Username')
user.placeholder = 'Username'
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

# Contact Number Entry
contact = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
contact.place(x=30, y=180)
contact.insert(0, 'Contact Number')
contact.placeholder = 'Contact Number'
contact.bind("<FocusIn>", on_enter)
contact.bind("<FocusOut>", on_leave)

# Password Entry
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11), show='*')
code.place(x=30, y=230)
code.insert(0, 'Password')
code.placeholder = 'Password'
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=207)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=sign_up).place(x=35, y=270)

root.mainloop()
