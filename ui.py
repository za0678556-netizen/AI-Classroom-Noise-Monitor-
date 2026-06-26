# ui.py
import tkinter as tk
from tkinter import ttk

class NoiseUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Classroom Noise Monitor")
        self.root.geometry("400x300")
        
        self.db_label = ttk.Label(root, text="dB: 0.0", font=("Arial", 24))
        self.db_label.pack(pady=20)
        
        self.status_label = ttk.Label(root, text="Status: QUIET", font=("Arial", 18))
        self.status_label.pack(pady=10)
        
        self.message_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=350)
        self.message_label.pack(pady=10)

    def update_display(self, db_level, status, message, color):
        self.db_label.config(text=f"dB: {db_level}")
        self.status_label.config(text=f"Status: {status}")
        self.message_label.config(text=message)
        self.root.config(bg=color)
        self.status_label.config(background=color)
