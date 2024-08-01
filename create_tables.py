import sqlite3
import pandas as pd

# se crear todas las tablas
def create_tables():
    try:
        connection = sqlite3.connect('biblioteca.db')
        cursor = connection.cursor()
