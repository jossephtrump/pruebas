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
    mywindow.geometry("700x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")

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

    h = 110
    username_label = Label(mywindow, text="Nombre ", font=("Cambria", 16),
                       width=7, height=1, fg="white", anchor="center",
                        justify="center", bg="#213141")
    username_label.pack()
    

    username_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=25)
    username_entry.pack()

    cedula_label = Label(mywindow, text="Cedula ", font=("Cambria", 16),
                        width=7, height=1, fg="white", anchor="center",
                        justify="center", bg="#213141")
    cedula_label.pack()

    cedula_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=25)
    cedula_entry.pack()

    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                    width=7, height=1, fg="white", anchor="center",
                    justify="center", bg="#213141")
    tlf_label.pack()

    telefono_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=25)
    telefono_entry.pack()

    correo_label = Label(mywindow, text="Correo ", font=("Cambria", 16),
                        width=7, height=1, fg="white",
                        anchor="center", justify="center", bg="#213141")
    
    correo_label.pack()
    correo_entry = Entry(mywindow,font=("Cambria", 16), justify='center',width=25)
    correo_entry.pack()
   
    direccion_label = Label(mywindow, text="Direccion ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    
    direccion_label.pack()
    direccion_entry= Entry(mywindow,font=("Cambria", 16), width=25, justify="center")
    direccion_entry.pack()

    canatidad_label = Label(mywindow, text="cantidad de alumnos", font=("Cambria", 16),
                            width=16, height=2, fg="white",
                            anchor="center", justify="center", bg="#213141")
    canatidad_label.pack()

    caalumnos_entry = Entry(mywindow, font=("Cambria", 16),justify='center', width=20)
    caalumnos_entry.pack()
    Label(mywindow,bg="#213141").pack()
    Button(mywindow, text="GUARDAR", font=("Cambria", 6),
                           width=40, height=10, anchor="center",command=insertarestudiante).pack()
    
    mywindow.mainloop()
    
def insertarestudiante():
        
        sql = "INSERT INTO representante (cedula,nombre,direccion,telefono,numero_alumnos,correo)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(cedula_entry.get(),username_entry.get(),direccion_entry.get(),telefono_entry.get(),caalumnos_entry.get(),correo_entry.get())
	
   
        cur.execute(sql)
        if cur.rowcount == 0:
            mydb.rollback()
        else:
            mydb.commit()
            print(cur.rowcount,"Fue insetado correctamente")
    
    
    # # Manipulate data from registration fields
    # mydb = mysql.connector.connect(host='localhost',user='root',passwd='',db='colegio')
    # cur = mydb.cursor()
    # global username_entry
    # global cedula_entry
    # global tlf_entry
    # global correo_entry
    # global direccion_entry
    # global cantidad_alumnos_entry
    # global username
    # global cedula
    # global tlf
    # global correo
    # global direccion
    # global cantidad_alumnos
    # username = StringVar()
    # cedula = StringVar()
    # tlf = StringVar()
    # correo = StringVar()
    # direccion = StringVar()
    # cantidad_alumnos = StringVar()
    
    


    # # Create new instance - Class cTk()
    # mywindow = ctk.CTk()
    # mywindow.geometry("700x600")
    # mywindow.title("Registro")
    # mywindow.resizable(False, False)
    # mywindow.config(background="#213141")
   
  
    # def mostrar_error(widget, textvariable):
    #     valor1 = username_entry.get()
    #     valor2 = cedula_entry.get()
    #     valor3 = tlf_entry.get()
    #     valor4 = cantidad_alumnos_entry.get()

    # # Validamos el valor de la entrada de texto
    #     if valor1 == "" or valor2 == "" or valor3 == "" or valor4 == "":
    #         messagebox.showerror("Error", "La entrada no es válida")
    #     # Call the `mostrar_error()` function with the correct arguments
    # mostrar_error(username_entry, username)

   
    
    # def send_data():
    #     username_info = username.get()
    #     cedula_info = cedula.get()
    #     tlf_info = tlf.get()
    #     correo_info = correo.get()
    #     direccion_info = direccion.get()
    #     alumnos_info = cantidad_alumnos.get()

    #     # Insert the user data into the database
    #     insert_query = "INSERT INTO representantes (username, cedula, tlf, correo, direccion, cantidad_alumnos) VALUES (%s, %s, %s, %s, %s, %s)"
    #     cur.execute(insert_query, (username_info, cedula_info, tlf_info, correo_info, direccion_info, alumnos_info))
    #     mydb.commit()

    #     # Delete data from previous event
    #     username_entry.delete(0, END)
    #     cedula_entry.delete(0, END)
    #     tlf_entry.delete(0, END)
    #     correo_entry.delete(0, END)
    #     direccion_entry.delete(0, END)
    #     cantidad_alumnos_entry.delete(0, END)

    
    # # Submit Button
    # submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
    #                        width=30, height=20, anchor="center", command=lambda:  send_data())

    # submit_btn.place(x=300, y=540)
    # # bucle
    # mywindow.mainloop()


# funcion para registrar los alumnos
def alumno():

    global ecedula_entry
    global eusername_entry
    global edireccion_entry
    global etelefono_entry 
    global ecorreo_entry
    global ecedrepresentante_entry
    global egrado_entry

    ecedrepresentante_entry = tkinter.StringVar()
    ecedula_entry = tkinter.StringVar()
    eusername_entry = tkinter.StringVar()
    edireccion_entry = tkinter.StringVar()
    etelefono_entry = tkinter.StringVar()
    ecorreo_entry = tkinter.StringVar()
    egrado_entry = tkinter.StringVar()

    global mywindow
    mywindow = ctk.CTk()
    mywindow.geometry("700x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")

    username_label = Label(mywindow, text="Nombre ", font=("Cambria", 16),
                           width=7, height=1, fg="white", anchor="center",
                           justify="center", bg="#213141").pack()
    
    eusername_entry = Entry(mywindow, textvariable=eusername_entry, font=("Cambria", 9),justify='center', width=35)
    eusername_entry.pack()


    cedula_label = Label(mywindow, text="Cedula del representante ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    ecedrepresentante_entry = Entry(mywindow, textvariable=ecedrepresentante_entry, font=("Cambria", 9),justify='center' ,width=30)
    ecedrepresentante_entry.pack()

    cedula_label = Label(mywindow, text="Cedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141").pack()
    
    ecedula_entry = Entry(mywindow, textvariable=ecedula_entry, font=("Cambria", 9),justify='center', width=25)
    ecedula_entry.pack()

    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                      width=7, height=1, fg="white", anchor="center",
                      justify="center", bg="#213141").pack()
    
    etelefono_entry = Entry(mywindow, textvariable=etelefono_entry, font=("Cambria", 16),justify='center', width=25)
    etelefono_entry.pack()

   

    direccion_label = Label(mywindow, text="Direccion ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141").pack()
    
    edireccion_entry= Entry(mywindow, textvariable=edireccion_entry ,font=("Cambria", 16), width=25, justify="center")
    edireccion_entry.pack()

    grado_label = Label(mywindow, text="curso ", font=("Cambria", 16),
                       width=7, height=1, fg="white",
                       anchor="center", justify="center", bg="#213141").pack()

    grado_values = ('S3', 'S4', 'S5', '1GU', '2GU', '3GU', '4GU', '5GU', '6GU',
                   '1AA', '1AB', '2AA', '2AB', '3AA', '3AB', '4AA', '4AB', '5AA', '5AB')

    egrado_combobox = ttk.Combobox(mywindow,textvariable=egrado_entry ,values=grado_values,
                                  font=("Cambria", 16), justify='center',width=25)
    egrado_combobox.current(0)
    egrado_combobox.pack()

    Label(mywindow,bg="#213141").pack()
    Button(mywindow, text="GUARDAR", font=("Cambria", 6),
                           width=40, height=10, anchor="center",command=ingresaralumno).pack()

    # bucle
    mywindow.mainloop()

def ingresaralumno():
   sql = "INSERT INTO alumno (cedula,cedula_representante,nombre,direccion,telefono,pago,curso)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(ecedula_entry.get(),ecedrepresentante_entry.get(),eusername_entry.get(),edireccion_entry.get(),etelefono_entry.get(),0,egrado_entry.get())
	
   
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








def opcion():
    print("Opcion: No se que va aqui aun")
