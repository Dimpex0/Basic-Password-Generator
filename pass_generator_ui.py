from tkinter import *
import random


def generate():
    chars_small = 'abcdefghljklmnopqrstuvwxyz'
    chars_big = 'ABCDEFGHLJKLMNOPQRSTUVWXYZ'
    all = chars_big + chars_small
    password = '1!D'
    for _ in range(10):
        symbol = random.choice(all)
        password += symbol
    l3.config(text=f'{password}')


main = Tk()
main.title('Password Generator')
main.geometry('400x300')
main.resizable()
l1 = Label(main, text='Password Generator', bg='white', font='Helvetica 10')
l1.place(x=120, y=0)
l2 = Label(main, text='Password:', bg='white')
l2.place(x=150, y=50)
l3 = Label(main, text='                           ', bg='white')
l3.place(x=135, y=80)
btn1 = Button(main, text='Generate', bg='white', command=generate)
btn1.place(x=150, y=120)
main.mainloop()
