from tkinter import *
from tkinter.ttk import Treeview
from customtkinter import *
import tkinter as tk
from db_con import connect_to_database

def update(rows):
    for i in rows:
        trv.insert('', 'end', values=i)

root = Tk()
root.geometry("1000x700")
VTable = LabelFrame (root, width=960, height=500, background="white")
VTable.place(relx=0.5, rely=0.6, anchor="center")

trv = Treeview(VTable, columns=(1,2,3,4,5,6,7), show="headings", height="10")
trv.pack()

trv.heading(1, text="Name")
trv.heading(2, text="Date")
trv.heading(3, text="Log In Time")
trv.heading(4, text="Log Out Time")
trv.heading(5, text="Resident")
trv.heading(6, text="Purpose")
trv.heading(7, text="Guard")

conn = connect_to_database()
cursor = conn.cursor()
query = """
SELECT visit_name, log_day, login_time, logout_time, log_purpose,  res_id, sec_id
FROM visitor_data
"""
cursor.execute(query)
rows = cursor.fetchall()
update(rows)



root.mainloop()