# importaciones necesarias
from tkinter import *
import tkinter as tk
import customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox


def representante():
    # Manipulate data from registration fields
    def send_data():
        username_info = username.get()
        cedula_info = cedula.get()
        tlf_info = tlf.get()
        correo_info = correo.get()
        direccion_info = direccion.get()
        alumnos_info = cantidad_alumnos.get()
        print(username_info, "\t", cedula_info, "\t", tlf_info, "\t", correo_info, "\t",
              direccion_info, alumnos_info, "\t", )
        #  Open and write data to a file
        file = open("user.txt", "a")
        file.write(username_info)
        file.write("\t")
        file.write(cedula_info)
        file.write("\t")
        file.write(tlf_info)
        file.write("\t")
        file.write(correo_info)
        file.write("\t\n")
        file.write(direccion_info)
        file.write("\t\n")
        file.write(alumnos_info)
        print(f" Datos del Registro:\n"
              f" Nombres: {username_info} --- Cedula {cedula_info}\n"
              f"Telefono: {tlf_info} --- Correo: {correo_info}"
              f"Direccion: {direccion_info} --- Cantidad de alumnos: {alumnos_info}"
              )
        #  Delete data from previous event
        username_entry.delete(0, END)
        cedula_entry.delete(0, END)
        tlf_entry.delete(0, END)
        correo_entry.delete(0, END)
        direccion_entry.delete(0, END)
        cantidad_alumnos_entry.delete(0, END)

    # Create new instance - Class cTk()
    mywindow = ctk.CTk()
    mywindow.geometry("700x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")
    main_title = ctk.CTkLabel(mywindow, text="Registro | Representantes", font=("Cambria", 19),
                              fg_color="gray21", width=500, height=2)
    main_title.pack(fill="x")

    # Define Label Fields
    h = 110
    username_label = Label(mywindow, text="Nombre ", font=("Cambria", 16),
                           width=7, height=1, fg="white", anchor="center",
                           justify="center", bg="#213141")
    username_label.place(x=h, y=30)
    cedula_label = Label(mywindow, text="Cedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141")
    cedula_label.place(x=h, y=110)

    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                      width=7, height=1, fg="white", anchor="center",
                      justify="center", bg="#213141")
    tlf_label.place(x=h, y=190)

    correo_label = Label(mywindow, text="Correo ", font=("Cambria", 16),
                         width=7, height=1, fg="white",
                         anchor="center", justify="center", bg="#213141")
    correo_label.place(x=h, y=270)

    direccion_label = Label(mywindow, text="Direccion ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    direccion_label.place(x=h, y=350)

    cantidad_label = Label(mywindow, text="Nº Alumnos", font=("Cambria", 16),
                           width=8, height=1, fg="white",
                           anchor="center", justify="center", bg="#213141")
    cantidad_label.place(x=h, y=430)
    # Get and store data from users
    username = StringVar()
    cedula = StringVar()
    tlf = StringVar()
    correo = StringVar()
    direccion = StringVar()
    cantidad_alumnos = StringVar()

    # Funct for invalid entries
    def mostrar_error():
        valor1 = username_entry.get()
        valor2 = cedula_entry.get()
        valor3 = tlf_entry.get()
        valor4 = cantidad_alumnos_entry.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "" or valor2 == "" or valor3 == "" or valor4 == "":
            messagebox.showerror("Error", "La entrada no es válida")

    vcmd = mywindow.register(mostrar_error)

    # creacion de los entry
    username_entry = ctk.CTkEntry(mywindow, textvariable=username, font=("Cambria", 16),
                                  justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))

    cedula_entry = ctk.CTkEntry(mywindow, textvariable=cedula, font=("Cambria", 16),
                                justify="center", width=485, height=35, text_color="black",
                                placeholder_text="Primer Nombre", placeholder_text_color="black",
                                fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))

    tlf_entry = ctk.CTkEntry(mywindow, textvariable=tlf, font=("Cambria", 16),
                             justify="center", width=485, height=35, text_color="black",
                             placeholder_text="Primer Nombre", placeholder_text_color="black",
                             fg_color="snow2")

    correo_entry = ctk.CTkEntry(mywindow, textvariable=correo, font=("Cambria", 16),
                                justify="center", width=485, height=35, text_color="black",
                                placeholder_text="Primer Nombre", placeholder_text_color="black",
                                fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))
    direccion_entry = ctk.CTkEntry(mywindow, textvariable=direccion, font=("Cambria", 16),
                                   justify="center", width=485, height=35, text_color="black", fg_color="snow2")

    opciones = (1, 2, 3, 4, 5)
    cantidad_alumnos_entry = ttk.Combobox(mywindow, textvariable=cantidad_alumnos, font=("Cambria", 16),
                                          width=22, values=opciones, validate="focusout", validatecommand=(vcmd, "%P"))

    # Entries positioning
    a = 110
    username_entry.place(x=a, y=70)
    cedula_entry.place(x=a, y=150)
    tlf_entry.place(x=a, y=230)
    correo_entry.place(x=a, y=310)
    direccion_entry.place(x=a, y=390)
    cantidad_alumnos_entry.place(x=a, y=470)

    # Submit Button
    submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", command=lambda: [mostrar_error(), send_data()])

    submit_btn.place(x=300, y=540)
    # bucle
    mywindow.mainloop()


