# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:17:33 2021

@author: DELL
"""

from tkinter import *
#import math


def click(event):
    global first_number
    text = event.widget.cget("text")
    if text == "=":
        if first_number.get().isdigit():
            value = int(first_number.get())
        else: 
            try:
                value = eval(screen.get())
                
            except Exception as e:
                print(e)
                value = "Error"
    
        first_number.set(value)
        screen.update()
    
    elif text == "CLEAR":
        first_number.set("")
        screen.update()
        
    else:
        first_number.set(first_number.get() + text)
        screen.update()
        
    """
    elif text == "√":
                value = math.sqrt(first_number.get())
                first_number.set(value)
                screen.update()
    """
    
    



root = Tk()
root.geometry("265x300")
root.configure(background = "orange")

first_number = StringVar()
first_number.set("")

Label(root,text = "HAMLET MANUFACTURERS",font = ("broadway", 12, "bold", "underline") , background = "orange").pack(pady = 10)
        

screen = Entry(root,textvariable = first_number)
screen.pack(ipady = 13,ipadx = 40, pady = 20)
        

b = Button(root,  text = "0", background = "pink", activebackground = "purple", border = 3,padx = 42)
b.place(x = 5, y = 265)
b.bind("<Button-1>", click)

b = Button(root,text = ".", background = "pink", activebackground = "purple", border = 3, padx = 17)
b.place(x = 111, y = 265)
b.bind("<Button-1>", click)

b = Button(root,text = "1", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 5, y = 232)
b.bind("<Button-1>", click)
b = Button(root,text = "2", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 58, y = 232)
b.bind("<Button-1>", click)
b = Button(root,text = "3", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 111, y = 232)
b.bind("<Button-1>", click)
        
b = Button(root,text = "4", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 5, y = 199)
b.bind("<Button-1>", click)
b = Button(root,text = "5", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 58, y = 199)
b.bind("<Button-1>", click)
b = Button(root,text = "6", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 111, y = 199)
b.bind("<Button-1>", click)
        
b = Button(root,text = "7", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 5, y = 166)
b.bind("<Button-1>", click)
b = Button(root,text = "8", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 58, y = 166)
b.bind("<Button-1>", click)
b = Button(root,text = "9", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 111, y = 166)
b.bind("<Button-1>", click)
        
b = Button(root,text = "+", background = "pink", activebackground = "purple", border = 3, padx = 14)
b.place(x = 164, y = 265)
b.bind("<Button-1>", click)
b = Button(root,text = "-", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 164, y = 232)
b.bind("<Button-1>", click)
b = Button(root,text = "*", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 164, y = 199)
b.bind("<Button-1>", click)
b = Button(root,text = "/", background = "pink", activebackground = "purple", border = 3, padx = 15)
b.place(x = 164, y = 166)
b.bind("<Button-1>", click)
        
b = Button(root,text = "=", background = "pink", activebackground = "purple", border = 3, pady = 34, padx = 10)
b.place(x = 217, y = 199)
b.bind("<Button-1>", click)
      
b = Button(root,text = "√", background = "pink", activebackground = "purple", border = 3, padx = 10)
b.place(x = 217, y = 166)
b.bind("<Button-1>", click)
        
b = Button(root,text = "CLEAR", background = "pink", activebackground = "purple", border = 3, padx = 28)
b.place(x = 5, y = 133)
b.bind("<Button-1>", click)
b = Button(root,text = "x^2", background = "pink", activebackground = "purple", border = 3, padx = 8)
b.place(x = 111, y = 133)
b.bind("<Button-1>", click)
b = Button(root,text = "x^3", background = "pink", activebackground = "purple", border = 3, padx = 8)
b.place(x = 164, y = 133)
b.bind("<Button-1>", click)
Button(root,text = "Close", background = "pink", activebackground = "purple", border = 3, command = root.destroy).place(x = 217, y = 133)
    

root.mainloop()