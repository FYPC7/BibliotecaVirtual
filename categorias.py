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
        
     def setup_ui(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.grid(row=0, column=0, sticky='nsew')
        self.tree = ttk.Treeview(self, columns=('idcategoria', 'NOMBRE'), show='headings')
        self.tree.heading('idcategoria', text='ID')
        self.tree.heading('NOMBRE', text='Nombre')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10, fill='x')

        self.nombre_label = ttk.Label(self.form_frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

         
        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_categoria)
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_categoria)
        self.edit_button.grid(row=2, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_categoria)
        self.delete_button.grid(row=2, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=3, column=0, padx=5, pady=5)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=3, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_categoria)
        self.search_button.grid(row=3, column=2, padx=5, pady=5)

        for col in self.tree['columns']:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c, False))

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS categorias (
                idcategoria TEXT PRIMARY KEY,
                NOMBRE TEXT NOT NULL
            )
        ''')

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM categorias')
        categorias = cursor.fetchall()
        for categoria in categorias:
            self.tree.insert('', tk.END, values=categoria)
        connection.close()

    def add_categoria(self):
        nombre = self.nombre_entry.get()

        if nombre:
            cursor = self.tree.get_children()
            new_id = f'Cate.{len(cursor) + 1}'
            self.execute_query('''
                INSERT INTO categorias (idcategoria, NOMBRE) 
                VALUES (?, ?)
            ''', (new_id, nombre))
            messagebox.showinfo("Éxito", "Categoría agregada correctamente")
            self.populate_tree()
        else:
            messagebox.showerror("Error", "El campo nombre es obligatorio")

    def edit_categoria(self):
        selected_item = self.tree.selection()
        if selected_item:
            nombre = self.nombre_entry.get()
            categoria_id = self.tree.item(selected_item)['values'][0]

            if nombre:
                self.execute_query('''
                    UPDATE categorias SET NOMBRE=? WHERE idcategoria=?
                ''', (nombre, categoria_id))
                messagebox.showinfo("Éxito", "Categoría actualizada correctamente")
                self.populate_tree()
                self.clear_form()
            else:
                messagebox.showerror("Error", "El campo nombre es obligatorio")
        else:
            messagebox.showerror("Error", "Por favor, selecciona una categoría para editar")

    def delete_categoria(self):
        selected_item = self.tree.selection()
        if selected_item:
            categoria_id = self.tree.item(selected_item)['values'][0]

            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de querer eliminar esta categoría?")
            if confirm:
                self.execute_query('''
                    DELETE FROM categorias WHERE idcategoria=?
                ''', (categoria_id,))
                messagebox.showinfo("Éxito", "Categoría eliminada correctamente")
                self.populate_tree()
        else:
            messagebox.showerror("Error", "Por favor, selecciona una categoría para eliminar")

    def clear_form(self):
        self.nombre_entry.delete(0, tk.END)
