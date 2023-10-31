# importaciones necesarias
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

def representante():
    global mywindow
    mywindow = ctk.CTk()
    mywindow.geometry("600x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")
    main_title = ctk.CTkLabel(mywindow, text="Registro | Representantes", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    global cedula_entry
    global username_entry
    global direccion_entry
    global telefono_entry
    global caalumnos_entry
    global correo_entry
    
    cedula_entry = IntVar()
    username_entry = tkinter.StringVar()
    direccion_entry = tkinter.StringVar()
    telefono_entry = tkinter.StringVar()
    caalumnos_entry = IntVar()
    correo_entry = tkinter.StringVar()

    # Funct for invalid entries
    def mostrar_error():
        valor1 = username_entry.get()
        valor2 = cedula_entry.get()
        valor3 = telefono_entry.get()
        valor4 = caalumnos_entry.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "":
            messagebox.showerror("Error", "Ingrese Nombre")
            return True
        elif  valor2 == "":
            messagebox.showerror("Error", "Ingrese Cedula")
            return True
        elif  valor3 == "":
            messagebox.showerror("Error", "Ingrese Celular")
            return True
        elif  valor4 == "":
            messagebox.showerror("Error", "Ingrese Nº de Alumnos")
            return True
        return False

    vcmd = mywindow.register(mostrar_error)

    h = 125
    username_label = Label(mywindow, text="Nombre", font=("Cambria", 16),
                       width=7, height=1, fg="white", anchor="center",
                        justify="center", bg="#213141")
    username_label.place(x=h, y=30)
    
    a = 125
    w = 30
    username_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=w,
                           validatecommand=(vcmd, "%P"))
    username_entry.place(x=a, y=70)


    cedula_label = Label(mywindow, text="Cedula", font=("Cambria", 16),
                        width=7, height=1, fg="white", anchor="center",
                        justify="center", bg="#213141")
    cedula_label.place(x=h, y=110)

    cedula_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=w,
                          validatecommand=(vcmd, "%P")) #validacion, no puede quedar vacio
    cedula_entry.place(x=a, y=150)


    tlf_label = Label(mywindow, text="Telefono", font=("Cambria", 16),
                    width=7, height=1, fg="white", anchor="center",
                    justify="center", bg="#213141")
    tlf_label.place(x=h, y=190)

    telefono_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=w)
    telefono_entry.place(x=a, y=230)


    correo_label = Label(mywindow, text="Correo", font=("Cambria", 16),
                        width=7, height=1, fg="white",
                        anchor="center", justify="center", bg="#213141")
    
    correo_label.place(x=h, y=270)
    correo_entry = Entry(mywindow,font=("Cambria", 16), justify='center', width=w)
    correo_entry.place(x=a, y=310)
   

    direccion_label = Label(mywindow, text="Direccion", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    
    direccion_label.place(x=h, y=350)
    direccion_entry= Entry(mywindow,font=("Cambria", 16), width=w,  justify="center" )
    direccion_entry.place(x=a, y=390)


    canatidad_label = Label(mywindow, text="Nº Alumnos", font=("Cambria", 16),
                            width=8, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    canatidad_label.place(x=h, y=430)

    caalumnos_entry = Entry(mywindow, font=("Cambria", 16), justify='center', width=w, 
                            validatecommand=(vcmd, "%P"))
    caalumnos_entry.place(x=a, y=470)


    submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                           command=lambda: [insertarestudiante() if not mostrar_error() else None]) 
    submit_btn.place(x=250, y=540)

    
    mywindow.mainloop()
    
def insertarestudiante():
        
        sql = "INSERT INTO representante (cedula,nombre,direccion,telefono,numero_alumnos,correo)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(cedula_entry.get(),
               username_entry.get(),
               direccion_entry.get(),
               telefono_entry.get(),
               caalumnos_entry.get(),
               correo_entry.get())
	
   
        cur.execute(sql)
        if cur.rowcount == 0:
            mydb.rollback()
        else:
            mydb.commit()
            print(cur.rowcount,"Fue insertado correctamente") #chinazo_XD
            cedula_entry.delete(0, END)
            username_entry.delete(0, END)
            direccion_entry.delete(0, END)
            telefono_entry.delete(0, END)
            caalumnos_entry.delete(0, END)
            correo_entry.delete(0, END)
 
