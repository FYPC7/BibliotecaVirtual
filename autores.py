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
