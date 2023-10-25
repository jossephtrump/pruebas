from tkinter import *

import tkinter as tkinter
import customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
import MySQLdb as mysql
mydb = mysql.connect(host='localhost',user='root',passwd='',db='colegio')
cur = mydb.cursor()


def inscripcion():
    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("700x600")
    mwindow.title("Registro")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")

    global cedula_entry
    
    cedula_entry = StringVar()

    inscripcion = Label(mwindow,text="ingrese la cedula ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    cedula_entry= Entry(mwindow,)
    
