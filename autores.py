import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class AutoresApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.tree = ttk.Treeview(self, columns=('idautor', 'NOMBRES', 'APELLIDOS', 'DNI', 'NACIONALIDAD'), show='headings')
        self.tree.heading('idautor', text='ID')
        self.tree.heading('NOMBRES', text='Nombres')
        self.tree.heading('APELLIDOS', text='Apellidos')
        self.tree.heading('DNI', text='DNI')
        self.tree.heading('NACIONALIDAD', text='Nacionalidad')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.nombres_label = ttk.Label(self.form_frame, text="Nombres:")
        self.nombres_label.grid(row=0, column=0)
        self.nombres_entry = ttk.Entry(self.form_frame)
        self.nombres_entry.grid(row=0, column=1)

        self.apellidos_label = ttk.Label(self.form_frame, text="Apellidos:")
        self.apellidos_label.grid(row=1, column=0)
        self.apellidos_entry = ttk.Entry(self.form_frame)
        self.apellidos_entry.grid(row=1, column=1)

        self.dni_label = ttk.Label(self.form_frame, text="DNI:")
        self.dni_label.grid(row=2, column=0)
        self.dni_entry = ttk.Entry(self.form_frame)
        self.dni_entry.grid(row=2, column=1)

        self.nacionalidad_label = ttk.Label(self.form_frame, text="Nacionalidad:")
        self.nacionalidad_label.grid(row=3, column=0)
        self.nacionalidad_entry = ttk.Entry(self.form_frame)
        self.nacionalidad_entry.grid(row=3, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_autor)
        self.add_button.grid(row=4, column=0, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_autor)
        self.edit_button.grid(row=4, column=1, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_autor)
        self.delete_button.grid(row=4, column=2, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=5, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=5, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_autor)
        self.search_button.grid(row=5, column=2)


