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
        email=emailid.get()
        contact_no=contact.get()

        # Insert user data into the database
        query = "INSERT INTO login (username, password,email,contact_no) VALUES (%s, %s,%s,%s);"
        cursor.execute(query, (username, password,email,contact_no))

        # Commit the changes to the database
        db.commit()

        messagebox.showinfo("Registration Successful", "Welcome, " + username + "!")

    except mysql.connector.Error as err:
        # Handle database errors
        messagebox.showerror("Registration Failed", "Error: {}".format(err))


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

# img = PhotoImage(file='./images/login.png')
img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=500, height=550, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Email Entry
emailid = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft yaHei UI Light', 11))
emailid.place(x=30, y=80)
emailid.insert(0, 'Email')
emailid.placeholder = 'Email'
emailid.bind("<FocusIn>", on_enter)
emailid.bind("<FocusOut>", on_leave)

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
