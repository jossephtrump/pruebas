# aqui vamos a colocar las funciones necesarias para no estar
# colocando tanto codigo ahi, mejor importar las funciones y borrador

from tkinter import *
import tkinter as tk
import customtkinter
from customtkinter import *
from ttkthemes import ThemedTk
import customtkinter as ctk
import os
from tkinter import ttk
import tkinter.messagebox as messagebox






def nuevo():
    print("Nuevo: funcion inutil, no se pq la puse, algun dia le encontrare sentido")


def abrir():
    print("Buscar: accion para abrir no se que coño , si esto no es office")


def cierre():
    print("Cierre Diario: calculo total de los pagos realizados durante el dia")


def importar():
    print("Importar: accion para importar base de datos")


def exportar():
    print("Exportar: accion para exportar base de datos")


def representante():
    # Manipulate data from registration fields
    def send_data():
        username_info = username.get()
        apellidos_info = apellidos.get()
        cedula_info = cedula.get()
        tlf_info = tlf.get()
        direccion_info = direccion.get()
        alumnos_info = cantidad_alumnos.get()
        print(username_info, "\t", apellidos_info, "\t", cedula_info, "\t", tlf_info, "\t", alumnos_info, "\t",
              direccion_info)
        #  Open and write data to a file
        file = open("user.txt", "a")
        file.write(username_info)
        file.write("\t")
        file.write(apellidos_info)
        file.write("\t")
        file.write(cedula_info)
        file.write("\t")
        file.write(tlf_info)
        file.write("\t\n")
        file.write(direccion_info)
        file.write("\t\n")
        file.write(alumnos_info)
        print(" New user registered. Username: {} | "
              "FullName: {}   ".format(username_info, apellidos_info))

        #  Delete data from previous event
        username_entry.delete(0, END)
        apellidos_entry.delete(0, END)
        cedula_entry.delete(0, END)
        tlf_entry.delete(0, END)
        direccion_entry.delete(0, END)
        cantidad_alumnos_entry.delete(0, END)

    # Create new instance - Class Tk()
    mywindow = ctk.CTk()
    mywindow.geometry("700x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")  # 213141 gray31
    main_title = ctk.CTkLabel(mywindow, text="Registro | Representantes", font=("Cambria", 19), fg_color="gray21",
                              width=500, height=2)
    # bg = "cornflowerblue"
    main_title.pack(fill="x")

    # Define Label Fields
    h = 110
    username_label = Label(mywindow, text=" Nombre ", font=("Cambria", 16),
                           width=7, height=1, fg="white",
                           anchor="center", justify="center", bg="#213141")
    username_label.place(x=h, y=30)
    apellidos_label = Label(mywindow, text="Correo ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    apellidos_label.place(x=h, y=270)
    cedula_label = Label(mywindow, text="Cedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white",
                         anchor="center", justify="center", bg="#213141")
    cedula_label.place(x=h, y=110)
    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                      width=7, height=1, fg="white",
                      anchor="center", justify="center", bg="#213141")
    tlf_label.place(x=h, y=190)
    direccion_label = Label(mywindow, text="Direccion ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    direccion_label.place(x=h, y=350)
    cantidad_label = Label(mywindow, text="NºAlumnos", font=("Cambria", 16),
                           width=8, height=1, fg="white",
                           anchor="center", justify="center", bg="#213141")
    cantidad_label.place(x=h, y=430)

    # Get and store data from users
    username = StringVar()
    apellidos = StringVar()
    cedula = StringVar()
    tlf = StringVar()
    direccion = StringVar()
    cantidad_alumnos = StringVar()

    # Creamos una función que se ejecuta cuando la entrada es inválida
    def mostrar_error():
        # Obtenemos el valor de la entrada de texto
        valor1 = username_entry.get()
        valor2 = cedula_entry.get()
        valor3 = tlf_entry.get()
        valor4 = cantidad_alumnos_entry.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "":
            # Mostramos un mensaje de error usando el módulo messagebox
            messagebox.showerror("Error", "La entrada no es válida")
    vcmd = mywindow.register(mostrar_error)

#creacion de los entry
    username_entry = ctk.CTkEntry(mywindow, textvariable=username, font=("Cambria", 16),
                                  justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2")

    apellidos_entry = ctk.CTkEntry(mywindow, textvariable=apellidos, font=("Cambria", 16),
                            justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2")
    cedula_entry = ctk.CTkEntry(mywindow, textvariable=cedula, font=("Cambria", 16),
                         justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2",  validate="focusout", validatecommand=(vcmd, "%P"))
    tlf_entry = ctk.CTkEntry(mywindow, textvariable=tlf, font=("Cambria", 16),
                      justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2")
    direccion_entry = ctk.CTkEntry(mywindow, textvariable=direccion, font=("Cambria", 16),
                            justify="center", width=485, height=35, text_color="black",
                            placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2")

    opciones = (1, 2, 3, 4, 5)
    cantidad_alumnos_entry = ttk.Combobox(mywindow, textvariable=cantidad_alumnos, font=("Cambria", 16),
                                          width=22, values=opciones)


    a = 110
    username_entry.place(x=a, y=70)
    apellidos_entry.place(x=a, y=310)
    cedula_entry.place(x=a, y=150)
    tlf_entry.place(x=a, y=230)
    direccion_entry.place(x=a, y=390)
    cantidad_alumnos_entry.place(x=a, y=470)

    # Submit Button
    submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", command=lambda: [mostrar_error(), send_data()])

    submit_btn.place(x=300, y=540)




    mywindow.mainloop()


def alumno():
    print("Alumno: Inscribir Alumno")


def opcion():
    print("Opcion: No se que va aqui aun")


def inscripcion():
    print("Inscripcion: registrar pago inscripcion")


def Mensualidad():
    print("Mensualidad: registrar pago mensual")


def pagos_realizados():
    print("aqui se introduce la cedula y genera un\nreporte "
          "de todos los pagos realizados por ese representante")


def info_representantes():
    print("Se introduce el id y genera la data correspondiente\n"
          "al representante")


def info_alumnos():
    print("Se introduce el id y genera la data correspondiente\n"
          "al alumno")


def deuda_representante():
    print("Representate: luego de introducir el id, genera el estado de deuda\n"
          "si la posee")


def deuda_alumno():
    print("Alumno: luego de introducir el id, genera el estado de deuda\n"
          "si la posee")
