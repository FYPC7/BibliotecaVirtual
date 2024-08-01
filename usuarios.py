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

    def create_buttons(self):
        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_usuario)
        self.add_button.grid(row=5, column=0, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_usuario)
        self.edit_button.grid(row=5, column=1, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_usuario)
        self.delete_button.grid(row=5, column=2, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=6, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_usuario)
        self.search_button.grid(row=6, column=2)

        self.generate_button = ttk.Button(self.form_frame, text="Generar Carnet", command=self.generate_carnet)
        self.generate_button.grid(row=7, column=1, pady=10)

        self.import_button = ttk.Button(self.form_frame, text="Importar Excel", command=self.import_excel)
        self.import_button.grid(row=8, column=0, pady=10)

        self.export_button = ttk.Button(self.form_frame, text="Exportar Excel", command=self.export_excel)
        self.export_button.grid(row=8, column=1, pady=10)

    def execute_query(self, query, parameters=()):
        try:
            connection = sqlite3.connect('biblioteca.db')
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            connection.close()

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute('SELECT idusuario, NOMBRES, APELLIDOS, EMAIL, idrol FROM usuarios')
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            self.tree.insert('', tk.END, values=usuario)
        connection.close()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img.thumbnail((100, 100))  # Redimensiona la imagen a un tamaño pequeño
            self.profile_image = ImageTk.PhotoImage(img)
            self.photo_label.configure(image=self.profile_image)
            self.photo_label.image = self.profile_image

    def add_usuario(self):
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        email = self.email_entry.get()
        idrol = self.idrol_entry.get()

        if nombres and apellidos and email and idrol and self.image_path:
            with open(self.image_path, 'rb') as f:
                image_data = f.read()
            self.execute_query('''
                INSERT INTO usuarios (NOMBRES, APELLIDOS, EMAIL, idrol, foto_perfil) 
                VALUES (?, ?, ?, ?, ?)
            ''', (nombres, apellidos, email, idrol, image_data))
            messagebox.showinfo("Éxito", "Usuario agregado correctamente")
            self.populate_tree()
            self.clear_form()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def edit_usuario(self):
        selected_item = self.tree.selection()
        if selected_item:
            nombres = self.nombres_entry.get()
            apellidos = self.apellidos_entry.get()
            email = self.email_entry.get()
            idrol = self.idrol_entry.get()
            usuario_id = self.tree.item(selected_item)['values'][0]

            if nombres and apellidos and email and idrol:
                self.execute_query('''
                    UPDATE usuarios SET NOMBRES=?, APELLIDOS=?, EMAIL=?, idrol=? WHERE idusuario=?
                ''', (nombres, apellidos, email, idrol, usuario_id))
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                self.populate_tree()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            messagebox.showerror("Error", "Por favor, selecciona un usuario para editar")

    def delete_usuario(self):
        selected_item = self.tree.selection()
        if selected_item:
            usuario_id = self.tree.item(selected_item)['values'][0]

            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de querer eliminar este usuario?")
            if confirm:
                self.execute_query('''
                    DELETE FROM usuarios WHERE idusuario=?
                ''', (usuario_id,))
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
                self.populate_tree()
                self.clear_form()
        else:
            messagebox.showerror("Error", "Por favor, selecciona un usuario para eliminar")

    def clear_form(self):
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.idrol_entry.delete(0, tk.END)
        self.image_path = None
        self.photo_label.configure(image='')
