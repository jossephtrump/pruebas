from tkinter import *

import tkinter as tkinter
import customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
import MySQLdb as mysql
from datetime import *

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
    global representante_entry

    cedula_entry = StringVar()
    representante_entry = StringVar()

    inscripcion = Label(mwindow,text="ingrese la cedula ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    cedula_entry= Entry(mwindow,textvariable=cedula_entry, font=("Cambria", 16), width=25, justify="center")

    cedula_entry.pack()

    inscripcion = Label(mwindow,text="ingrese la cedula del representante ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    representante_entry= Entry(mwindow,textvariable=representante_entry, font=("Cambria", 16), width=25, justify="center")
    representante_entry.pack()

    Label(mwindow,bg="#213141").pack()

    Button(mwindow,text="pago inscripcion",font=("Cambria", 6),
                           width=40, height=10, anchor="center",command=insertinscrip).pack()

    mwindow.mainloop()

def insertinscrip():
        
        hora_min = datetime.now().strftime("%H:%M")
        print("Hora y Minutos: ", hora_min)

        # Crea una variable para el día, mes y año
        dia_mes_anio = datetime.now().strftime("%Y/%m/%d")
        print("Día/Mes/Año: ", dia_mes_anio)

        #setencias
        sql = "UPDATE alumno SET pago= '{0}' WHERE cedula='{1}'".format(60,cedula_entry.get())
        sql2= "INSERT INTO registro_pagos (fecha,hora,cedula_estudiante,cedula_representante,pago) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(dia_mes_anio, hora_min,cedula_entry.get(),representante_entry.get(),60)

            #ejecucion de sentencia
        cur.execute(sql)
        cur.execute(sql2)

        #comprobacion de sentencias (crear notificacion)
        if cur.rowcount == 0:
            mydb.rollback()
        else:
            mydb.commit()
            print(cur.rowcount,"Fue insetado correctamente")
    

def pago_mensualidad():
    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("700x600")
    mwindow.title("Registro")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")

    global cantidad_pago
    global cedula_entry
    global representante_entry
  

    cedula_entry = StringVar()
    representante_entry = StringVar()
    cantidad_pago = IntVar()

    inscripcion = Label(mwindow,text="ingrese la cedula ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    cedula_entry= Entry(mwindow,textvariable=cedula_entry, font=("Cambria", 16), width=25, justify="center")

    cedula_entry.pack()

    inscripcion = Label(mwindow,text="ingrese la cedula del representante ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    representante_entry= Entry(mwindow,textvariable=representante_entry, font=("Cambria", 16), width=25, justify="center")
    representante_entry.pack()
    
    inscripcion = Label(mwindow,text="ingrese la cantidad pagada ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    cantidad_pago = Entry(mwindow,textvariable=cantidad_pago,font=("Cambria", 16), width=25, justify="center")
    cantidad_pago.pack()

    Label(mwindow,bg="#213141").pack()

    Button(mwindow,text="pago inscripcion",font=("Cambria", 6),
                           width=40, height=10, anchor="center",command=factura).pack()

    mwindow.mainloop()

def factura():
     
 
            
    hora_min = datetime.now().strftime("%H:%M")
    print("Hora y Minutos: ", hora_min)

        # Crea una variable para el día, mes y año
    dia_mes_anio = datetime.now().strftime("%Y/%m/%d")
    print("Día/Mes/Año: ", dia_mes_anio)

     #setencias
    sql = "UPDATE alumno SET pago= pago +'{0}' WHERE cedula='{1}'".format(cantidad_pago.get(),cedula_entry.get())
    sql2= "INSERT INTO registro_pagos (fecha,hora,cedula_estudiante,cedula_representante,pago) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(dia_mes_anio, hora_min,cedula_entry.get(),representante_entry.get(),cantidad_pago.get())

        #ejecucion de sentencia
    cur.execute(sql)
    cur.execute(sql2)

        #comprobacion de sentencias (crear notificacion)
    if cur.rowcount == 0:
        mydb.rollback()
    else:
        mydb.commit()
        print(cur.rowcount,"Fue insetado correctamente")    