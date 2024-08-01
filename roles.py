import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class RolesApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = ttk.Treeview(self, columns=('idrol', 'NOMBRE'), show='headings')
        self.tree.heading('idrol', text='ID')
        self.tree.heading('NOMBRE', text='Nombre')
        self.tree.pack(expand=True, fill='both')

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.nombre_label = ttk.Label(self.form_frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = ttk.Entry(self.form_frame)
        self.nombre_entry.grid(row=0, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_rol)
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_rol)
        self.edit_button.grid(row=2, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_rol)
        self.delete_button.grid(row=2, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=3, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=3, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_rol)
        self.search_button.grid(row=3, column=2)

        self.populate_tree()

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

