import sqlite3
import pandas as pd

def create_tables():
    try:
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()

        # Crear tabla autores
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            idautor INTEGER PRIMARY KEY,
            NOMBRES TEXT NOT NULL,
            APELLIDOS TEXT NOT NULL,
            DNI TEXT NOT NULL,
            NACIONALIDAD TEXT NOT NULL
        )
        ''')

        # Crear tabla categorias
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            idcategoria TEXT PRIMARY KEY,
            NOMBRE TEXT NOT NULL
        )
        ''')

        # Crear tabla libros
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            idlibro INTEGER PRIMARY KEY,
            TITULO TEXT NOT NULL,
            idcategoria TEXT,
            AUTOR TEXT NOT NULL,
            ISBN TEXT,
            FOREIGN KEY (idcategoria) REFERENCES categorias(idcategoria)
        )
        ''')

        # Crear tabla libros_autores
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros_autores (
            idlibro INTEGER,
            idautor INTEGER,
            PRIMARY KEY (idlibro, idautor),
            FOREIGN KEY (idlibro) REFERENCES libros(idlibro),
            FOREIGN KEY (idautor) REFERENCES autores(idautor)
        )
        ''')

        # Crear tabla prestamos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS prestamos (
            idprestamo INTEGER PRIMARY KEY AUTOINCREMENT,
            idlibro INTEGER,
            idusuario INTEGER,
            fecha_prestamo TEXT NOT NULL,
            fecha_devolucion TEXT,
            FOREIGN KEY (idlibro) REFERENCES libros(idlibro),
            FOREIGN KEY (idusuario) REFERENCES usuarios(idusuario)
        )
        ''')

        # Crear tabla roles
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            idrol INTEGER PRIMARY KEY,
            NOMBRE TEXT NOT NULL
        )
        ''')

        # Crear tabla usuarios
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            idusuario INTEGER PRIMARY KEY,
            NOMBRES TEXT NOT NULL,
            APELLIDOS TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            idrol INTEGER,
            FOREIGN KEY (idrol) REFERENCES roles(idrol)
        )
        ''')

        connection.commit()
    except sqlite3.Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        connection.close()

def add_column_to_table():
    try:
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()

        # Verificar si la columna ISBN ya existe en la tabla libros
        cursor.execute('PRAGMA table_info(libros)')
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'ISBN' not in columns:
            cursor.execute('''
                ALTER TABLE libros
                ADD COLUMN ISBN TEXT
            ''')
            connection.commit()
            print("Columna ISBN agregada correctamente.")
        else:
            print("La columna ISBN ya existe.")
    except sqlite3.Error as e:
        print(f"Error al agregar columna ISBN: {e}")
    finally:
        connection.close()
