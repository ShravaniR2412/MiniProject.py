from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shravani0212",
    database="login"
)

cursor = db.cursor()
def sign_in():
    username = user.get()
    password = code.get()

    # Fetch user data from the database
    query = "SELECT * FROM login WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user_data = cursor.fetchone()

    if user_data:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_home_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def open_home_window():
    # Execute the login.py script
    subprocess.run(["python", "Home.py"])

def on_enter(e):
    e.widget.delete(0, 'end')

def on_leave(e):
    if e.widget.get() == '':
        e.widget.insert(0, e.widget.placeholder)

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
user.place(x=30, y=80)
user.placeholder = 'Username'
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11), show='*')
code.place(x=30, y=130)
code.insert(0, 'Password')
code.placeholder = 'Username'
code.insert(0, 'Username')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=35, y=184)

label = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Microsoft yaHei UI Light', 9))
label.place(x=75, y=250)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=250)

root.mainloop()
