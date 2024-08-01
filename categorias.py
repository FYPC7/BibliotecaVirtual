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
    
