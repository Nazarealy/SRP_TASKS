import tkinter as tk
from tkinter import messagebox

def add_cell_dialog(sheet, refresh_table):
    def save_cell():
        cell = cell_entry.get()
        value = value_entry.get()
        if cell and value:
            sheet.add_value(cell, value)
            refresh_table()
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Both fields must be filled!")

    add_window = tk.Toplevel()
    add_window.title("Add Cell")
    tk.Label(add_window, text="Cell:").pack(pady=5)
    cell_entry = tk.Entry(add_window)
    cell_entry.pack(pady=5)
    tk.Label(add_window, text="Value:").pack(pady=5)
    value_entry = tk.Entry(add_window)
    value_entry.pack(pady=5)
    tk.Button(add_window, text="Save", command=save_cell).pack(pady=10)
