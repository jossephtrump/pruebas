from tkinter import *
import tkinter as tkinter
import customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
import MySQLdb as mysql
from datetime import *
import tkinter as tk

from tkinter import ttk
mydb = mysql.connect(host='localhost',user='root',passwd='',db='colegio')
cur = mydb.cursor()


def consulta_alumnos():


    
    def vaciar_tabla():
        filas = tvEstudiante.get_children()
        for fila in filas:
            tvEstudiante.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        sql="select * from alumno where cedula = '{0}'".format(cedula_entry.get())
        cur.execute(sql)
        filas = cur.fetchall()
        for fila in filas:
            cedula= fila[0]
            tvEstudiante.insert("", END,cedula , text=cedula, values= fila )


    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("600x600")
    mwindow.title("Consultas")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")

    global cedula_entry

    cedula_entry = StringVar()

    tvEstudiante = ttk.Treeview(mwindow)
    tvEstudiante.grid(column=0,row=3, columnspan=4)
    tvEstudiante["columns"]=("cedula","representante","nombre","direccion","telefono","pago","curso")

    tvEstudiante.column("#0", width=0, stretch=NO)
    tvEstudiante.column("cedula", width=125, anchor=CENTER)
    tvEstudiante.column("representante", width=125, anchor=CENTER)
    tvEstudiante.column("nombre", width=100, anchor=CENTER)
    tvEstudiante.column("direccion", width=100, anchor=CENTER)
    tvEstudiante.column("telefono", width=100, anchor=CENTER)
    tvEstudiante.column("pago", width=75, anchor=CENTER)
    tvEstudiante.column("curso", width=75, anchor=CENTER)
    
    tvEstudiante.heading("#0", text="")
    tvEstudiante.heading("cedula",text="cedula",anchor=CENTER)
    tvEstudiante.heading("representante",text="representante",anchor=CENTER)
    tvEstudiante.heading("nombre",text="nombre",anchor=CENTER)
    tvEstudiante.heading("direccion",text="direccion",anchor=CENTER)
    tvEstudiante.heading("telefono",text="telefono",anchor=CENTER)
    tvEstudiante.heading("pago",text="pago",anchor=CENTER)
    tvEstudiante.heading("curso",text="curso",anchor=CENTER)

    cedula_entry = Entry(mwindow, textvariable=cedula_entry, font=("Cambria", 16),justify='center',
                          width=20)
    cedula_entry.place(x=220, y=390)
    submit_btn = CTkButton(mwindow, text="BUSCAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                         command=llenar_tabla) 
    submit_btn.place(x=301, y=450)


    
    mwindow.mainloop()
 
    
def consulta_curso():
    print("ayuda")


def consulta_representante():
    def vaciar_tabla():
        filas = tvEstudiante.get_children()
        for fila in filas:
            tvEstudiante.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        sql="select * from representante where cedula= '{0}'".format(cedula_entry.get())
        cur.execute(sql)
        filas = cur.fetchall()
        for fila in filas:
            cedula= fila[0]
            tvEstudiante.insert("", END,cedula , text=cedula, values= fila )

     

    global cedula_entry

    cedula_entry = StringVar()



    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("600x600")
    mwindow.title("Consultas")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")

    tvEstudiante = ttk.Treeview(mwindow)
    tvEstudiante.grid(column=0,row=3, columnspan=4)
    tvEstudiante["columns"]=("cedula","nombre","direccion","telefono","numero_alumnos","correo")

    tvEstudiante.column("#0", width=0, stretch=NO)
   
    tvEstudiante.column("cedula", width=125, anchor=CENTER)
    tvEstudiante.column("nombre", width=100, anchor=CENTER)
    tvEstudiante.column("direccion", width=100, anchor=CENTER)
    tvEstudiante.column("telefono", width=100, anchor=CENTER)
    tvEstudiante.column("numero_alumnos", width=75, anchor=CENTER)
    tvEstudiante.column("correo", width=75, anchor=CENTER)
    
    tvEstudiante.heading("#0", text="")
    tvEstudiante.heading("cedula",text="cedula",anchor=CENTER)
    tvEstudiante.heading("nombre",text="nombre",anchor=CENTER)
    tvEstudiante.heading("direccion",text="direccion",anchor=CENTER)
    tvEstudiante.heading("telefono",text="telefono",anchor=CENTER)
    tvEstudiante.heading("numero_alumnos",text="asociados",anchor=CENTER)
    tvEstudiante.heading("correo",text="correo",anchor=CENTER)



    cedula_entry = Entry(mwindow, textvariable=cedula_entry, font=("Cambria", 16),justify='center',
                          width=20)
    cedula_entry.place(x=220, y=390)
    submit_btn = CTkButton(mwindow, text="BUSCAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                         command=llenar_tabla) 
    submit_btn.place(x=301, y=450)

    
    mwindow.mainloop()