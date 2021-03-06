#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Tkinter import *
import sql.mssql

class sqlTool:
    def __init__(self):
        self.win = Tk()
        self.win.title("sql-tool")
        self.win.geometry("600x400")
        self.menubar = Frame(self.win,relief=RAISED,borderwidth=1)
        self.menubar.pack(fill=X)
    
    def show(self):
        self.addLinkMenu()
        self.addExpMenu()
        self.addButton()
        self.addSqlEntry()
        self.win.mainloop()
        self.sqltext = None
        self.showtext = None
        
    def addLinkMenu(self):
        cmdbutton1 = Menubutton(self.menubar, text="links",underline=0)
        cmdbutton1.pack(side=LEFT, padx="1m")
        cmdbutton1.menu = Menu(cmdbutton1)
        cmdbutton1.menu.add_command(label="mssql",underline=0,command=self.mssql)
        cmdbutton1.menu.add_command(label="mysql",underline=0,command=self.mysql)
        cmdbutton1.menu.add("separator")
        cmdbutton1.menu.add_command(label="quit",underline=0,command=self.win.destroy)
        cmdbutton1['menu'] = cmdbutton1.menu
        self.menubar.tk_menuBar(cmdbutton1)

    def addExpMenu(self):
        cmdbutton2 = Menubutton(self.menubar, text="export",underline=0)
        cmdbutton2.pack(side=LEFT, padx="1m")
        cmdbutton2.menu = Menu(cmdbutton2)
        cmdbutton2.menu.add_command(label="exp_xls",underline=0,command=self.exp_xls)
        cmdbutton2.menu.add_command(label="exp_dbf",underline=0,command=self.exp_dbf)
        cmdbutton2['menu'] = cmdbutton2.menu
        self.menubar.tk_menuBar(cmdbutton2)

    def addSqlEntry(self):
        self.sqltext = Text(self.win)
        self.sqltext.pack(side=LEFT)
        self.showtext = Text(self.win)
        self.showtext.pack(side=LEFT)

    def addButton(self):
        exebutton = Button(self.win, text="execute", command = self.sqlExecute)
        exebutton.pack(side=LEFT)
        
    def mssql(self):
        print("mssql")
        
    def mysql(self):
        print("mysql")
        
    def exp_xls(self):
        print("exp_xls")
         
    def exp_dbf(self):
        print("exp_dbf")

    def sqlExecute(self):
        text = (self.sqltext.get(1.0,END))
        ms = sql.mssql.MSSQL(host="localhost",user="sa",pwd="sasa",db="ks")
        resList = ms.ExecQuery(text.encode("utf8"))
        self.showtext.delete(1.0,END)
        self.showtext.insert(1.0,resList)

mytool = sqlTool()
mytool.show()
