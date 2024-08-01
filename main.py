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

USERS = {
    "admin": {"password": "admin.45", "role": "admin"},
    "bibliotecario": {"password": "bibliotecario.45", "role": "bibliotecario"},
    "estudiante": {"password": "estudiante.45", "role": "estudiante"},
}

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("login")
        self.geometry("600x400")
        self.configure(bg="#2C3E50")

        # Crear los widgets
        self.create_widgets()
        
     def create_widgets(self):
        welcome_label = ttk.Label(
            self, 
            text="BIENVENIDO A LA BIBLIOTECA UNIVERSITARIA", 
            foreground='#ECF0F1', 
            font=("Verdana", 14, "bold"),
            background='#2C3E50'
        )
        welcome_label.pack(pady=(20, 10))

        self.role_label = ttk.Label(self, text="Role:", foreground='#ECF0F1', background='#2C3E50')
        self.role_label.pack(pady=6)
        self.role_combobox = ttk.Combobox(self, values=["admin", "bibliotecario", "estudiante"], state='readonly')
        self.role_combobox.set("admin")  
        self.role_combobox.pack(pady=6)

        self.username_label = ttk.Label(self, text="Username:", foreground='#ECF0F1', background='#2C3E50')
        self.username_label.pack(pady=(6, 6))
        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.pack(pady=6)

        self.password_label = ttk.Label(self, text="Password:", foreground='#ECF0F1', background='#2C3E50')
        self.password_label.pack(pady=6)
        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.pack(pady=6)

        self.login_button = ttk.Button(self, text="INGRESAR", command=self.check_credentials, width=15)
        self.login_button.pack(pady=20)


    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_combobox.get()

        if username in USERS and USERS[username]["password"] == password and USERS[username]["role"] == role:
            self.destroy()
            app = MainApp(role)
            app.mainloop()
        else:
            messagebox.showerror("Error", "Invalid credentials or role")
