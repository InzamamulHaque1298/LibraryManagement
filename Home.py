from tkinter import *

from AddBook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *

w=Tk()
w.geometry('900x600')
w.title('Frame')
f1=Frame(w,background='Green')
f1.place(x=100,y=10,width=700,height=70)
l1=Label(f1,text="Library Management System",font=('times new roman',20,'bold'),bg='steelblue',fg='yellow')
l1.place(x=150,y=12)
#import
def Add():
    add()
def View():
    view()
def delete():
    delet()
def Issue():
     issue()
def Return():
     ret()

#Links
B1=Button(text="AddBook",width=14,height=1,font=('times new roman',20,'bold'),bg='LightBlue',fg='Black',command=Add)
B1.place(x=330,y=120)
B2=Button(text="ViewBook",width=14,height=1,font=('times new roman',20,'bold'),bg='LightBlue',fg='Black',command=View)
B2.place(x=330,y=180)
B3=Button(text="DeleteBook",width=14,height=1,font=('times new roman',20,'bold'),bg='LightBlue',fg='Black',command=delete)
B3.place(x=330,y=240)
B4=Button(text="IssueBook",width=14,height=1,font=('times new roman',20,'bold'),bg='LightBlue',fg='Black',command=Issue)
B4.place(x=330,y=300)
B5=Button(text="ReturnBook",width=14,height=1,font=('times new roman',20,'bold'),bg='LightBlue',fg='Black',command=Return)
B5.place(x=330,y=360)
w.mainloop()