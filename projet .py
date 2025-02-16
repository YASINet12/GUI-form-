from tkinter import *     
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


conn = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_data"
    )
except Error as e:
    print("Error connecting to database:", e)


root = Tk()  
root.title('Login')
root.geometry('950x500+300+200')
root.configure(bg='pink')
root.resizable(False, False)


img = Image.open("image1.png") 
img = ImageTk.PhotoImage(img)
label = Label(root, image=img, bg="pink", width=500, height=360)
label.place(x=50, y=40)


frame = Frame(root, width=450, height=350, bg="pink")
frame.place(x=480, y=100)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='pink', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Input fields
user = Entry(frame, width=25, fg='black', border=1, bg='lightgrey', font=('Microsoft YaHei UI Light', 11, 'bold'))
user.place(x=30, y=80)
user.insert(0, 'Username')

email = Entry(frame, width=25, fg='black', border=1, bg='lightgrey', font=('Microsoft YaHei UI Light', 11, 'bold'))
email.place(x=30, y=120)
email.insert(0, 'Email')

message = Text(frame, width=25, height=5, fg='black', border=1, bg='lightgrey', font=('Microsoft YaHei UI Light', 11, 'bold'))
message.place(x=30, y=165)
message.insert(1.0, 'Message')


def insert_data():
    global conn

    if conn is None or not conn.is_connected():
        messagebox.showinfo("Error", "Database connection is not available")
        return

    username = user.get().strip()
    address_mail = email.get().strip()
    user_message = message.get("1.0", "end-1c").strip()

    if username == '' or address_mail == '' or user_message == '' or username == "Username" or address_mail == "Email" or user_message == "Message":
        messagebox.showinfo("Error", "Please enter all fields")
        return

    try:
        pst = conn.cursor()

        
        sql_query = f"INSERT INTO data_py (username, adress_mail, text_meassage) VALUES ('{username}', '{address_mail}', '{user_message}')"
        
        pst.execute(sql_query)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
        pst.close()
        
        user.delete(0, END)
        email.delete(0, END)
        message.delete("1.0", END)

       
        user.insert(0, 'Username')
        email.insert(0, 'Email')
        message.insert("1.0", 'Message')

    except Error as e:
        messagebox.showinfo("Error", "Database Insertion Failed")
        print(e)

Button = Button(frame, text='Send', width=20, height=2, bg='green', fg='white', command=insert_data)
Button.place(x=75, y=275)



root.mainloop()
