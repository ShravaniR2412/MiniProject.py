from tkinter import *
from tkinter import messagebox
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shravani0212",
    database="login"
)

cursor = db.cursor()
def sign_up():
    try:
        username = user.get()
        password = code.get()

        # Insert user data into the database
        query = "INSERT INTO login (username, password) VALUES (%s, %s);"
        cursor.execute(query, (username, password))

        # Commit the changes to the database
        db.commit()

        messagebox.showinfo("Registration Successful", "Welcome, " + username + "!")

    except mysql.connector.Error as err:
        # Handle database errors
        messagebox.showerror("Registration Failed", "Error: {}".format(err))
root = Tk()
root.title('Registartion')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Enter your username')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11), show='*')
code.place(x=30, y=130)
code.insert(0, 'Create Password')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)

Button(frame, width=39, pady=7, text='Register', bg='#57a1f8', fg='white', border=0, command=sign_up).place(x=35, y=184)

label = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Microsoft yaHei UI Light', 9))
label.place(x=75, y=250)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=250)

root.mainloop()
