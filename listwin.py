from tkinter import * 

def todo_list(n):
    # Importing all the necessary modules
  

    # Initializing the python to do list GUI window
    root2 = Tk()
    root2.title('To-Do List')
    root2.geometry('300x500')
    root2.resizable(0, 0)
    root2.config(bg= "LightCyan2")

    def add_item(entry: Entry, listbox: Listbox):
        new_task = entry.get()
        listbox.insert(END, new_task)
        with open(n+'.txt', 'a') as tasks_list_file:
            tasks_list_file.write(f'{new_task}\n')
        tasks_list_file.close()

    def delete_item(listbox: Listbox):
        l=e3.get()
        
        with open(n+'.txt', 'r') as a:
            lines = a.readlines()

        with open(n+'.txt', 'w') as b:
            
            for i in lines:
                if i.strip('\n') != l:
                    b.write(i)
            
        y=list(listbox.get(0,END))
        for i in y:
            if i.strip('\n')==l:
                listbox.delete(y.index(i))
            #else:
                #listbox.delete(i)


            '''else:
                y.append(i)
'''
        #a=y.index(l)
        
                         
       # listbox.delete(listbox.get(listbox.index(l)))

        '''
            a=listbox.get(ANCHOR)
            for line in lines:
                if line.strip('\n') != a:
                    b.write(line)
                else:
                    pass
        b.close()
        listbox.delete(ANCHOR)
        
            for line in lines:
                if line != listbox.get(ANCHOR):
                    b.write(line)
            b.close()
        listbox.delete(ANCHOR)
        
        
            for i in lines[:-1]:
                b.write(i)
            b.close()
           
        listbox.delete(END)
        '''

        #listbox.delete(ANCHOR)
        #listbox.delete(lines[:-1])
    
    
        

    # Adding and Deleting items functions

    #
    Label(root2, text='To Do List', font=("Comic Sans MS", 15), wraplength=300).place(x=85, y=0)
    # Listbox with all the tasks with a Scrollbar
    tasks = Listbox(root2, selectbackground='azure3', bg='azure3', font=('Helvetica', 12), height=12, width=25)
    scroller = Scrollbar(root2, orient=VERTICAL, command=tasks.yview)
    scroller.place(x=260, y=50, height=232)
    tasks.config(yscrollcommand=scroller.set)
    tasks.place(x=35, y=50)
    # Adding items to the Listbox
    with open(n+'.txt', 'r+') as tasks_list:
        for task in tasks_list:
            print(task)
            tasks.insert(END, task)
        tasks_list.close()
    # Creating the Entry widget where the user can enter a new item
    new_item_entry = Entry(root2, width=37)
    new_item_entry.place(x=35, y=310)
    
    # Creating the Buttons
    add_btn = Button(root2, text='Add Item', bg='azure3', width=20, font=('Helvetica', 12),
                    command=lambda: add_item(new_item_entry, tasks))
    

    # add_btn.place(x=45, y=350)
    add_btn.place(x=45, y=360)
    e3 = Entry(root2, width=37)
    e3.place(x=35, y=420)
    delete_btn = Button(root2, text='Delete Item', bg='azure3', width=20, font=('Helvetica', 12),
                    command=lambda: delete_item(tasks))
    delete_btn.place(x=45, y=450)

    # Finalizing the window
    root2.update()
    root2.mainloop()
