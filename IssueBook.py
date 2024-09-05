from tkinter import *
def issue():
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
    L2=Label(w,text="Enter your name:",font=('times new roman',24,'bold'),bg='Black',fg='yellow')
    L2.place(x=20,y=150)
    E2=Entry(w,font=('times new roman',20,'bold'),bg='white',fg='black',textvar=b)
    E2.place(x=280,y=150)
    L3=Label(w,text="Phone:",font=('times new roman',24,'bold'),bg='Black',fg='yellow')
    L3.place(x=20,y=220)
    E3=Entry(w,font=('times new roman',20,'bold'),bg='white',fg='black',textvar=c)
    E3.place(x=280,y=220)
    def issued():
        m=a.get()
        n=b.get()
        p=c.get()
        e='Issued';
        cr.execute('update Book set IssuedTo=?,Phone=?,status=? where BookName=?',(n,p,e,m))
        db.commit()
        m = a.set('')
        n = b.set('')
        p = c.set('')
    B1=Button(w,text="Issue",width="25",height=4,font=('times new roman',10,'bold'),command=issued)
    B1.place(x=200,y=270)
    w.mainloop()
