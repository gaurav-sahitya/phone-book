from tkinter import *
from datetime import datetime as dt
from my_contact import *
from add_people import *
date= str(dt.now().date())

class Application():
    def __init__(self,master):
        self.master=master
        self.top=Frame(master,height=150,bg="white").pack(fill=X)
        self.bottom = Frame(master, height=600, bg="#17bd6c").pack(fill=X)
        self.top_image=PhotoImage(file="icons/main.png")
        self.top_image_label=Label(self.top,image=self.top_image,bg="white").place(x=75,y=43)
        self.heading=Label(self.top,text="Phonebook",fg="#0fd478",bg="white",font="arial 32 bold").place(x=150,y=55)
        self.date=Label(self.top,text="Date:\n"+date,fg="#17bd6c",bg="white",font="arial 12").place(x=400,y=90)
        self.add_image=PhotoImage(file="icons/add.png")
        self.add=Button(self.bottom,text="Add Contact",image=self.add_image,compound=LEFT,font="arial 25",bg="#17bd6c",relief="flat",highlightthickness=0,fg="#dadbd9",activebackground="#17bd6c",activeforeground="white",width=360,command=self.add).place(x=57,y=250)
        self.contact_image = PhotoImage(file="icons/contact.png")
        self.contact = Button(self.bottom, text=" My Contact", image=self.contact_image, compound=LEFT, font="arial 25",bg="#17bd6c", relief="flat", highlightthickness=0, fg="#dadbd9",activebackground="#17bd6c",activeforeground="white",command=self.contact,width=360).place(x=57, y=450)

    def contact(self):
        self.master.destroy()
        self.master=Tk()
        self.master.title("My Contact")
        self.master.geometry("500x750")
        self.master.resizable(False, False)
        a=my_contact(self.master)
        self.master.mainloop()
        root = Tk()
        root.title("Phonebook")
        root.geometry("500x750")
        app = Application(root)
        root.resizable(False, False)
        root.mainloop()

    def add(self):
        self.master.destroy()
        self.master=Tk()
        self.master.title("Add New People")
        self.master.geometry("500x750")
        self.master.resizable(False, False)
        add=add_people(self.master)
        self.master.mainloop()
        root = Tk()
        root.title("Phonebook")
        root.geometry("500x750")
        app = Application(root)
        root.resizable(False, False)
        root.mainloop()

def main():
    root=Tk()
    root.title("Phonebook")
    root.geometry("500x750")
    app=Application(root)
    root.resizable(False,False)
    root.mainloop()

if __name__=="__main__":
    main()