from tkinter import *
import tkinter as tkinter
import customtkinter
from customtkinter import *
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
import MySQLdb as mysql
from datetime import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



mydb = mysql.connect(host='localhost',user='root',passwd='',db='colegio')
cur = mydb.cursor()


def inscripcion():
    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("500x500")
    mwindow.title("Pago de Inscripcion")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")
    main_title = ctk.CTkLabel(mwindow, text="PAGO | INSCRIPCION", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    global cedula_entry
    global representante_entry
    global cantidad_pago

    cedula_entry = StringVar()
    representante_entry = StringVar()
    cantidad_pago = IntVar()

    def mostrar_error():
        valor1 = representante_entry.get() 
        valor2 = cedula_entry.get()
        valor3 = cantidad_pago.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "":
            messagebox.showerror("Error", "Cedula del Representante")
            return True
        elif  valor2 == "":
            messagebox.showerror("Error",  "Ingrese IDCedula")
            return True
        elif  valor3 == "":
            messagebox.showerror("Error", "Ingrese Monto")
            return True
        return False

    vcmd = mwindow.register(mostrar_error)


    h = 100
    w = 25
    representante_label = Label(mwindow,text="Cedula Representante", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=50)
    representante_entry= Entry(mwindow,textvariable=representante_entry, font=("Cambria", 16), width=w, 
                               justify="center", validatecommand=(vcmd, "%P"))
    representante_entry.place(x=h, y=90)

    id_alumno = Label(mwindow,text="IDCedula Alumno ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=140)
    cedula_entry= Entry(mwindow,textvariable=cedula_entry, font=("Cambria", 16), width=w, 
                        justify="center", validatecommand=(vcmd, "%P"))
    cedula_entry.place(x=h, y=180)

    monto_label =  Label(mwindow,text="MONTO", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=230)
    cantidad_pago= Entry(mwindow,textvariable=cantidad_pago, font=("Cambria", 16), width=w, 
                        justify="center", validatecommand=(vcmd, "%P"))
    cantidad_pago.place(x=h, y=270)

    submit_btn = CTkButton(mwindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", command=lambda: [insertinscrip() if not mostrar_error() else None]) 
    submit_btn.place(x=200, y=350)

    submit_btn = CTkButton(mwindow, text="factura", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                           command=lambda: generar_factura_pdf('{0}.pdf'.format(cedula_entry.get())))
    submit_btn.place(x=200, y=400)
    
    mwindow.mainloop()

def insertinscrip():
        
        hora_min = datetime.now().strftime("%H:%M")
        print("Hora y Minutos: ", hora_min)
        # Crea una variable para el día, mes y año
        dia_mes_anio = datetime.now().strftime("%Y/%m/%d")
        print("Día/Mes/Año: ", dia_mes_anio)

        #sentencias
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
            representante_entry.delete(0, END)
            cedula_entry.delete(0, END)
            cantidad_pago.delete(0, END)
    

def pago_mensualidad():
    global mwindow
    mwindow = ctk.CTk()
    mwindow.geometry("500x500")
    mwindow.title("PAGOS")
    mwindow.resizable(False, False)
    mwindow.config(background="#213141")
    main_title = ctk.CTkLabel(mwindow, text="PAGO | MES", font=("Cambria", 20),
                              fg_color="gray21", width=500, height=3)
    main_title.pack(fill="x")

    global cantidad_pago
    global cedula_entry
    global representante_entry
  

    cedula_entry = StringVar()
    representante_entry = StringVar()
    cantidad_pago = IntVar()

    def mostrar_error():
        valor1 = representante_entry.get()
        valor2 = cedula_entry.get()
        valor3 = cantidad_pago.get()

        # Validamos el valor de la entrada de texto
        if valor1 == "":
            messagebox.showerror("Error", "Cedula del Representante")
            return True
        elif valor2 == "":
            messagebox.showerror("Error", "Ingrese IDCedula")
            return True
        elif valor3 == "":
            messagebox.showerror("Error", "Ingrese Monto")
            return True
        return False

    vcmd = mwindow.register(mostrar_error)

    h = 100
    w = 25
    representate_label = Label(mwindow,text="Cedula Representante", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=50)
    representante_entry= Entry(mwindow,textvariable=representante_entry, font=("Cambria", 16), 
                               width=w, justify="center", validatecommand=(vcmd, "%P"))
    representante_entry.place(x=h, y=90)

    cedula_label = Label(mwindow,text="IDCedula ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=140)
    cedula_entry= Entry(mwindow,textvariable=cedula_entry, font=("Cambria", 16), width=w,
                         justify="center", validatecommand=(vcmd, "%P"))
    cedula_entry.place(x=h, y=180)
    
    cantidad_label = Label(mwindow,text="MONTO PAGADO ", font=("Cambria", 16),
                         width=35, height=1, fg="white", anchor=W,
                         justify="center", bg="#213141").place(x=h, y=230)
    cantidad_pago = Entry(mwindow,textvariable=cantidad_pago, font=("Cambria", 16), width=w, 
                          justify="center", validatecommand=(vcmd, "%P"))
    cantidad_pago.place(x=h, y=270)

    submit_btn = CTkButton(mwindow, text="GUARDAR", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                           command=lambda: [factura() if not mostrar_error() else None])
    submit_btn.place(x=200, y=350)


    submit_btn = CTkButton(mwindow, text="factura", font=("Cambria", 18),
                           width=30, height=20, anchor="center", 
                           command=lambda: generar_factura_pdf("{0}.pdf".format(cedula_entry.get())))
    submit_btn.place(x=200, y=400)

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
        cedula_entry.delete(0, END)
        representante_entry.delete(0, END)
        cantidad_pago.delete(0, END)




def generar_factura_pdf(archivo):
    global nombre   

    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')

    # Agregar la carpeta 'pdfs' a la ruta del archivo
    archivo = os.path.join('pdfs', cedula_entry.get())

   
    sql = "SELECT direccion  FROM representante WHERE cedula = '{0}'".format(representante_entry.get())
    cur.execute(sql)
    direccion = cur.fetchone()[0]


    sql2 = "SELECT nombre FROM representante WHERE cedula = '{0}'".format(representante_entry.get())
    cur.execute(sql2)
    nombre = cur.fetchone()[0]

    sql3= "SELECT nombre FROM alumno WHERE cedula = '{0}'".format(cedula_entry.get())
    cur.execute(sql3)
    estudiante= cur.fetchone()[0]

    print(estudiante)

    c = canvas.Canvas(archivo, pagesize=letter)
    width, height = letter
    total = 0
    y = height - 50

    c.setFont("Helvetica", 20)
    c.drawString(50, y, "U. S. P. INTEGRAL EL PRADO")

    y -= 30
    c.setFont("Helvetica", 16)
    c.drawString(50, y, 'Urb. El Prado Av 70B-79F')

    y -= 30
    c.setFont("Helvetica", 16)
    c.drawString(50, y, 'Pquia. Raul Leoni Maracaibo')

    y -= 30
    c.setFont("Helvetica", 16)
    c.drawString(50, y, 'telef: 0261-7544608')

    fecha = datetime.now().strftime("%Y/%m")
    fecha2 = datetime.now().strftime("%Y/%m/%d")


    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, 'representante: {0}'.format(nombre))
    c.drawString(300, y, 'fecha: {0}'.format(fecha2))

    y -= 30
    c.drawString(50, y, 'direccion: {0}'.format(direccion))
    c.drawString(300, y, 'CI/RIF: {0}'.format( representante_entry.get()))

    y -= 30
    
    
    y -= 30
    

    y -= 30
    c.drawString(50, y, 'DESCRIPCION ')

    y -= 30
    c.drawString(50, y, 'MENSUALIDAD {0}  {1}'.format(fecha, estudiante))

    y -= 30
    c.drawString(50, y, 'TOTAL: {0}'.format(cantidad_pago.get()))

    c.save()


   
        