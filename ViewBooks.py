from tkinter import *
def view():

    import sqlite3

    try:
        db = sqlite3.connect('Library.db')
        cr = db.cursor()
        cr.execute('create table Book(BookName text,IssuedTo text,Phone integer,Status text)')
        db.commit()
    except:
        print("DataBase Created")

    w = Tk()
    x=StringVar()
    eq_label=StringVar()
    w.geometry("600x600")
    w.config(background="steelblue")
    L1=Label(w,text="View Books:",font=('times new roman',24,'bold'),bg='Black',fg='yellow')
    L1.place(x=200,y=100)
    L2=Label(w,textvariable=eq_label,font=('times new roman',24,'bold'),bg='White',fg='Black',width=30,height=8)
    L2.place(x=10,y=250)
    #display
    def display():
        a=x.get()
        cr.execute('select BookName from Book')

        data=cr.fetchmany(2)
        eq_label.set(data);
        B5 = Button(w, text="Next 2 Books", width="25", height=4, font=('times new roman', 10, 'bold'), command=next)
        B5.place(x=400, y=150)



    B1=Button(w,text="View",width="25",height=4,font=('times new roman',10,'bold'),command=display)
    B1.place(x=200,y=150)


    def next():
        data = cr.fetchmany(2)
        eq_label.set(data);
    w.mainloop()
