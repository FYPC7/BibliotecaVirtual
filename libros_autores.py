import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class LibrosAutoresApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        self.populate_tree()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", font=("Helvetica", 10))
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TButton", font=("Helvetica", 10, "bold"), foreground="white", background="#007ACC")
        
        self.tree = ttk.Treeview(self, columns=('idlibro', 'idautor'), show='headings')
        self.tree.heading('idlibro', text='ID Libro')
        self.tree.heading('idautor', text='ID Autor')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10, padx=10, fill='x')

        self.idlibro_label = ttk.Label(self.form_frame, text="ID Libro:")
        self.idlibro_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.idlibro_entry = ttk.Entry(self.form_frame)
        self.idlibro_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.idautor_label = ttk.Label(self.form_frame, text="ID Autor:")
        self.idautor_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.idautor_entry = ttk.Entry(self.form_frame)
        self.idautor_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_libro_autor)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_libro_autor)
        self.edit_button.grid(row=3, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_libro_autor)
        self.delete_button.grid(row=3, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_libro_autor)
        self.search_button.grid(row=4, column=2, padx=5, pady=5)
