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

