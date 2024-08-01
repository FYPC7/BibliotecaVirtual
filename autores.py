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

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.nombres_label = ttk.Label(self.form_frame, text="Nombres:")
        self.nombres_label.grid(row=0, column=0)
        self.nombres_entry = ttk.Entry(self.form_frame)
        self.nombres_entry.grid(row=0, column=1)

        self.apellidos_label = ttk.Label(self.form_frame, text="Apellidos:")
        self.apellidos_label.grid(row=1, column=0)
        self.apellidos_entry = ttk.Entry(self.form_frame)
        self.apellidos_entry.grid(row=1, column=1)

        self.dni_label = ttk.Label(self.form_frame, text="DNI:")
        self.dni_label.grid(row=2, column=0)
        self.dni_entry = ttk.Entry(self.form_frame)
        self.dni_entry.grid(row=2, column=1)

        self.nacionalidad_label = ttk.Label(self.form_frame, text="Nacionalidad:")
        self.nacionalidad_label.grid(row=3, column=0)
        self.nacionalidad_entry = ttk.Entry(self.form_frame)
        self.nacionalidad_entry.grid(row=3, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_autor)
        self.add_button.grid(row=4, column=0, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_autor)
        self.edit_button.grid(row=4, column=1, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_autor)
        self.delete_button.grid(row=4, column=2, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=5, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=5, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_autor)
        self.search_button.grid(row=5, column=2)


        self.import_button = ttk.Button(self.form_frame, text="Importar Excel", command=self.import_excel)
        self.import_button.grid(row=6, column=0, pady=10)

        self.export_button = ttk.Button(self.form_frame, text="Exportar Excel", command=self.export_excel)
        self.export_button.grid(row=6, column=1, pady=10)

        self.create_table()
        self.populate_tree()

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

    def create_table(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS autores (
                idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRES TEXT NOT NULL,
                APELLIDOS TEXT NOT NULL,
                DNI TEXT NOT NULL,
                NACIONALIDAD TEXT NOT NULL
            )
        ''')
        
    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM autores')
        autores = cursor.fetchall()
        for autor in autores:
            self.tree.insert('', tk.END, values=autor)
        connection.close()

    def add_autor(self):
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        dni = self.dni_entry.get()
        nacionalidad = self.nacionalidad_entry.get()

        if nombres and apellidos and dni and nacionalidad:
            self.execute_query('''
                INSERT INTO autores (NOMBRES, APELLIDOS, DNI, NACIONALIDAD) 
                VALUES (?, ?, ?, ?)
            ''', (nombres, apellidos, dni, nacionalidad))
            messagebox.showinfo("Éxito", "Autor agregado correctamente")
            self.populate_tree()
            self.clear_form()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def edit_autor(self):
        selected_item = self.tree.selection()
        if selected_item:
            nombres = self.nombres_entry.get()
            apellidos = self.apellidos_entry.get()
            dni = self.dni_entry.get()
            nacionalidad = self.nacionalidad_entry.get()
            autor_id = self.tree.item(selected_item)['values'][0]

            if nombres and apellidos and dni and nacionalidad:
                self.execute_query('''
                    UPDATE autores SET NOMBRES=?, APELLIDOS=?, DNI=?, NACIONALIDAD=? WHERE idautor=?
                ''', (nombres, apellidos, dni, nacionalidad, autor_id))
                messagebox.showinfo("Éxito", "Autor actualizado correctamente")
                self.populate_tree()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            messagebox.showerror("Error", "Por favor, selecciona un autor para editar")

    def delete_autor(self):
        selected_item = self.tree.selection()
        if selected_item:
            autor_id = self.tree.item(selected_item)['values'][0]

            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de querer eliminar este autor?")
            if confirm:
                self.execute_query('''
                    DELETE FROM autores WHERE idautor=?
                ''', (autor_id,))
                messagebox.showinfo("Éxito", "Autor eliminado correctamente")
                self.populate_tree()
                self.clear_form()
        else:
            messagebox.showerror("Error", "Por favor, selecciona un autor para eliminar")

    def clear_form(self):
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.nacionalidad_entry.delete(0, tk.END)

    def search_autor(self):
        search_term = self.search_entry.get()

        if search_term:
            connection = sqlite3.connect('biblioteca.db')
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM autores 
                WHERE NOMBRES LIKE ? OR APELLIDOS LIKE ? OR DNI LIKE ? OR NACIONALIDAD LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            autores = cursor.fetchall()

            for row in self.tree.get_children():
                self.tree.delete(row)

            for autor in autores:
                self.tree.insert('', tk.END, values=autor)
            
            connection.close()
        else:
            self.populate_tree()

    def import_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            try:
                df = pd.read_excel(file_path)
                for index, row in df.iterrows():
                    self.execute_query('''
                        INSERT INTO autores (NOMBRES, APELLIDOS, DNI, NACIONALIDAD) 
                        VALUES (?, ?, ?, ?)
                    ''', (row['NOMBRES'], row['APELLIDOS'], row['DNI'], row['NACIONALIDAD']))
                messagebox.showinfo("Éxito", "Datos importados correctamente")
                self.populate_tree()
            except Exception as e:
                messagebox.showerror("Error", f"Error al importar datos: {e}")

    def export_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            try:
                connection = sqlite3.connect('biblioteca.db')
                df = pd.read_sql_query('SELECT * FROM autores', connection)
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Éxito", "Datos exportados correctamente")
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar datos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Autores")
    root.geometry("600x400")
    app = AutoresApp(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
