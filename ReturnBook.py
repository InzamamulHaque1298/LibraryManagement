from tkinter import *
def ret():
    import sqlite3
    try:
        db=sqlite3.connect('Library.db')
        cr=db.cursor()
        cr.execute('create table Book(BookName text,IssuedTo text,Phone integer,status text)')
        db.commit()
    except:
        print("DataBase Created")

    w=Tk()

    w.geometry("600x600")
    w.title('IssueBook')
    w.config(background="steelblue")
    a=StringVar()
    b=StringVar()
    c=StringVar()
    L1=Label(w,text="Book Name:",font=('times new roman',24,'bold'),bg='Black',fg='yellow')
    L1.place(x=20,y=80)
    E1=Entry(w,font=('times new roman',20,'bold'),bg='white',fg='black',textvar=a)
    E1.place(x=280,y=80)

    def issued():
        m=a.get()

        e='Available';
        cr.execute('update Book set IssuedTo=?,Phone=?,status=? where BookName=?',("-","-",e,m))
        db.commit()
        m = a.set('')
        n = b.set('')
        p = c.set('')
    B1=Button(w,text="Return",width="25",height=4,font=('times new roman',10,'bold'),command=issued)
    B1.place(x=200,y=270)
    w.mainloop()
