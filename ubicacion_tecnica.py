from tkinter import *
from tkinter import messagebox
import sqlite3

# FUNCIONES
def crear_bd():

    conexion=sqlite3.connect("ubicacion tecnica")
    cursor=conexion.cursor()

    try:
        cursor.execute('''
        CREATE TABLE ubicaciones (
        buzon INTEGER UNIQUE NOT NULL,
        ubicacion VARCHAR(50) UNIQUE NOT NULL
        )''')

        messagebox.showinfo("BBDD", "BBDD creada con exito.")

    except:

        messagebox.showwarning("Atención", "La BBDD ya existe.")


def salir():

    valor = messagebox.askquestion("Salir", "Desea salir de la aplicación.")

    if valor == "yes":
        root.destroy()



def insertar():

    conexion=sqlite3.connect("ubicacion tecnica")
    cursor=conexion.cursor()

    datos = consulta.get(), ubicacion.get()

    cursor.execute("INSERT INTO ubicaciones VALUES (?,?)", (datos))

    conexion.commit()

    consulta.set("")
    ubicacion.set("")

    messagebox.showinfo("BBDD","Registro insertado con exito.")


def leer():

    conexion=sqlite3.connect("ubicacion tecnica")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM ubicaciones WHERE buzon="+consulta.get())

    buzones=cursor.fetchall()

    for bzn in buzones:
        consulta.set(bzn[0])
        ubicacion.set(bzn[1])

    conexion.commit()


def actualizar():

    conexion=sqlite3.connect("ubicacion tecnica")
    cursor=conexion.cursor()

    datos=consulta.get(),ubicacion.get()

    cursor.execute('''
    UPDATE ubicaciones SET consulta=?,
    ubicacion=?'''+"WHERE consulta="+consulta.get(), (datos))

    conexion.commit()

    messagebox.showinfo("BBDD","Registro actualizado con exito.")



def borrar():

    conexion=sqlite3.connect("ubicacion tecnica")
    cursor=conexion.cursor()

    cursor.execute("DELETE FROM ubicaciones WHERE consulta="+ consulta.get())

    conexion.commit()

    consulta.set("")
    ubicacion.set("")

    messagebox.showinfo("BBDD","Registro borrado exitosamente!!!")


def licencia():

    messagebox.showinfo("Licencia","Creado por Luchini.")


# CONFIGURAR LA RAIZ
root = Tk()
root.title("Ubicación Tecnica Acarreo")
root.resizable(0,0)

# CONFIGURAR LA BARRA MENÚ
barra_menu = Menu(root)
root.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=crear_bd)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Insertar", command=insertar)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=borrar)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia", command=licencia)

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# CONFIGURAR EL FRAME
frame = Frame(root)
frame.pack()

# PA LOS BOTONES
consulta = StringVar()
ubicacion = StringVar()

# CONFIGURACIÓN DE LA VENTANA
# LOS LABEL
lblBuzon = Label(frame, text = "N° Buzón")
lblBuzon.grid(row=0, column=0, padx=10, pady=10)

lblUbicacion = Label(frame, text = "Ubicacion Tecnica")
lblUbicacion.grid(row=0, column=1, padx=10, pady=10)

# LAS CAJAS DE TEXTO
txtBuzon = Entry(frame)
txtBuzon.grid(row=1, column=0, padx=10, pady=10)

txtUbicacion = Entry(frame)
txtUbicacion.grid(row=1, column=1, padx=10, pady=10)

# LOS BOTONES
btnConsultar = Button(frame, text = "Consultar", command=leer)
btnConsultar.grid(row=3, column=0, padx=10, pady=10)

btnSalir = Button(frame, text="Salir", command=salir)
btnSalir.grid(row=3, column=1, padx=10, pady=10)




root.mainloop()
