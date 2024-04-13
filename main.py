from re import search
from tkinter import *
from tkinter import ttk
import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
engine = create_engine('sqlite:///database.db',echo=True)
Base = declarative_base()
sessions = sessionmaker(bind=engine)
session = sessions()

win=Tk()

win.geometry('1500x800')
humans=[]
class human(Base):
    __tablename__ = 'humans'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    family=Column(String)
    def __init__(self,name='',family=''):
        self.name=name
        self.family=family
Base.metadata.create_all(engine)
#def
def onClickRegister(e):
    #human={'name':txtName.get(),'family':txtFamily.get()}
    human1=human(name=txtName.get(),family=txtFamily.get())
    register(human1)
    LoadData()
def insertTable(human):
    table.insert('','end',values=[human.name,human.family])
def register(human):
    session.add(human)
    session.commit()

def onClickSearch(e):
    dialog=txtSearch.get()
    if dialog=='':
        LoadData()
    else:
        result=search(dialog)
        clearTable()
        for item in result:
            insertTable(item)
def search(dialog):
    alldata=session.query(human).all()
    resultList=[]
    for data in alldata:
        if data.name==dialog or data.family==dialog:
            resultList.append(data)
    return resultList
def clearTable():
    for item in table.get_children():
        table.delete(item)
def LoadData():
    clearTable()
    alldata=session.query(human).all()
    for item in alldata:
        insertTable(item)
#txt1
txtName=Entry(win,)
txtName.place(x=100,y=100)
txtFamily=Entry(win,)
txtFamily.place(x=100,y=140)

txtSearch=Entry(win,)
txtSearch.place(x=600,y=50)
#lbl
lblName=Label(win,text='Name')
lblName.place(x=50,y=100)
lblFamily=Label(win,text='Family')
lblFamily.place(x=50,y=140)

#btn
btnRegister=Button(win,text='Register')
btnRegister.bind('<Button-1>', onClickRegister)
btnRegister.place(x=100,y=200)

btnSearch=Button(win,text='Search')
btnSearch.bind('<Button-1>', onClickSearch)
btnSearch.place(x=500,y=50)
#tbl
coulmns=('Name','Family')
table=ttk.Treeview(win,columns=coulmns,show='headings')
table.heading(coulmns[0],text='Name')
table.heading(coulmns[1],text='Family')
for i in range(2):
    table.column(coulmns[i],width=100)
"""
table.column(coulmns[0],width=100)
table.column(coulmns[1],width=100)
"""
table.place(x=500,y=100)
LoadData()
win.mainloop()