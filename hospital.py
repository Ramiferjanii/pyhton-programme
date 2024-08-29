from tkinter import*
from tkinter import ttk 
import random 
import time 
import datetime
from tkinter import messagebox 
import mysql.connector


class hospital : 
    def __init__(self,root):
        self.root = root 
        self.root.title(" Hospital Managment system ")
        self.root.geometry("1540×400+0+0")

root = Tk()
ob=hospital(root)
root.mainloop()

