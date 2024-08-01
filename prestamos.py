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
