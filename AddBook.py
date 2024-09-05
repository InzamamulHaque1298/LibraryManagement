from tkinter import *
def add():
    import sqlite3
    try:
        db=sqlite3.connect('Library.db')
        cr=db.cursor()
        cr.execute('create table Book(BookName text,IssuedTo text,Phone integer,status text)')
        db.commit()
    except:
        print("DataBase Created")

    w=Tk()
    b = StringVar()
    w.geometry("600x600")
    w.title('AddBook')
    w.config(background="steelblue")
    L1=Label(w,text="Book Name:",font=('times new roman',24,'bold'),bg='Black',fg='yellow')
    L1.place(x=100,y=80)
    E1=Entry(w,font=('times new roman',20,'bold'),bg='white',fg='black',textvar=b)
    E1.place(x=280,y=80)
#add
    def add():
        a=b.get()
        cr.execute('insert into Book(BookName,IssuedTo,Phone,status)values(?,?,?,?)', (a,'-','-','Available'))
        db.commit()
    B1=Button(w,text="Add",width="25",height=4,font=('times new roman',10,'bold'),command=add)
    B1.place(x=200,y=140)
    w.mainloop()
