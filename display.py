from tkinter import  *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect("database.db")
cur=con.cursor()

class Display():
    def __init__(self,master,person_id):
        self.person_id=person_id
        query="select * from addressbook where person_id = '{}'".format(person_id)
        result=cur.execute(query).fetchone()
        person_name=result[1]
        person_surname=result[2]
        person_email=result[3]
        person_phone=result[4]
        person_address=result[5]

        self.master = master
        self.top = Frame(master, height=150, bg="white").pack(fill=X)
        self.bottom = Frame(master, height=600, bg="#eb656d").pack(fill=X)
        self.top_image = PhotoImage(file=r"icons/add_01.png")
        self.heading = Label(self.top, text=" Display Contact", fg="#eb656d", bg="white", font="arial 32 bold",
                             image=self.top_image, compound=LEFT).place(x=50, y=36)

        self.label_name = Label(self.bottom, text="Name: ").place(x=30, y=200)
        self.entry_name = Entry(self.bottom, width=30)
        self.entry_name.insert(0,person_name)
        self.entry_name.config(state="disabled")
        self.entry_name.place(x=100, y=200)

        self.label_surname = Label(self.bottom, text="Surname: ").place(x=30, y=250)
        self.entry_surname = Entry(self.bottom, width=30)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.config(state="disabled")
        self.entry_surname.place(x=100, y=250)

        self.label_email = Label(self.bottom, text="Email: ").place(x=30, y=300)
        self.entry_email = Entry(self.bottom, width=30)
        self.entry_email.insert(0,person_email)
        self.entry_email.config(state="disabled")
        self.entry_email.place(x=100, y=300)

        self.label_ph = Label(self.bottom, text="Phone No.: ").place(x=30, y=350)
        self.entry_ph = Entry(self.bottom, width=30)
        self.entry_ph.insert(0, person_phone)
        self.entry_ph.config(state="disabled")
        self.entry_ph.place(x=100, y=350)

        self.label_address = Label(self.bottom, text="Address: ").place(x=30, y=400)
        self.entry_address = Text(self.bottom, width=30, height=10)
        self.entry_address.insert(1.0,person_address)
        self.entry_address.config(state="disabled")
        self.entry_address.place(x=100, y=400)