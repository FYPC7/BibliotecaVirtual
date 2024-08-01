import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
import io
import os
import pandas as pd

class UsuariosApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        self.image_path = None
        self.populate_tree()

    def setup_ui(self):
        self.tree = ttk.Treeview(self, columns=('idusuario', 'NOMBRES', 'APELLIDOS', 'EMAIL', 'idrol'), show='headings')
        self.tree.heading('idusuario', text='ID')
        self.tree.heading('NOMBRES', text='Nombres')
        self.tree.heading('APELLIDOS', text='Apellidos')
        self.tree.heading('EMAIL', text='Email')
        self.tree.heading('idrol', text='ID Rol')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.create_form()
        self.create_buttons()

    def create_form(self):
        self.nombres_label = ttk.Label(self.form_frame, text="Nombres:")
        self.nombres_label.grid(row=0, column=0)
        self.nombres_entry = ttk.Entry(self.form_frame)
        self.nombres_entry.grid(row=0, column=1)

        self.apellidos_label = ttk.Label(self.form_frame, text="Apellidos:")
        self.apellidos_label.grid(row=1, column=0)
        self.apellidos_entry = ttk.Entry(self.form_frame)
        self.apellidos_entry.grid(row=1, column=1)

        self.email_label = ttk.Label(self.form_frame, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = ttk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1)

        self.idrol_label = ttk.Label(self.form_frame, text="ID Rol:")
        self.idrol_label.grid(row=3, column=0)
        self.idrol_entry = ttk.Entry(self.form_frame)
        self.idrol_entry.grid(row=3, column=1)

        self.photo_label = ttk.Label(self.form_frame, text="Foto de perfil:")
        self.photo_label.grid(row=4, column=0)
        self.photo_button = ttk.Button(self.form_frame, text="Seleccionar imagen", command=self.load_image)
        self.photo_button.grid(row=4, column=1)