# funcion para registrar los alumnos
def alumno():

    global ecedula_entry
    global eusername_entry
    global edireccion_entry
    global etelefono_entry 
    global ecorreo_entry
    global ecedrepresentante_entry
    global egrado_entry
    global egrado_combobox

    egrado_combobox= tkinter.StringVar()
    ecedrepresentante_entry = tkinter.StringVar()
    ecedula_entry = tkinter.StringVar()
    eusername_entry = tkinter.StringVar()
    edireccion_entry = tkinter.StringVar()
    etelefono_entry = tkinter.StringVar()
    ecorreo_entry = tkinter.StringVar()
    egrado_entry = tkinter.StringVar()

    global mywindow
    mywindow = ctk.CTk()
    mywindow.geometry("600x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")
    main_title = ctk.CTkLabel(mywindow, text="Registro | Alumnos", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    def mostrar_error():
        valor1 = eusername_entry.get()
        valor2 = ecedrepresentante_entry.get() 
        valor3 = ecedula_entry.get()
        valor4 = egrado_combobox.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "":
            messagebox.showerror("Error", "Ingrese Nombre")
            return True
        elif  valor2 == "":
            messagebox.showerror("Error",  "Ingrese Cedula del Representante")
            return True
        elif  valor3 == "":
            messagebox.showerror("Error", "Ingrese IDCedula")
            return True
        elif  valor4 == "":
            messagebox.showerror("Error", "Grado")
            return True
        return False

    vcmd = mywindow.register(mostrar_error)


    h = 125
    w = 30
    username_label = Label(mywindow, text="Nombre ", font=("Cambria", 16),
                           width=7, height=1, fg="white", anchor="w",
                           justify="left", bg="#213141")
    username_label.place(x=h, y=30)
    eusername_entry = Entry(mywindow, textvariable=eusername_entry, font=("Cambria", 16),
                            justify='center', width=w, validatecommand=(vcmd, "%P"))
    eusername_entry.place(x=h, y=70)


    cedula_label = Label(mywindow, text="Cedula del representante ", font=("Cambria", 16),
                         width=w, height=1, fg="white", anchor=W,
                         justify="left", bg="#213141")
    cedula_label.place(x=h, y=110)
    ecedrepresentante_entry = Entry(mywindow, textvariable=ecedrepresentante_entry, font=("Cambria", 16),
                                    justify='center' ,width=w, validatecommand=(vcmd, "%P") )
    ecedrepresentante_entry.place(x=h, y=150)


    Idcedula_label = Label(mywindow, text="IDCedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white", anchor=W,
                         justify="left", bg="#213141")
    Idcedula_label.place(x=h, y=190)
    ecedula_entry = Entry(mywindow, textvariable=ecedula_entry, font=("Cambria", 16),justify='center', width=w,
                          validatecommand=(vcmd, "%P"))
    ecedula_entry.place(x=h, y=230)

    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                      width=7, height=1, fg="white", anchor=W,
                      justify="left", bg="#213141").place(x=h, y=270)
    
    etelefono_entry = Entry(mywindow, textvariable=etelefono_entry, font=("Cambria", 16),justify='center', width=w)
    etelefono_entry.place(x=h, y=310)

   
    grado_label = Label(mywindow, text="Curso ", font=("Cambria", 16),
                       width=7, height=1, fg="white",
                       anchor=W, justify="left", bg="#213141").place(x=h, y=350)

    grado_values = ('S3', 'S4', 'S5', '1GU', '2GU', '3GU', '4GU', '5GU', '6GU',
                   '1AA', '1AB', '2AA', '2AB', '3AA', '3AB', '4AA', '4AB', '5AA', '5AB')

    egrado_combobox = ttk.Combobox(mywindow,textvariable=egrado_entry ,values=grado_values,
                                  font=("Cambria", 16), justify='center',width=28,validatecommand=(vcmd, "%P") )
    egrado_combobox.current(0)
    egrado_combobox.place(x=h, y=390)

   
    submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                         command=lambda: [ingresaralumno() if not mostrar_error() else None]) 
    submit_btn.place(x=250, y=540)

    # bucle
    mywindow.mainloop()

def ingresaralumno():
   sql = "INSERT INTO alumno (cedula,cedula_representante,nombre,direccion,telefono,pago,curso)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(ecedula_entry.get(),ecedrepresentante_entry.get(),eusername_entry.get(),edireccion_entry.get(),etelefono_entry.get(),0,egrado_combobox.get())
	
   
   cur.execute(sql)
   if cur.rowcount == 0:
       mydb.rollback()
   else:
        mydb.commit()
        print(cur.rowcount,"Fue insetado correctamente")
        print("Guardar datos:")
        print("Cedula del representante:", ecedrepresentante_entry.get())
        print("Cedula:", ecedula_entry.get())
        print("Nombre:", eusername_entry.get())
        print("Direccion:", edireccion_entry.get())
        print("Telefono:", etelefono_entry.get())
        print("Grado:", egrado_entry.get())
        eusername_entry.delete(0, END)
        ecedrepresentante_entry.delete(0, END)
        ecedula_entry.delete(0, END)
        etelefono_entry.delete(0, END)

def opcion():
    print("Opcion: No se que va aqui aun")
