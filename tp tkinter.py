from tkinter import *


window = Tk()
window.title('Login')
window.geometry('950x500+300+200')
window.configure(bg='white')



frame = Frame(window, width=250, height=350, bg="white")
frame.place(x=170, y=100)


def celsius_to_fahrenheit():
    try:
        celsius_value = float(celsius.get())  
        fahrenheit = (celsius_value * 9/5) + 32  
        result_label.config(text=f"{fahrenheit:.2f}°F")  
    except ValueError:
        result_label.config(text="Invalid input!") 


celsius = Entry(width=70,height=5,fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
celsius.place(x=50, y=100)
celsius.insert(0, 'Enter the value')


button = Button(frame, text="Convert", command=celsius_to_fahrenheit, bg='green', fg='white')
button.place(x=50, y=150)

result_label = Label(frame, text="", bg="white", font=('Microsoft YaHei UI Light', 12, 'bold'))
result_label.place(x=50, y=70)


window.mainloop()
