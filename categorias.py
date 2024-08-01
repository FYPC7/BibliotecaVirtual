import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class CategoriasApp(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        self.create_table()
        self.populate_tree()
        self.populate_initial_data()
        
     def setup_ui(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.grid(row=0, column=0, sticky='nsew')
        self.tree = ttk.Treeview(self, columns=('idcategoria', 'NOMBRE'), show='headings')
        self.tree.heading('idcategoria', text='ID')
        self.tree.heading('NOMBRE', text='Nombre')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10, fill='x')

        self.nombre_label = ttk.Label(self.form_frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
