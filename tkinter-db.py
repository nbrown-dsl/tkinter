from tkinter import *
import sqlite3
 
 
root = Tk()
root.title('tkinter PE database')
root.geometry("400x600")
 
# Databases
 
# Create a database or connect to one
conn = sqlite3.connect('PE.db')
 
# Create cursor
c = conn.cursor()
 
# Create table (uncomment and run once then comment in again)
 
# c.execute("""CREATE TABLE time (
#      time integer,
#      student_name text    
#       )""")

 
# c.execute("""CREATE TABLE student (
#       student_name text,
#       student_class text      
#        )""")
 
# Create Update function to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    record_id = delete_box.get()
 
    c.execute("""UPDATE time SET
        time = :time
        
        WHERE oid = :oid""",
        {
        'time': time_editor.get(),       
        'oid': record_id
        })
 
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
    editor.destroy()
    root.deiconify()
 

# Create Edit function to update a record
def edit():
    # root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x400")
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
    record_id = clicked.get()
    #record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM time WHERE oid = " + record_id)
    records = c.fetchall()
    
    #Create Global Variables for text box names
    global time_editor
    
 
    # Create Text Boxes
    time_editor = Entry(editor, width=30)
    time_editor.grid(row=2, column=1)
    
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    
    
    # Create Text Box Labels
    time_label = Label(editor, text="Time")
    time_label.grid(row=1, column=0)
    
    state_label = Label(editor, text="Student")
    state_label.grid(row=4, column=0)
    
 
    # Loop thru results 
    for record in records:
        time_editor.insert(0, record[0])
        state_editor.insert(0, record[1])
    
    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Save time", command=update)
    edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
 
# confirm delete a record
def deleteConfirm():
    global confirm
    confirm = Tk()
    confirm.title('Delete A time')
    confirm.geometry("600x200")
    
    # Create Text Box Labels
    f_name_label = Label(confirm, text="Do you want to delete record?",font=("Courier", 24))
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    
    yes_btn = Button(confirm, text="Yes",font=("Courier", 34),bg="Red", command=delete)
    yes_btn.grid(row=2, column=0, columnspan=1, pady=10, padx=10) 
 
# Create Function to Delete A Record
def delete():
    confirm.destroy()
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Delete a record with id entered 
    c.execute("DELETE from time WHERE oid = " + delete_box.get())
 
    delete_box.delete(0, END)
 
    
    conn.commit()
    conn.close()
 
# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Insert Into Table
    c.execute("INSERT INTO time VALUES (:time, :state)",
            {
                'time': time.get(),
                
                'state': clickedWorkplace.get()               
            })
 
    conn.commit()
    conn.close()
 
    # Clear The Text Boxes
    time.delete(0, END)
    
 
def show_id():
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT oid FROM time")
    records = c.fetchall()
    # print(records)
 
    options = []
    global clicked 
    clicked = StringVar()
    
    
    # Loop Thru Results (comment out on first run, add record then uncomment)
    if len(records)>1:
        print_records = ''
        for record in records:
            options.append(str(record[0]))
    
        clicked.set(options[0])
        drop = OptionMenu(root, clicked, *options)
        drop.grid(row=21, column=0, columnspan=2) 
        print(options)  
 
# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT *, oid FROM time")
    records = c.fetchall()
    # print(records)
 
    # Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record[2]) + "   "  + str(record[0]) + "   " + str(record[1]) + "\n"
        print (record)    
 
    query_label = Label(root, text=print_records)
    query_label.grid(row=14, column=0, columnspan=2)
 
    conn.commit()
    conn.close()
 
def submitWorkSpace():
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Insert Into Table
    c.execute("INSERT INTO student VALUES (:w_name, :w_class)",
            {
                'w_name': student_name.get(),
                'w_class': student_class.get()
                
            })
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
    # Clear The Text Boxes
    student_name.delete(0, END)
    student_class.delete(0, END)
    
    
 
def addWorkspace():
    global workspace
    workspace = Tk()
    workspace.title('Add student')
    workspace.geometry("400x200")
 
    global student_name
    global student_class
    
 
    # Create Text Boxes
    student_name = Entry(workspace, width=30)
    student_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    student_class = Entry(workspace, width=30)
    student_class.grid(row=1, column=1)
    
 
    # Create Text Box Labels
    student_name_label = Label(workspace, text="Student name")
    student_name_label.grid(row=0, column=0, pady=(10, 0))
    student_class_label = Label(workspace, text="Class")
    student_class_label.grid(row=1, column=0)
    
    # Create Submit Button
    submit_btn = Button(workspace, text="Add student To Database", command=submitWorkSpace)
    submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
 
def listWorkplace():
    
    # Create a database or connect to one
    conn = sqlite3.connect('PE.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT * FROM student")
    records = c.fetchall()
    # print(records)
 
    options = [""]
    
    # Loop Thru Results (comment out on first run, add record then uncomment)
    print_records = ''
    for record in records:
        options.append(str(record[0]))
 
    print(options)
    
    return options 
 
 
workplaces = listWorkplace()
clickedWorkplace= StringVar()
clickedWorkplace.set("select")
 
# Create Text Boxes
time = Entry(root, width=30)
time.grid(row=0, column=1, padx=20, pady=(10, 0))

state = OptionMenu(root, clickedWorkplace, *workplaces)
state.grid(row=4, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)
 
 
# Create Text Box Labels
time_label = Label(root, text="time")
time_label.grid(row=0, column=0)

state_label = Label(root, text="Student")
state_label.grid(row=4, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)
 
# Create Submit Button
submit_btn = Button(root, text="Add time", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
 
# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
 
#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=deleteConfirm)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
 
# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
 
# Create a workspace Button
edit_btn = Button(root, text="Add student", command=addWorkspace)
edit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
 
 
#Commit Changes
conn.commit()
 
# Close Connection 
conn.close()
 
show_id()
 
root.mainloop()
 
 
 
 
 
 
 

