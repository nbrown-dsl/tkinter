from tkinter import *
import sqlite3
 
 
root = Tk()
root.title('tkinter address database')
root.geometry("400x600")
 
# Databases
 
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')
 
# Create cursor
c = conn.cursor()
 
# Create table (uncomment and run once then comment in again)
 
# c.execute("""CREATE TABLE addresses (
#      first_name text,
#      last_name text,
#      address text,
#       city text,
#       state text,
#       zipcode integer
#       )""")
# once table created run ALTER TABLE lines uncommented then comment in
# c.execute("""ALTER TABLE addresses
# ADD Email varchar(255)""")
 
c.execute("""CREATE TABLE workplace (
      workplace_name text,
      workplace_url text,
      workplace_tel integer
       )""")
 
# Create Update function to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    record_id = delete_box.get()
 
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode,
        email = :email 
 
        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'email': email_editor.get(),
        'oid': record_id
        })
 
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
    editor.destroy()
    root.deiconify()
 
# validate email
def emailValidation():
 
    emailInput = email.get()
 
    if (emailInput.find("@")<0):
        # root.withdraw()
        global confirm
        confirm = Tk()
        confirm.title('Invalid email')
        confirm.geometry("600x200")
        
        # Create Text Box Labels
        f_name_label = Label(confirm, text="Email invalid",font=("Courier", 24))
        f_name_label.grid(row=0, column=0, pady=(10, 0))
    else:
        submit()
    
# Create Edit function to update a record
def edit():
    # root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x400")
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    record_id = clicked.get()
    #record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    #Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global email_editor
 
    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)
    email_editor = Entry(editor, width=30)
    email_editor.grid(row=6, column=1)
    
    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="Workplace")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    email_label = Label(editor, text="Email")
    email_label.grid(row=6, column=0)
 
    # Loop thru results 
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
        email_editor.insert(0, record[6])
 
    
    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
 
# confirm delete a record
def deleteConfirm():
    global confirm
    confirm = Tk()
    confirm.title('Delete A Record')
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
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
 
    delete_box.delete(0, END)
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :email)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': clickedWorkplace.get(),
                'zipcode': zipcode.get(),
                'email': email.get()
            })
 
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
    email.delete(0, END)
 
def show_id():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT oid FROM addresses")
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
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
 
    # Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[7]) + "\n"
        
 
    query_label = Label(root, text=print_records)
    query_label.grid(row=14, column=0, columnspan=2)
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
def submitWorkSpace():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Insert Into Table
    c.execute("INSERT INTO workplace VALUES (:w_name, :w_url, :w_tel)",
            {
                'w_name': workspace_name.get(),
                'w_url': workspace_url.get(),
                'w_tel': workspace_tel.get()
            })
 
    #Commit Changes
    conn.commit()
 
    # Close Connection 
    conn.close()
 
    # Clear The Text Boxes
    workspace_name.delete(0, END)
    workspace_url.delete(0, END)
    workspace_tel.delete(0, END)
    
 
def addWorkspace():
    global workspace
    workspace = Tk()
    workspace.title('Create workspace')
    workspace.geometry("400x200")
 
    global workspace_name
    global workspace_url
    global workspace_tel
 
    # Create Text Boxes
    workspace_name = Entry(workspace, width=30)
    workspace_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    workspace_url = Entry(workspace, width=30)
    workspace_url.grid(row=1, column=1)
    workspace_tel = Entry(workspace, width=30)
    workspace_tel.grid(row=2, column=1)
 
    # Create Text Box Labels
    workspace_name_label = Label(workspace, text="Workspace name")
    workspace_name_label.grid(row=0, column=0, pady=(10, 0))
    workspace_url_label = Label(workspace, text="URL")
    workspace_url_label.grid(row=1, column=0)
    workspace_tel_label = Label(workspace, text="Telephone")
    workspace_tel_label.grid(row=2, column=0)
 
    # Create Submit Button
    submit_btn = Button(workspace, text="Add Workspace To Database", command=submitWorkSpace)
    submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
 
def listWorkplace():
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
 
    # Query the database
    c.execute("SELECT * FROM workplace")
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
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = OptionMenu(root, clickedWorkplace, *workplaces)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
email = Entry(root, width=30)
email.grid(row=6, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)
 
 
# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="Workplace")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=6, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)
 
# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=emailValidation)
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
edit_btn = Button(root, text="Add workspace", command=addWorkspace)
edit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
 
 
#Commit Changes
conn.commit()
 
# Close Connection 
conn.close()
 
show_id()
 
root.mainloop()
 
 
 
 
 
 
 

