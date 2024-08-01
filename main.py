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


class MainApp(tk.Tk):
    def __init__(self, role):
        super().__init__()

        self.role = role
        self.title("BIBLIOTECA UNIVERSITARIA")
        self.geometry("1200x800")

        self.style = ttk.Style(self)
        self.configure_style()

        self.create_header()

        self.notebook = ttk.Notebook(self, style="Custom.TNotebook")
        self.notebook.pack(expand=True, fill='both', padx=20, pady=20)

        self.add_tabs()

        self.conn = sqlite3.connect('library.db')

    def configure_style(self):
        self.style.theme_create("custom_theme", parent="alt", settings={
            "TNotebook": {
                "configure": {
                    "tabmargins": [0, 5, 0, 0],
                    "background": "#34495E",
                    "borderwidth": 0,
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [15, 10],
                    "font": ('Arial', 12, 'bold'),
                },
                "map": {
                    "background": [("selected", "#1ABC9C"), ("active", "#16A085")],
                    "foreground": [("selected", "#ffffff"), ("active", "#000000")],
                    "expand": [("selected", [1, 1, 1, 0])],
                    "padding": [("selected", [15, 10])],
                }
            },
            "TFrame": {
                "configure": {
                    "background": "#ECF0F1",
                }
            },
            "TLabel": {
                "configure": {
                    "background": "#ECF0F1",
                    "foreground": "#2C3E50",
                }
            },
            "TButton": {
                "configure": {
                    "padding": [5, 5],
                    "background": "#1ABC9C",
                    "foreground": "#ffffff",
                    "borderwidth": 1,
                    "relief": "flat",
                },
                "map": {
                    "background": [("active", "#16A085")],
                    "foreground": [("active", "#000000")],
                }
            }
        })
        self.style.theme_use("custom_theme")
