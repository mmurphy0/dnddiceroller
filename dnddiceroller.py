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

def showmultiple():
    multiresult = Toplevel()
    multiresult.title('Result')

    dice = dice_entry.get()
    rolls = rolls_entry.get()

    if dice == 'd4' or 'D4':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice4)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()
    
    elif dice == 'd6' or 'D6':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice6)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

    elif dice == 'd8' or 'D8':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice8)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

    elif dice == 'd10' or 'D10':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice10)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

    elif dice == 'd12' or 'D12':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice12)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

    elif dice == 'd20' or 'D20':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice20)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

    elif dice == 'd100' or 'D100':
        l = []
        rolls = int(rolls)
        for i in range(rolls):
            num = random.choice(dice100)
            num = str(num)
            l.append(num)
        rolled = tk.Label(
            multiresult,
            text=l,
            font=('Arial',15)
        )
        rolled.pack()

        l.clear()

        back_button = tk.Button(
            multiresult,
            text='Back',
            font=('Arial',15),
            width=20,
            command=multiresult.destroy
        )
        back_button.pack()

def multiple():
    multiple = Toplevel()
    multiple.geometry('240x130')
    multiple.minsize(240,120)
    multiple.maxsize(240,120)
    multiple.title('How many rolls?')

    global dice_entry, rolls_entry

    multiple_title = tk.Label(
        multiple,
        text='How Many Rolls?',
        font=('Arial',15,'bold')
    )
    multiple_title.grid(
        row=1,
        column=1,
        columnspan=2
    )

    dice_selector = tk.Label(
        multiple,
        text='Dice:',
        font=('Arial',15)
    )
    dice_selector.grid(
        row=2,
        column=1
    )

    dice_entry = tk.Entry(multiple)
    dice_entry.grid(
        row=2,
        column=2
    )

    rolls_label = tk.Label(
        multiple,
        text='Rolls:',
        font=('Arial',15)
    )
    rolls_label.grid(
        row=3,
        column=1
    )

    rolls_entry = tk.Entry(multiple)
    rolls_entry.grid(
        row=3,
        column=2
    )

    roll_button = tk.Button(
        multiple,
        text='Roll',
        font=('Arial',15),
        width=20,
        command=showmultiple
    )
    roll_button.grid(
        row=4,
        column=1,
        columnspan=2
    )


def d4():
    rolled = random.choice(dice4)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d6():
    rolled = random.choice(dice6)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d8():
    rolled = random.choice(dice8)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d10():
    rolled = random.choice(dice10)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d12():
    rolled = random.choice(dice12)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d20():
    rolled = random.choice(dice20)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()

def d100():
    rolled = random.choice(dice100)
    
    result = Toplevel()
    result.title('Result')
    
    l = tk.Label(result,text=rolled, font=('Arial',15))
    l.pack()
    
    b = tk.Button(result,text='Back',command=result.destroy)
    b.pack()


root = tk.Tk()
root.title('D&D Dice Roller')
root.geometry('200x260')
root.minsize(200,260)
root.maxsize(200,260)

title = tk.Label(root,text='D&D Dice Roller', font=('Arial',20))
title.pack()

b1 = tk.Button(
    root,
    text='D4',
    command=d4,
    font=('Arial')
)
b1.pack()

b2 = tk.Button(
    root,
    text='D6',
    command=d6,
    font=('Arial')
)
b2.pack()

b3 = tk.Button(
    root,
    text='D8',
    command=d8,
    font=('Arial')
)
b3.pack()

b4 = tk.Button(
    root,
    text='D10',
    command=d10,
    font=('Arial')
)
b4.pack()

b5 = tk.Button(
    root,
    text='D12',
    command=d12,
    font=('Arial')
)
b5.pack()

b6 = tk.Button(
    root,
    text='D20',
    command=d20,
    font=('Arial')
)
b6.pack()

b7 = tk.Button(
    root,
    text='D100',
    command=d100,
    font=('Arial')
)
b7.pack()

b8 = tk.Button(
    root,
    text='Multiple Rolls',
    font=('Arial',15),
    command=multiple
)
b8.pack()

root.mainloop()