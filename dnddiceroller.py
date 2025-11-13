import random
import tkinter as tk
from tkinter import Toplevel
from tkinter import Label

dice4 = [1,2,3,4]

dice6 = [1,2,3,4,5,6]

dice8 = [1,2,3,4,5,6,7,8]

dice10 = [1,2,3,4,5,6,7,8,9,10]

dice12 = [1,2,3,4,5,6,7,8,9,10,11,12]

dice20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

dice100 = list(range(1,101))

def d4():
    rolled = random.choice(dice4)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d6():
    rolled = random.choice(dice6)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d8():
    rolled = random.choice(dice8)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()


def d10():
    rolled = random.choice(dice10)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d12():
    rolled = random.choice(dice12)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d20():
    rolled = random.choice(dice20)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d100():
    rolled = random.choice(dice100)
    
    result = Toplevel()
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()


root = tk.Tk()
root.title('D&D Dice Roller')
root.geometry('200x220')

title = tk.Label(root,text='D&D Dice Roller', font=('Arial',20))
title.pack()

b1 = tk.Button(root,text='D4',command=d4,font=('Arial'))
b1.pack()

b2 = tk.Button(root,text='D6',command=d6,font=('Arial'))
b2.pack()

b3 = tk.Button(root,text='D8',command=d8,font=('Arial'))
b3.pack()

b4 = tk.Button(root,text='D10',command=d10,font=('Arial'))
b4.pack()

b5 = tk.Button(root,text='D12',command=d12,font=('Arial'))
b5.pack()

b6 = tk.Button(root,text='D20',command=d20,font=('Arial'))
b6.pack()

b7 = tk.Button(root,text='D100',command=d100,font=('Arial'))
b7.pack()

root.mainloop()