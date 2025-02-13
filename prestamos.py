import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class PrestamosApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = ttk.Treeview(self, columns=('idprestamo', 'idlibro', 'idusuario', 'fecha_prestamo', 'fecha_devolucion'), show='headings')
        self.tree.heading('idprestamo', text='ID')
        self.tree.heading('idlibro', text='ID Libro')
        self.tree.heading('idusuario', text='ID Usuario')
        self.tree.heading('fecha_prestamo', text='Fecha Prestamo')
        self.tree.heading('fecha_devolucion', text='Fecha Devolucion')
        self.tree.pack(expand=True, fill='both')

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)

        self.idlibro_label = ttk.Label(self.form_frame, text="ID Libro:")
        self.idlibro_label.grid(row=0, column=0)
        self.idlibro_entry = ttk.Entry(self.form_frame)
        self.idlibro_entry.grid(row=0, column=1)

        self.idusuario_label = ttk.Label(self.form_frame, text="Nombre Usuario:")
        self.idusuario_label.grid(row=1, column=0)
        self.idusuario_entry = ttk.Entry(self.form_frame)
        self.idusuario_entry.grid(row=1, column=1)

        self.fecha_prestamo_label = ttk.Label(self.form_frame, text="Fecha Prestamo (YYYY-MM-DD):")
        self.fecha_prestamo_label.grid(row=2, column=0)
        self.fecha_prestamo_entry = ttk.Entry(self.form_frame)
        self.fecha_prestamo_entry.grid(row=2, column=1)

        self.fecha_devolucion_label = ttk.Label(self.form_frame, text="Fecha Devolucion (YYYY-MM-DD):")
        self.fecha_devolucion_label.grid(row=3, column=0)
        self.fecha_devolucion_entry = ttk.Entry(self.form_frame)
        self.fecha_devolucion_entry.grid(row=3, column=1)

        self.add_button = ttk.Button(self.form_frame, text="Agregar", command=self.add_prestamo)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.edit_button = ttk.Button(self.form_frame, text="Editar", command=self.edit_prestamo)
        self.edit_button.grid(row=5, column=0, pady=10)

        self.delete_button = ttk.Button(self.form_frame, text="Eliminar", command=self.delete_prestamo)
        self.delete_button.grid(row=5, column=1, pady=10)

        self.search_label = ttk.Label(self.form_frame, text="Buscar:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = ttk.Entry(self.form_frame)
        self.search_entry.grid(row=6, column=1)

        self.search_button = ttk.Button(self.form_frame, text="Buscar", command=self.search_prestamo)
        self.search_button.grid(row=6, column=2)

        self.import_button = ttk.Button(self.form_frame, text="Importar Excel", command=self.import_excel)
        self.import_button.grid(row=7, column=0, pady=10)

        self.export_button = ttk.Button(self.form_frame, text="Exportar Excel", command=self.export_excel)
        self.export_button.grid(row=7, column=1, pady=10)

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
            CREATE TABLE IF NOT EXISTS prestamos (
                idprestamo INTEGER PRIMARY KEY AUTOINCREMENT,
                idlibro TEXT NOT NULL,
                idusuario TEXT NOT NULL,
                fecha_prestamo TEXT NOT NULL,
                fecha_devolucion TEXT
            )
        ''')

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM prestamos')
        prestamos = cursor.fetchall()
        for prestamo in prestamos:
            self.tree.insert('', tk.END, values=prestamo)
        connection.close()

    def add_prestamo(self):
        idlibro = self.idlibro_entry.get()
        idusuario = self.idusuario_entry.get()
        fecha_prestamo = self.fecha_prestamo_entry.get()
        fecha_devolucion = self.fecha_devolucion_entry.get()

        if idlibro and idusuario and fecha_prestamo:
            self.execute_query('''
                INSERT INTO prestamos (idlibro, idusuario, fecha_prestamo, fecha_devolucion) 
                VALUES (?, ?, ?, ?)
            ''', (idlibro, idusuario, fecha_prestamo, fecha_devolucion))
            messagebox.showinfo("Éxito", "Préstamo agregado correctamente")
            self.populate_tree()
            self.clear_form()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def edit_prestamo(self):
        selected_item = self.tree.selection()
        if selected_item:
            idlibro = self.idlibro_entry.get()
            idusuario = self.idusuario_entry.get()
            fecha_prestamo = self.fecha_prestamo_entry.get()
            fecha_devolucion = self.fecha_devolucion_entry.get()
            prestamo_id = self.tree.item(selected_item)['values'][0]

            if idlibro and idusuario and fecha_prestamo:
                self.execute_query('''
                    UPDATE prestamos SET idlibro=?, idusuario=?, fecha_prestamo=?, fecha_devolucion=? 
                    WHERE idprestamo=?
                ''', (idlibro, idusuario, fecha_prestamo, fecha_devolucion, prestamo_id))
                messagebox.showinfo("Éxito", "Préstamo actualizado correctamente")
                self.populate_tree()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            messagebox.showerror("Error", "Por favor, selecciona un préstamo para editar")

    def delete_prestamo(self):
        selected_item = self.tree.selection()
        if selected_item:
            prestamo_id = self.tree.item(selected_item)['values'][0]

            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de querer eliminar este préstamo?")
            if confirm:
                self.execute_query('''
                    DELETE FROM prestamos WHERE idprestamo=?
                ''', (prestamo_id,))
                messagebox.showinfo("Éxito", "Préstamo eliminado correctamente")
                self.populate_tree()
                self.clear_form()
        else:
            messagebox.showerror("Error", "Por favor, selecciona un préstamo para eliminar")

    def clear_form(self):
        self.idlibro_entry.delete(0, tk.END)
        self.idusuario_entry.delete(0, tk.END)
        self.fecha_prestamo_entry.delete(0, tk.END)
        self.fecha_devolucion_entry.delete(0, tk.END)

    def search_prestamo(self):
        search_term = self.search_entry.get()

        if search_term:
            connection = sqlite3.connect('biblioteca.db')
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM prestamos 
                WHERE idlibro LIKE ? OR idusuario LIKE ? OR fecha_prestamo LIKE ? OR fecha_devolucion LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            prestamos = cursor.fetchall()

            for row in self.tree.get_children():
                self.tree.delete(row)

            for prestamo in prestamos:
                self.tree.insert('', tk.END, values=prestamo)
            
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
                        INSERT INTO prestamos (idlibro, idusuario, fecha_prestamo, fecha_devolucion) 
                        VALUES (?, ?, ?, ?)
                    ''', (row['idlibro'], row['idusuario'], row['fecha_prestamo'], row['fecha_devolucion']))
                messagebox.showinfo("Éxito", "Datos importados correctamente")
                self.populate_tree()
            except Exception as e:
                messagebox.showerror("Error", f"Error al importar datos: {e}")

    def export_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            try:
                connection = sqlite3.connect('biblioteca.db')
                df = pd.read_sql_query('SELECT * FROM prestamos', connection)
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Éxito", "Datos exportados correctamente")
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar datos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Préstamos")
    root.geometry("600x400")
    app = PrestamosApp(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
