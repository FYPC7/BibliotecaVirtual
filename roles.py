import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class RolesApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = ttk.Treeview(self, columns=('idrol', 'NOMBRE'), show='headings')
        self.tree.heading('idrol', text='ID')
        self.tree.heading('NOMBRE', text='Nombre')
        self.tree.pack(expand=True, fill='both')

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.nombre_label = ttk.Label(self.form_frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = ttk.Entry(self.form_frame)
        self.nombre_entry.grid(row=0, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_rol)
        self.add_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_rol)
        self.edit_button.grid(row=2, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_rol)
        self.delete_button.grid(row=2, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=3, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=3, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_rol)
        self.search_button.grid(row=3, column=2)

        self.populate_tree()

    def execute_query(self, query, parameters=()):
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        connection.close()

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM roles')
        roles = cursor.fetchall()
        for rol in roles:
            self.tree.insert('', tk.END, values=rol)
        connection.close()

    def add_rol(self):
        nombre = self.nombre_entry.get()

        if nombre:
            self.execute_query('''
                INSERT INTO roles (NOMBRE) 
                VALUES (?)
            ''', (nombre,))
            messagebox.showinfo("Éxito", "Rol agregado correctamente")
            self.populate_tree()
        else:
            messagebox.showerror("Error", "El campo nombre es obligatorio")
            
    def edit_rol(self):
        selected_item = self.tree.selection()
        if selected_item:
            nombre = self.nombre_entry.get()
            rol_id = self.tree.item(selected_item)['values'][0]

            if nombre:
                self.execute_query('''
                    UPDATE roles SET NOMBRE=? WHERE idrol=?
                ''', (nombre, rol_id))
                messagebox.showinfo("Éxito", "Rol actualizado correctamente")
                self.populate_tree()
                self.clear_form()
            else:
                messagebox.showerror("Error", "El campo nombre es obligatorio")
        else:
            messagebox.showerror("Error", "Por favor, selecciona un rol para editar")

    def delete_rol(self):
        selected_item = self.tree.selection()
        if selected_item:
            rol_id = self.tree.item(selected_item)['values'][0]

            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de querer eliminar este rol?")
            if confirm:
                self.execute_query('''
                    DELETE FROM roles WHERE idrol=?
                ''', (rol_id,))
                messagebox.showinfo("Éxito", "Rol eliminado correctamente")
                self.populate_tree()
                self.clear_form()
        else:
            messagebox.showerror("Error", "Por favor, selecciona un rol para eliminar")

    def clear_form(self):
        self.nombre_entry.delete(0, tk.END)

    def search_rol(self):
        search_term = self.search_entry.get()

        if search_term:
            connection = sqlite3.connect('biblioteca.db')
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM roles 
                WHERE NOMBRE LIKE ?
            ''', (f'%{search_term}%',))
            roles = cursor.fetchall()

            for row in self.tree.get_children():
                self.tree.delete(row)

            for rol in roles:
                self.tree.insert('', tk.END, values=rol)
            
            connection.close()
        else:
            self.populate_tree()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Roles")
    root.geometry("400x400")
    app = RolesApp(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
