from tkinter import  *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect("database.db")
cur=con.cursor()

class add_people():
    def __init__(self,master):
        self.master=master
        self.top = Frame(master, height=150, bg="white").pack(fill=X)
        self.bottom = Frame(master, height=600, bg="#eb656d").pack(fill=X)
        self.top_image=PhotoImage(file=r"icons/add_01.png")
        self.heading = Label(self.top, text=" Add New People", fg="#eb656d", bg="white", font="arial 32 bold",image=self.top_image,compound=LEFT).place(x=50,y=36)

        self.label_name=Label(self.bottom,text="Name: ").place(x=30,y=200)
        self.entry_name=Entry(self.bottom,width=30)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=100,y=200)

        self.label_surname = Label(self.bottom, text="Surname: ").place(x=30, y=250)
        self.entry_surname = Entry(self.bottom, width=30)
        self.entry_surname.insert(0, "Enter Surname")
        self.entry_surname.place(x=100, y=250)

        self.label_email = Label(self.bottom, text="Email: ").place(x=30, y=300)
        self.entry_email = Entry(self.bottom, width=30)
        self.entry_email.insert(0, "Enter Email")
        self.entry_email.place(x=100, y=300)

        self.label_ph = Label(self.bottom, text="Phone No.: ").place(x=30, y=350)
        self.entry_ph = Entry(self.bottom, width=30)
        self.entry_ph.insert(0, "Enter Phone No.")
        self.entry_ph.place(x=100, y=350)

        self.label_address = Label(self.bottom, text="Address: ").place(x=30, y=400)
        self.entry_address = Text(self.bottom, width=30,height=10)
        self.entry_address.place(x=100, y=400)

        self.button=Button(self.bottom,text="Add Person",command=self.add_person).place(x=200,y=700)

    def add_person(self):
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone_no=self.entry_ph.get()
        address=self.entry_address.get(1.0,"end-1c")
        if all((name,surname,email,phone_no,address)):
            try:
                query ="insert into 'addressbook' (person_name,person_surname,person_email,person_phone,person_address) values(?,?,?,?,?)"
                cur.execute(query,(name,surname,email,phone_no,address))
                con.commit()
                messagebox.showinfo("Success","Contact Added")
            except Exception as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","Fill all the fields",icon="warning")


# root=Tk()
# root.title("Add New People")
# root.geometry("500x750")
# root.resizable(False, False)
# add=add_people(root)
# root.mainloop()
