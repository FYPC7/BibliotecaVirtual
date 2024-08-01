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

         
        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_categoria)
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_categoria)
        self.edit_button.grid(row=2, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_categoria)
        self.delete_button.grid(row=2, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=3, column=0, padx=5, pady=5)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=3, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_categoria)
        self.search_button.grid(row=3, column=2, padx=5, pady=5)

        for col in self.tree['columns']:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c, False))

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS categorias (
                idcategoria TEXT PRIMARY KEY,
                NOMBRE TEXT NOT NULL
            )
        ''')
