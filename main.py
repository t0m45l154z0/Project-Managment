import tkinter as tk


progresstasks = 1
todotasks     = 1
donetasks     = 1

def typetaskfunc(typen):
    global typetask
    typetask = typen

def createtasks(name, listn):
    global todotasks, progresstasks, donetasks

    if listn == 1:
        newttask = tk.Checkbutton(todoframe, text=name, variable=tk.IntVar(), onvalue=1, offvalue=0)
        newttask.grid(row=todotasks, column=0, padx=5, pady=5)
        todotasks += 1
    
    elif listn == 2:
        newptask = tk.Checkbutton(progressframe, text=name, variable=tk.IntVar(), onvalue=1, offvalue=0)
        newptask.grid(row=progresstasks, column=0, padx=5, pady=5)
        progresstasks += 1

    elif listn == 3:
        newdtask = tk.Checkbutton(doneframe, text=name, variable=tk.IntVar(), onvalue=1, offvalue=0)
        newdtask.grid(row=donetasks, column=0, padx=5, pady=5)
        donetasks += 1

    else:
        print("There was an error in the creation of a new task")


root = tk.Tk()
root.title("Projects Managment")
root.resizable(False, False)
radio = tk.IntVar()


creationframe = tk.Frame()
creationframe.grid(row=0, column=0, rowspan=10, sticky="nsew")
todoframe = tk.Frame()
todoframe.grid(row=0, column=1, rowspan=10, sticky="nsew")
todoframe.config(bg="light blue")
progressframe = tk.Frame()
progressframe.grid(row=0, column=2, rowspan=10, sticky="nsew")
progressframe.config(bg="light green")
doneframe = tk.Frame()
doneframe.grid(row=0, column=3, rowspan=10, sticky="nsew")
doneframe.config(bg="pink")


creationlabel = tk.Label(creationframe, text="Add a New Task")
creationlabel.grid(row=0, column=0, padx=10, pady=10)
textbox = tk.Entry(creationframe)
textbox.grid(row=0, column=0, padx=10, pady=10)
todoradio = tk.Radiobutton(creationframe, text="Things to do", variable=radio, 
                                value=1, command=lambda:typetaskfunc(1))
todoradio.grid(row=1, column=0, padx=5, pady=5)
progressradio = tk.Radiobutton(creationframe, text="In progress", variable=radio, 
                                value=2, command=lambda:typetaskfunc(2))
progressradio.grid(row=2, column=0, padx=5, pady=5)
doneradio = tk.Radiobutton(creationframe, text="Already done", variable=radio, 
                                value=3, command=lambda:typetaskfunc(3))
doneradio.grid(row=3, column=0, padx=5, pady=5)
createbutton = tk.Button(creationframe, text="Add", command=lambda:createtasks(textbox.get(), typetask))
createbutton.grid(row=4, column=0, padx=5, pady=5)


todolabel = tk.Label(todoframe, text="Things to do")
todolabel.grid(row=0, column=0, padx=10, pady=10)
progresslabel = tk.Label(progressframe, text="In progress")
progresslabel.grid(row=0, column=0, padx=10, pady=10)
donelabel = tk.Label(doneframe, text="Already done")
donelabel.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
