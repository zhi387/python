#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Tkinter import *

class sqlTool:
    def __init__(self):
        self.win = Tk()
        self.win.title("sql-tool")
        self.win.geometry("600x400")
    
    def run(self):
        menubar = Frame(self.win,relief=RAISED,borderwidth=1)
        menubar.pack(fill=X)
        cmdbutton1 = Menubutton(menubar, text="links",underline=0)
        cmdbutton1.pack(side=LEFT, padx="2m")
        cmdbutton1.menu = Menu(cmdbutton1)
        cmdbutton1.menu.add_command(label="mssql",underline=0,command=self.mssql)
        cmdbutton1.menu.add_command(label="mysql",underline=0,command=self.mysql)
        cmdbutton1.menu.add("separator")
        cmdbutton1.menu.add_command(label="quit",underline=0,command=self.win.destroy)
        cmdbutton1['menu'] = cmdbutton1.menu
        cmdbutton2 = Menubutton(menubar, text="links",underline=0)
        cmdbutton2.pack(side=LEFT, padx="2m")
        cmdbutton2.menu = Menu(cmdbutton2)
        cmdbutton2.menu.add_command(label="exp_xls",underline=0,command=self.exp_xls)
        cmdbutton2.menu.add_command(label="exp_dbf",underline=0,command=self.exp_dbf)
        cmdbutton2['menu'] = cmdbutton2.menu    
        menubar.tk_menuBar(cmdbutton1)
        menubar.tk_menuBar(cmdbutton2)
        self.win.mainloop()
        
    def mssql(self):
        print("mssql")
        
    def mysql(self):
        print("mysql")
        
    def exp_xls(self):
        print("exp_xls")
         
    def exp_dbf(self):
        print("exp_dbf")

mytool = sqlTool()
mytool.run()
