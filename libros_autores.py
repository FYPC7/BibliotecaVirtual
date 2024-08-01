import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class LibrosAutoresApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        self.populate_tree()
