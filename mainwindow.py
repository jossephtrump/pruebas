# Importamos los módulos necesarios
import tkinter as tk
from tkinter import *
import customtkinter
from customtkinter import CTkEntry, CTkButton
from ttkthemes import ThemedTk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import customtkinter as ctk
from menu_registro import *
from funciones2 import *
#from funct import *

# Creamos una ventana principal
root = ctk.CTk()

root.title("LS Software")
root.geometry("1366x768+1+1")
#title_label = Label(root, text="LS Software")

root.config(background="gray21")

# Creamos un canvas con un color de fondo y sin bordes
canvas = tk.Canvas(root, width=1280, height=720, bg="gray21",
                   highlightthickness=0)
canvas.pack()

# Cargamos una imagen desde un archivo
#imagen = Image.open("image.png")
# La convertimos a un formato compatible con tkinter
photo = PhotoImage(file="image.png")
# Creamos una imagen sobre el canvas con la foto cargada
canvas_image = canvas.create_image(650, 270, image=photo, anchor=CENTER)

window = root
# creacion del entry
entry = ctk.CTkEntry(window, width=285, height=38,
                               fg_color="snow2", text_color="black",
                               font=("arial", 20), placeholder_text="ej: 18123456",
                               justify="center")
# aqui la ubicamos:
entry.place(x=676, y=621, anchor=CENTER)

#funciones para bottones
def agregar():
    cedula = entry.get()
    print("accion para registrar pago de mensualidad: " + cedula)

def buscar():
    cedula = entry.get()
    print("accion para buscar estado de cuenta del representante:  "
          + cedula)

#Boton de agregar para registrar pagos de mensualidades

add_button = CTkButton(window, text="Agregar", font=("arial", 16),
                       anchor=CENTER, width=10, command=agregar)
add_button.place(x=685, y=657, anchor=CENTER)

#buscar_button = busqueda con la CI para ver estado de cuenta del representante
buscar_button = CTkButton(window, text="Buscar",
                          font=("arial", 16),
                          width=10, height=37, command=buscar)
buscar_button.place(x=855, y=621, anchor=CENTER)

# Crear una instancia de Menu
menu_bar = Menu(root, background="black")
# Asignar la barra de menú a la ventana
root.config(menu=menu_bar)

# Crear un elemento de menú "Archivo"
archivo_menu = Menu(menu_bar, tearoff=0, font=("calibri", 11),
                    background="gray80")
menu_bar.add_cascade(label="ARCHIVO", font=("calibri", 18),
                     menu=archivo_menu)

archivo_menu.add_command(label="Nuevo", command=nuevo)
archivo_menu.add_command(label="Abrir",command=abrir )
archivo_menu.add_command(label="Importar", command=importar)
archivo_menu.add_command(label="Exportar", command=exportar)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

# Agregar el elemento de menú "Registro" a la barra de menú
registro_menu = Menu(menu_bar, tearoff=0, font=("calibri", 11),
                    background="gray80")
menu_bar.add_cascade(label="REGISTRO", menu=registro_menu)

registro_menu.add_command(label="Representante", command=representante)
registro_menu.add_command(label="Alumno", command=alumno)
registro_menu.add_command(label="opcion 3", command=opcion)

# construccion del menu PAGOS
pagos_menu = Menu(menu_bar, tearoff=0, font=("calibri", 11),
                    background="gray80")
menu_bar.add_cascade(label="PAGOS", menu=pagos_menu)

pagos_menu.add_command(label="Inscripcion")
pagos_menu.add_command(label="Mensualidad")
pagos_menu.add_command(label="Cierre Diario", command=cierre)
pagos_menu.add_command(label="Facturas")

# Agregar el elemento "CONSULTAS" a la barra de menú
consultas_menu = Menu(menu_bar, tearoff=0, font=("calibri", 11),
                    background="gray80")
#creating cascade
menu_bar.add_cascade(label="CONSULTAS", menu=consultas_menu)
#creating elements for cascade
consultas_menu.add_command(label="Info Representante")
consultas_menu.add_command(label="Info Alumnos")
#CREAR SUB_MENU MOROSIDAD
morosidad_menu = Menu(consultas_menu, tearoff=0, font=("calibri", 11),
                    background="gray80")
morosidad_menu.add_command(label="Por Alumno")
morosidad_menu.add_command(label="Por Grado")
morosidad_menu.add_command(label="Por Seccion")
morosidad_menu.add_command(label="TOTAL")
consultas_menu.add_cascade(label="MOROSIDAD", menu=morosidad_menu)
consultas_menu.add_command(label="opcion 4") #extra option

# Agregar cuentas por cobrar
cobranza_menu = Menu(menu_bar, tearoff=0, font=("calibri", 11),
                    background="gray80")
menu_bar.add_cascade(label="COBRANZA", menu=cobranza_menu)

cobranza_menu.add_command(label="Por Alumno")
cobranza_menu.add_command(label="Por Grado")
cobranza_menu.add_command(label="Por Seccion")
cobranza_menu.add_command(label="TOTAL")

# Iniciamos el bucle principal de la ventana
root.mainloop()