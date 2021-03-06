from tkinter import *
from tkinter import messagebox
import sqlite3
from add_people import add_people
from update_people import Update
from display import Display

con=sqlite3.connect("database.db")
cur=con.cursor()

class my_contact():
    def __init__(self,master):
        self.master=master
        self.top = Frame(master, height=150, bg="white").pack(fill=X)
        self.bottom = Frame(master, height=600, bg="#eb656d").pack(fill=X)
        self.top_image=PhotoImage(file=r"icons/contact_01.png")
        self.heading = Label(self.top, text="  My Contact", fg="#eb656d", bg="white", font="arial 32 bold",image=self.top_image,compound=LEFT).place(x=90,y=36)
        self.listbox=Listbox(self.bottom,width=36,height=32,bg="white")
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.scroll.config(command=self.listbox.yview)
        self.scroll.place(x=302,y=159,height=581)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.listbox.place(x=10,y=160)

        persons=cur.execute("select * from addressbook").fetchall()
        self.list=[]
        for i in range(len(persons)):
            self.listbox.insert(i,"{}. {} {}".format(i+1,persons[i][1],persons[i][2]))
            self.list.append([persons[i][0], persons[i][1]])

        self.btn_add=Button(self.bottom,text="Add",width=10,font="arial 18",pady=10,command=self.add).place(x=330,y=200)
        self.btn_update = Button(self.bottom, text="Update", width=10, font="arial 18", pady=10,command=self.update).place(x=330, y=300)
        self.btn_display = Button(self.bottom, text="Display", width=10, font="arial 18", pady=10,command=self.display).place(x=330, y=400)
        self.btn_delete = Button(self.bottom, text="Delete", width=10, font="arial 18", pady=10,command=self.delete).place(x=330, y=500)

    def add(self):
        self.master.destroy()
        self.master=Tk()
        self.master.title("Add New People")
        self.master.geometry("500x750")
        self.master.resizable(False, False)
        add=add_people(self.master)
        self.master.mainloop()
        root = Tk()
        root.title("My Contact")
        root.geometry("500x750")
        root.resizable(False, False)
        a = my_contact(root)
        root.mainloop()

    def update(self):
        try:
            person_id = self.list[int(str(self.listbox.curselection())[1:-2])][0]
            self.master.destroy()
            self.master = Tk()
            self.master.title("Update Contact")
            self.master.geometry("500x750")
            self.master.resizable(False, False)
            update_page = Update(self.master,person_id)
            self.master.mainloop()
            root = Tk()
            root.title("My Contact")
            root.geometry("500x750")
            root.resizable(False, False)
            a = my_contact(root)
            root.mainloop()
        except:
            pass

    def display(self):
        try:
            person_id = self.list[int(str(self.listbox.curselection())[1:-2])][0]
            self.master.destroy()
            self.master = Tk()
            self.master.title("Display Contact")
            self.master.geometry("500x750")
            self.master.resizable(False, False)
            display_page = Display(self.master, person_id)
            self.master.mainloop()
            root = Tk()
            root.title("My Contact")
            root.geometry("500x750")
            root.resizable(False, False)
            a = my_contact(root)
            root.mainloop()
        except:
            pass

    def delete(self):
        try:
            person_id = self.list[int(str(self.listbox.curselection())[1:-2])][0]
            person_name = self.list[int(str(self.listbox.curselection())[1:-2])][1]
            query = "delete from addressbook where person_id = {}".format(person_id)
            if messagebox.askquestion("Warning", "Are you sure wanna delete " + person_name + " ?") == "yes":
                try:
                    cur.execute(query)
                    con.commit()
                    messagebox.showinfo("Success", "Deleted")
                    persons = cur.execute("select * from addressbook").fetchall()
                    self.list = []
                    self.listbox.delete("0", "end")
                    for i in range(len(persons)):
                        self.listbox.insert(i, "{}. {} {}".format(i + 1, persons[i][1], persons[i][2]))
                        self.list.append([persons[i][0], persons[i][1]])
                except Exception as e:
                    messagebox.showinfo("Info", str(e))
        except Exception as e:
            print(e)