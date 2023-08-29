from tkinter import *
from tkinter import messagebox
import os
import listwin
root = Tk()
root.geometry("350x550")
root.title('To-Do List')
lb1 = Label(root, text = "To-Do List", bg = "light blue",font = ("Times Bold Italic", 24))
lb1.pack()

def createlist():
    root1 = Tk()
    root1.geometry("350x550")
    lb1 = Label(root1, text = "Enter the name of the list you want to create.",
    wraplength=300, bg = "light blue",font = ("Times Bold Italic", 15))
    lb1.pack()
    e1 = Entry(root1, width = 35)
    e1.place(x= 58, y = 100)
    def onclick():
        n=e1.get()
        f = open(n+".txt",'x')
        f.close()
        messagebox.showinfo(message = "List successfully created! Go back to the main window")
        root1.destroy()
    b3 = Button(root1, text = "Create",bg='azure3', command = onclick)
    b3.place(x = 150, y = 150)
    root1.mainloop()

def openlist():
    root2 = Tk()
    root2.geometry("350x550")
    lb1 = Label(root2, text = "Enter the name of the list you want to open: ",
     wraplength = 300, bg = "light blue", font = ("Times Bold Italic", 15))
    lb1.pack()
    e2 = Entry(root2, width = 35)
    e2.place(x=58, y=100)

    def new():
        n1 = e2.get()
        listwin.todo_list(n1)
    b4 = Button(root2, text = "Open",bg='azure3', command = new)
    b4.place(x=150, y = 150)
    root2.mainloop()

def dellist():
    root6 = Tk()
    root6.geometry("350x550")
    lb1 = Label(root6, text = "Enter the name of the list you want to delete: ",
    wraplength = 300, bg = "light blue", font = ("Times Bold Italic", 15))
    lb1.pack()
    e2 = Entry(root6, width = 35)
    e2.place(x=58, y=100)

    def new():
        n1 = e2.get()
        os.remove(n1+'.txt')
    
    b4 = Button(root6, text = "Delete",bg='azure3', command = new)
    b4.place(x=150, y = 150)
    root6.mainloop()


b1 = Button(root, text = "Create a list",bg='azure3',font = ("Times Bold Italic", 15), command = createlist)
b1.place(relwidth=0.6,relheight=0.1,relx=0.5,rely=0.2,anchor='n')

b2 = Button(root, text = "Open a list",bg='azure3',font = ("Times Bold Italic", 15), command = openlist)
b2.place(relwidth=0.6,relheight=0.1,relx=0.5,rely=0.4,anchor='n')

b2 = Button(root, text = "Delete a list",bg='azure3',font = ("Times Bold Italic", 15), command = dellist)
b2.place(relwidth=0.6,relheight=0.1,relx=0.5,rely=0.6,anchor='n')

root.mainloop()
