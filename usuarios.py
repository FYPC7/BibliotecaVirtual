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
