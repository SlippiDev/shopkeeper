import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, END
import mysql.connector as mql

def program():
    def add():
        serial_number = e1.get()
        item_name = e2.get()
        item_status = e3.get()
        mydb = mql.connect(
        host = "localhost",
        database = "shopkeeper",
        user = "root",
        password = "4JVkrk75Jamd"
        )
        
        cursor = mydb.cursor()
        sql = "insert into stock (serial_number, item_name, item_status) values (%s,%s,%s)"
        val = (serial_number, item_name, item_status)
        cursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Information", "Added Data Successfully")

    root = tk.Tk()
    root.geometry("800x500")
    title = tk.Label(root, text = "SHOPKEEPER", font = ("Times", 14, "bold", "underline"))
    title.place(x = 300, y = 5)

    l1 = tk.Label(root, text = "Serial Number").place(x = 10, y = 50)

    e1 = tk.Entry(root)
    e1.place(x = 140, y = 50)

    l2 = tk.Label(root, text = "Item Name").place(x = 10, y = 90)

    e2 = tk.Entry(root)
    e2.place(x = 140, y = 90)

    l3 = tk.Label(root, text = "Item Status").place(x = 10, y = 130)

    e3 = tk.Entry(root)
    e3.place(x = 140, y = 130)

    b1 = tk.Button(root, text = "Add", command = add, height=1, width=12).place(x = 30, y = 210)


    root.mainloop()
    


program()