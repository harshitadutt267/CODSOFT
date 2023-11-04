from tkinter import *
from tkinter import messagebox
from tkinter import font

# Create an empty list to store tasks
tasks = []
task_number = 1

def addTask():
    global task_number
    task = txt1.get()
    if task:
        task_with_number = f"{task_number}. {task}"
        tasks.append((task_with_number, False))  # False indicates the task is not completed
        task_number += 1
        txt1.delete(0, END)
        updateTaskField()
        messagebox.showinfo("Task Added", f"Added: {task_with_number}")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def updateTaskField():
    task_field.delete(1.0, END)
    for task, is_completed in tasks:
        task_display = "[x] " if is_completed else "[ ] "
        task_display += task
        task_field.insert(END, task_display + '\n')

def toggleComplete():
    selected_task = task_field.index(INSERT)
    if selected_task:
        index = int(selected_task.split('.')[0]) - 1
        if 0 <= index < len(tasks):
            tasks[index] = (tasks[index][0], not tasks[index][1])  # Toggle completion status
            updateTaskField()

def showTask():
    if tasks:
        updateTaskField()
    else:
        task_field.delete(1.0, END)
        task_field.insert(END, "No tasks added yet.")

def deleteTask():
    global tasks
    try:
        task_number_to_delete = int(txt2.get())
        if 1 <= task_number_to_delete <= len(tasks):
            deleted_task = tasks.pop(task_number_to_delete - 1)
            updateTaskField()
            messagebox.showinfo("Task Deleted", f"Deleted Task: {deleted_task}")
        else:
            messagebox.showwarning("Warning", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid task number.")

def deleteAll():
    global tasks
    tasks = []  # Clear the tasks list
    updateTaskField()  # Update the displayed tasks
def exitW():
    root.destroy()  # Close the Tkinter window

# Create the main Tkinter window
root = Tk()
root.configure(bg='lightblue')
root.title('TO DO LIST')

messagebox.showinfo(title='To Do List', message='My To-Do List')

# Create labels, entry fields, and buttons
lbl1 = Label(root, text='Enter the Task :', padx=10, pady=10, fg='black', bg='antiquewhite')
lbl2 = Label(root, text='Enter the Task Number to delete :', padx=10, pady=10, fg='black', bg='antiquewhite')
txt1 = Entry(root, width=30, borderwidth='3', relief='solid')
txt2 = Entry(root, width=7, borderwidth='2', relief='solid')

btn1 = Button(root, text='Add Task', padx=20, pady=10, command=addTask, bg='pink')
btn3 = Button(root, text='Delete Task', padx=20, pady=10, bg='pink', command=deleteTask)
btn4 = Button(root, text='Delete All Tasks', padx=20, pady=10, bg='pink', command=deleteAll)
btn5 = Button(root, text='Exit', padx=20, pady=10, bg='pink', command=exitW)
toggle_button = Button(root, text="Toggle Complete", command=toggleComplete, bg='pink')

# Grid layout for labels, entry fields, and buttons
lbl1.grid(row=0, column=0)
lbl2.grid(row=2, column=0)
txt1.grid(row=1, column=0, padx=20, pady=20)
txt2.grid(row=2, column=1, padx=20, pady=20)
btn1.grid(row=4, column=0, padx=15, pady=5)
btn3.grid(row=5, column=0, padx=15, pady=5)
btn4.grid(row=6, column=0, padx=15, pady=5)
btn5.grid(row=8, column=0, padx=15, pady=5)
toggle_button.grid(row=7, column=0, padx=15, pady=5)

# Custom font for the text field
custom_font = font.Font(family="Georgia", size=12)

# Create a Frame to contain the Text widget with border and background color
frame = Frame(root, borderwidth=10, relief='groove')
frame.grid(row=0, column=3, rowspan=10, padx=20, pady=20)

# Create a Text widget inside the Frame
task_field = Text(frame, width=20, height=30, wrap=WORD, font=custom_font, bg='peachpuff')
task_field.pack()

# Start the main event loop
root.mainloop()

