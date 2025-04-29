import sys
import os

# Asegura que el directorio actual está en el path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import database as db

import tkinter as tk
from tkinter import ttk, messagebox


class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Clientes")
        self.root.geometry("500x400")

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("DNI", "Nombre", "Apellido"), show="headings")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.formulario()

        self.actualizar_lista()

    def formulario(self):
        form = ttk.Frame(self.root, padding=10)
        form.pack()

        ttk.Label(form, text="DNI:").grid(row=0, column=0)
        self.dni_entry = ttk.Entry(form)
        self.dni_entry.grid(row=0, column=1)

        ttk.Label(form, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = ttk.Entry(form)
        self.nombre_entry.grid(row=1, column=1)

        ttk.Label(form, text="Apellido:").grid(row=2, column=0)
        self.apellido_entry = ttk.Entry(form)
        self.apellido_entry.grid(row=2, column=1)

        ttk.Button(form, text="Añadir", command=self.añadir_cliente).grid(row=3, column=0)
        ttk.Button(form, text="Modificar", command=self.modificar_cliente).grid(row=3, column=1)
        ttk.Button(form, text="Borrar", command=self.borrar_cliente).grid(row=3, column=2)

    def actualizar_lista(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for c in db.Clientes.lista:
            self.tree.insert("", tk.END, values=(c.dni, c.nombre, c.apellido))

    def añadir_cliente(self):
        dni = self.dni_entry.get().upper()
        if not self.validar_dni(dni):
            return
        if db.Clientes.buscar(dni):
            messagebox.showerror("Error", "DNI ya registrado.")
            return
        nombre = self.nombre_entry.get().capitalize()
        apellido = self.apellido_entry.get().capitalize()
        db.Clientes.crear(dni, nombre, apellido)
        self.actualizar_lista()
        self.limpiar_entradas()

    def modificar_cliente(self):
        dni = self.dni_entry.get().upper()
        cliente = db.Clientes.buscar(dni)
        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return
        nombre = self.nombre_entry.get().capitalize()
        apellido = self.apellido_entry.get().capitalize()
        db.Clientes.modificar(dni, nombre, apellido)
        self.actualizar_lista()
        self.limpiar_entradas()

    def borrar_cliente(self):
        dni = self.dni_entry.get().upper()
        if not db.Clientes.borrar(dni):
            messagebox.showerror("Error", "Cliente no encontrado.")
        else:
            self.actualizar_lista()
            self.limpiar_entradas()

    def limpiar_entradas(self):
        self.dni_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)

    def validar_dni(self, dni):
        import re
        if not re.match(r'^[0-9]{2}[A-Z]$', dni):
            messagebox.showerror("Error", "DNI inválido. Formato: 2 dígitos y 1 letra mayúscula.")
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()



