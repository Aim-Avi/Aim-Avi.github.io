from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

def mymap():
    root = Tk()
    root.geometry("768x1024")
    root.minsize(768, 1024)
    root.maxsize(768, 1024)
    myFont = font.Font(family='Consolas', size=15)
    mapl = Label(root, text="Map for Arpt #1")
    mapl.config(font=("Consolas", 15))
    mapl.place(relx=0.8, rely=0.1, anchor='center')
    ll1 = Label(root, text="Clear for Landing on 09R")
    ll1.config(font=("Consolas", 15))
    ll1.place(relx=0.5, rely=0.55, anchor='center')
    ll2 = Label(root, text="Taxi to Gate 2 via B1 to C1 after holding for 5 mins")
    ll2.config(font=("Consolas", 15))
    ll2.place(relx=0.5, rely=0.58, anchor='center')
    btnn = Button(root, text='End', bg='black', fg='white', command=root.destroy)
    btnn.place(relx=0.5, rely=0.63, anchor='center')
    btnn['font'] = myFont
    ll3 = Label(root, text="Press End after fullstop")
    ll3.config(font=("Consolas", 10))
    ll3.place(relx=0.5, rely=0.67, anchor='center')
    img = Image.open("arpmap.jpg")
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    map = Label(root, image=tkimage).grid()
    map.place(x=40, y =40)
    root.mainloop()