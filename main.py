import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from autores import AutoresApp
from categorias import CategoriasApp
from libros import LibrosApp
from libros_autores import LibrosAutoresApp
from prestamos import PrestamosApp
from roles import RolesApp
from usuarios import UsuariosApp



class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("login")
        self.geometry("600x400")
        self.configure(bg="#2C3E50")

        # Crear los widgets
        self.create_widgets()

