import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class LibrosApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.style = ttk.Style()
        self.style.configure('Treeview',
                             background='#f0f0f0',
                             foreground='#333333',
                             fieldbackground='#e6e6e6',
                             font=('Helvetica', 12))
        self.style.configure('Treeview.Heading',
                             background='#4CAF50',
                             foreground='white',
                             font=('Helvetica', 14, 'bold'))
        self.style.configure('TButton',
                             relief='flat',
                             background='#4CAF50',
                             foreground='white',
                             font=('Helvetica', 12, 'bold'))
        self.style.map('TButton',
                       background=[('active', '#45a049')],
                       relief=[('pressed', 'sunken')])

        self.tree = ttk.Treeview(self, columns=('idlibro', 'TITULO', 'idcategoria', 'AUTOR', 'ISBN'), show='headings')
        self.tree.heading('idlibro', text='ID')
        self.tree.heading('TITULO', text='Título')
        self.tree.heading('AUTOR', text='Autor')
        self.tree.heading('idcategoria', text='ID Categoría')
        self.tree.heading('ISBN', text='ISBN')
        self.tree.column('idlibro', width=50)
        self.tree.column('TITULO', width=200)
        self.tree.column('AUTOR', width=150)
        self.tree.column('idcategoria', width=100)
        self.tree.column('ISBN', width=150)
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10, padx=10, fill='x')

        # Labels y Entries del formulario
        self.create_form()

        # Botones de acción
        self.create_buttons()

        # Cargar datos
        self.populate_tree()

    def create_form(self):
        
        self.titulo_label = ttk.Label(self.form_frame, text="Título:", font=('Helvetica', 12))
        self.titulo_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.titulo_entry = ttk.Entry(self.form_frame, width=30, font=('Helvetica', 12))
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.autor_label = ttk.Label(self.form_frame, text="Autor:", font=('Helvetica', 12))
        self.autor_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.autor_entry = ttk.Entry(self.form_frame, width=30, font=('Helvetica', 12))
        self.autor_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.categoria_label = ttk.Label(self.form_frame, text="ID Categoría:", font=('Helvetica', 12))
        self.categoria_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.categoria_entry = ttk.Entry(self.form_frame, width=30, font=('Helvetica', 12))
        self.categoria_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.isbn_label = ttk.Label(self.form_frame, text="ISBN:", font=('Helvetica', 12))
        self.isbn_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.isbn_entry = ttk.Entry(self.form_frame, width=30, font=('Helvetica', 12))
        self.isbn_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    def create_buttons(self):
      
        button_frame = ttk.Frame(self.form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.add_button = ttk.Button(button_frame, text="Agregar", command=self.add_libro)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = ttk.Button(button_frame, text="Editar", command=self.edit_libro)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = ttk.Button(button_frame, text="Eliminar", command=self.delete_libro)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:", font=('Helvetica', 12))
        self.search_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.search_entry = ttk.Entry(self.form_frame, width=30, font=('Helvetica', 12))
        self.search_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_libro)
        self.search_button.grid(row=5, column=2, padx=5)

        import_export_frame = ttk.Frame(self.form_frame)
        import_export_frame.grid(row=6, column=0, columnspan=3, pady=10)

        self.import_button = ttk.Button(import_export_frame, text="Importar Excel", command=self.import_excel)
        self.import_button.grid(row=0, column=0, padx=5)

        self.export_button = ttk.Button(import_export_frame, text="Exportar Excel", command=self.export_excel)
        self.export_button.grid(row=0, column=1, padx=5)