# funcion para registrar los alumnos
def alumno():
    print("Alumno: Inscribir Alumno")

    def send_data():
        username_info = username.get()
        cedula_info = cedula.get()
        tlf_info = tlf.get()
        correo_info = correo.get()
        direccion_info = direccion.get()
        print(username_info, "\t", cedula_info, "\t", tlf_info, "\t", correo_info, "\t",
              direccion_info)
        #  Open and write data to a file
        file = open("user.txt", "a")
        file.write(username_info)
        file.write("\t")
        file.write(cedula_info)
        file.write("\t")
        file.write(tlf_info)
        file.write("\t")
        file.write(correo_info)
        file.write("\t\n")
        file.write(direccion_info)
        print(f" Datos del Registro:\n"
              f" Nombres: {username_info} --- Cedula {cedula_info}\n"
              f"Telefono: {tlf_info} --- Correo: {correo_info}"
              f"Direccion: {direccion_info} ")
        #  Delete data from previous event
        username_entry.delete(0, END)
        cedula_entry.delete(0, END)
        tlf_entry.delete(0, END)
        correo_entry.delete(0, END)
        direccion_entry.delete(0, END)

    # Create new instance - Class cTk()
    mywindow = ctk.CTk()
    mywindow.geometry("700x600")
    mywindow.title("Registro")
    mywindow.resizable(False, False)
    mywindow.config(background="#213141")
    main_title = ctk.CTkLabel(mywindow, text="Registro | Alumnos", font=("Cambria", 19),
                              fg_color="gray21", width=500, height=2)
    main_title.pack(fill="x")

    # Define Label Fields
    h = 110
    username_label = Label(mywindow, text="Nombre ", font=("Cambria", 16),
                           width=7, height=1, fg="white", anchor="center",
                           justify="center", bg="#213141")
    username_label.place(x=h, y=30)
    cedula_label = Label(mywindow, text="Cedula ", font=("Cambria", 16),
                         width=7, height=1, fg="white", anchor="center",
                         justify="center", bg="#213141")
    cedula_label.place(x=h, y=110)

    tlf_label = Label(mywindow, text="Telefono ", font=("Cambria", 16),
                      width=7, height=1, fg="white", anchor="center",
                      justify="center", bg="#213141")
    tlf_label.place(x=h, y=190)

    correo_label = Label(mywindow, text="Correo ", font=("Cambria", 16),
                         width=7, height=1, fg="white",
                         anchor="center", justify="center", bg="#213141")
    correo_label.place(x=h, y=270)

    direccion_label = Label(mywindow, text="Direccion ", font=("Cambria", 16),
                            width=7, height=1, fg="white",
                            anchor="center", justify="center", bg="#213141")
    direccion_label.place(x=h, y=350)

    # Get and store data from users
    username = StringVar()
    cedula = StringVar()
    tlf = StringVar()
    correo = StringVar()
    direccion = StringVar()

    # Funct for invalid entries
    def mostrar_error():
        valor1 = username_entry.get()
        valor2 = cedula_entry.get()
        valor3 = tlf_entry.get()

        if valor1 != "" and valor2 != "" and valor3 != "":
            return
        # Validamos el valor de la entrada de texto
        messagebox.showerror("Error", "La entrada no es válida")

    vcmd = mywindow.register(mostrar_error)

    # creacion de los entry
    username_entry = ctk.CTkEntry(mywindow, textvariable=username, font=("Cambria", 16),
                                  justify="center", width=485, height=35, text_color="black",
                                  placeholder_text="Primer Nombre", placeholder_text_color="black",
                                  fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))

    cedula_entry = ctk.CTkEntry(mywindow, textvariable=cedula, font=("Cambria", 16),
                                justify="center", width=485, height=35, text_color="black",
                                placeholder_text="Primer Nombre", placeholder_text_color="black",
                                fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))

    tlf_entry = ctk.CTkEntry(mywindow, textvariable=tlf, font=("Cambria", 16),
                             justify="center", width=485, height=35, text_color="black",
                             placeholder_text="Primer Nombre", placeholder_text_color="black",
                             fg_color="snow2")

    correo_entry = ctk.CTkEntry(mywindow, textvariable=correo, font=("Cambria", 16),
                                justify="center", width=485, height=35, text_color="black",
                                placeholder_text="Primer Nombre", placeholder_text_color="black",
                                fg_color="snow2", validate="focusout", validatecommand=(vcmd, "%P"))
    direccion_entry = ctk.CTkEntry(mywindow, textvariable=direccion, font=("Cambria", 16),
                                   justify="center", width=485, height=35, text_color="black", fg_color="snow2")

    # Entries positioning
    a = 110
    username_entry.place(x=a, y=70)
    cedula_entry.place(x=a, y=150)
    tlf_entry.place(x=a, y=230)
    correo_entry.place(x=a, y=310)
    direccion_entry.place(x=a, y=390)

    # Submit Button
    submit_btn = CTkButton(mywindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", command=lambda: [mostrar_error(), send_data()])

    submit_btn.place(x=300, y=540)
    # bucle
    mywindow.mainloop()


def opcion():
    print("Opcion: No se que va aqui aun")
