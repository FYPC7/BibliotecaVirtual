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
