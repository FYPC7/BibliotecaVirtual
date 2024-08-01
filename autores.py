import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class AutoresApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
