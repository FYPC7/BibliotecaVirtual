import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class PrestamosApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = ttk.Treeview(self, columns=('idprestamo', 'idlibro', 'idusuario', 'fecha_prestamo', 'fecha_devolucion'), show='headings')
        self.tree.heading('idprestamo', text='ID')
        self.tree.heading('idlibro', text='ID Libro')
        self.tree.heading('idusuario', text='ID Usuario')
        self.tree.heading('fecha_prestamo', text='Fecha Prestamo')
        self.tree.heading('fecha_devolucion', text='Fecha Devolucion')
        self.tree.pack(expand=True, fill='both')

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.idlibro_label = ttk.Label(self.form_frame, text="ID Libro:")
        self.idlibro_label.grid(row=0, column=0)
        self.idlibro_entry = ttk.Entry(self.form_frame)
        self.idlibro_entry.grid(row=0, column=1)

        self.idusuario_label = ttk.Label(self.form_frame, text="Nombre Usuario:")
        self.idusuario_label.grid(row=1, column=0)
        self.idusuario_entry = ttk.Entry(self.form_frame)
        self.idusuario_entry.grid(row=1, column=1)

        self.fecha_prestamo_label = ttk.Label(self.form_frame, text="Fecha Prestamo (YYYY-MM-DD):")
        self.fecha_prestamo_label.grid(row=2, column=0)
        self.fecha_prestamo_entry = ttk.Entry(self.form_frame)
        self.fecha_prestamo_entry.grid(row=2, column=1)

        self.fecha_devolucion_label = ttk.Label(self.form_frame, text="Fecha Devolucion (YYYY-MM-DD):")
        self.fecha_devolucion_label.grid(row=3, column=0)
        self.fecha_devolucion_entry = ttk.Entry(self.form_frame)
        self.fecha_devolucion_entry.grid(row=3, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_prestamo)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_prestamo)
        self.edit_button.grid(row=5, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_prestamo)
        self.delete_button.grid(row=5, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=6, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_prestamo)
        self.search_button.grid(row=6, column=2)

        self.import_button = ttk.Button(self.form_frame, text="Importar Excel", command=self.import_excel)
        self.import_button.grid(row=7, column=0, pady=10)

        self.export_button = ttk.Button(self.form_frame, text="Exportar Excel", command=self.export_excel)
        self.export_button.grid(row=7, column=1, pady=10)

        self.create_table()
        self.populate_tree()
