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

def cobranza_alumno():
    global cedula_entry

    def vaciar_tabla():
        filas = tvEstudiante.get_children()
        for fila in filas:
            tvEstudiante.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        sql = "SELECT * FROM registro_pagos WHERE cedula_estudiante = {0}".format(cedula_entry.get())
        cur.execute(sql)
        filas = cur.fetchall()
        for fila in filas:
            cedula = fila[0]
        tvEstudiante.insert("", END, cedula, text=cedula, values=fila)


    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("700x500")
    mwindow.title("Cobranza")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")
    main_title = ctk.CTkLabel(mwindow, text="Registro | PAGOS", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    cedula_entry = StringVar()
    tvEstudiante = ttk.Treeview(mwindow)
    style = ttk.Style(tvEstudiante)
    style.configure("Treeview", background="#dcdcdc", foreground="black", font=("Arial", 14),
                    borderwidth=2, highlightthickness=1)
    style.configure("Treeview.Heading", background="black", foreground="black", font=("Arial", 14, "bold"))
    tvEstudiante.pack(fill="x", expand=True, side="top", anchor="n")
    tvEstudiante["columns"]=("id","fecha","hora", "cedula_estudiante","cedula_representante","pago")

    a = 90
    tvEstudiante.column("#0", width=10, stretch=NO)
    tvEstudiante.column("id", width=a, anchor=CENTER)
    tvEstudiante.column("fecha", width=a, anchor=CENTER)
    tvEstudiante.column("hora", width=a, anchor=CENTER)
    tvEstudiante.column("cedula_estudiante", width=a, anchor=CENTER)
    tvEstudiante.column("cedula_representante", width=a, anchor=CENTER)
    tvEstudiante.column("pago", width=80, anchor=CENTER)

    #tvEstudiante.heading("#0", text="")
    tvEstudiante.heading("id",text="Nº",anchor=CENTER)
    tvEstudiante.heading("fecha",text="Fecha",anchor=CENTER)
    tvEstudiante.heading("hora",text="Hora",anchor=CENTER)
    tvEstudiante.heading("cedula_estudiante",text="IDCedula",anchor=CENTER)
    tvEstudiante.heading("cedula_representante",text="Cedula",anchor=CENTER)
    tvEstudiante.heading("pago",text="MONTO",anchor=CENTER)

    w = 20
    h = 220
    Idcedula_label = Label(mwindow, text="IDCedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white", anchor=CENTER,
                         justify="center", bg="#213141")
    Idcedula_label.place(x=300, y=350)
    cedula_entry = Entry(mwindow, textvariable=cedula_entry, font=("Cambria", 16),justify='center',
                          width=w)
    cedula_entry.place(x=h, y=390)

    submit_btn = CTkButton(mwindow, text="BUSCAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                         command=llenar_tabla) 
    submit_btn.place(x=301, y=450)

    mwindow.mainloop()

def cobranza_curso():
    global egrado_entry
    global egrado_combobox

    egrado_combobox= tkinter.StringVar()
    egrado_entry= StringVar()
    def vaciar_tabla():
        filas = tvEstudiante.get_children()
        for fila in filas:
            tvEstudiante.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        print(egrado_combobox.get())
        sql = "SELECT * FROM registro_pagos WHERE cedula_estudiante IN (SELECT cedula FROM alumno WHERE curso = '{0}')".format(egrado_combobox.get())
        cur.execute(sql)
        filas = cur.fetchall()
        for fila in filas:
            cedula = fila[0]
            tvEstudiante.insert("", END, cedula, text=cedula, values=fila)


    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("700x700")
    mwindow.title("COBRANZA")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")
    main_title = ctk.CTkLabel(mwindow, text="COBRO | SECCIONES", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    cedula_entry = StringVar()
    tvEstudiante = ttk.Treeview(mwindow)
    style = ttk.Style(tvEstudiante)
    style.configure("Treeview", background="#dcdcdc", foreground="black", font=("Arial", 14),
                    borderwidth=2, highlightthickness=1)
    style.configure("Treeview.Heading", background="black", foreground="black", font=("Arial", 14, "bold"))

    tvEstudiante.pack(fill="x", expand=True, side="top", anchor="n")
    tvEstudiante["columns"]=("id","fecha","hora","cedula_estudiante","cedula_representante","pago")

    a = 80
    tvEstudiante.column("#0", width=0, stretch=NO)
    tvEstudiante.column("id", width=5, anchor=CENTER)
    tvEstudiante.column("fecha", width=a, anchor=CENTER)
    tvEstudiante.column("hora", width=a, anchor=CENTER)
    tvEstudiante.column("cedula_estudiante", width=a, anchor=CENTER)
    tvEstudiante.column("cedula_representante", width=a, anchor=CENTER)
    tvEstudiante.column("pago", width=70, anchor=CENTER)

    tvEstudiante.heading("#0", text="")
    tvEstudiante.heading("id",text="Nº",anchor=CENTER)
    tvEstudiante.heading("fecha",text="fecha",anchor=CENTER)
    tvEstudiante.heading("hora",text="hora",anchor=CENTER)
    tvEstudiante.heading("cedula_estudiante",text="IDAlumno",anchor=CENTER)
    tvEstudiante.heading("cedula_representante",text="Nombre",anchor=CENTER)
    tvEstudiante.heading("pago",text="pago",anchor=CENTER)
    grado_values = ('S3', 'S4', 'S5', '1GU', '2GU', '3GU', '4GU', '5GU', '6GU',
                   '1AA', '1AB', '2AA', '2AB', '3AA', '3AB', '4AA', '4AB', '5AA', '5AB')

    egrado_combobox = ttk.Combobox(mwindow,textvariable=egrado_entry ,values=grado_values,
                                  font=("Cambria", 16), justify='center',width=15)
    egrado_combobox.current(0)
    egrado_combobox.place(x=250, y=600)

     
    submit_btn = CTkButton(mwindow, text="BUSCAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                         command=llenar_tabla) 
    submit_btn.place(x=310, y=650)
    
    mwindow.mainloop()