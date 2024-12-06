import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils.csv_handler import load_from_csv, save_to_csv
from ui.dialogs import add_cell_dialog

class App:
    def __init__(self, root, sheet):
        self.sheet = sheet
        self.root = root
        self.root.title("Spreadsheet Parser")

        self.table = ttk.Treeview(root, columns=("Cell", "Value", "Result"), show="headings")
        self.table.heading("Cell", text="Cell")
        self.table.heading("Value", text="Value")
        self.table.heading("Result", text="Result")
        self.table.pack(expand=True, fill="both")

        self.load_button = ttk.Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(side="left", padx=10)

        self.save_button = ttk.Button(root, text="Save CSV", command=self.save_csv)
        self.save_button.pack(side="left", padx=10)

        self.add_button = ttk.Button(root, text="Add Cell", command=lambda: add_cell_dialog(self.sheet, self.refresh_table))
        self.add_button.pack(side="left", padx=10)

        self.delete_button = ttk.Button(root, text="Delete Cell", command=self.delete_cell)
        self.delete_button.pack(side="left", padx=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            load_from_csv(file_path, self.sheet)
            self.refresh_table()

    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            save_to_csv(file_path, self.sheet)
            messagebox.showinfo("Save CSV", "File saved successfully!")

    def refresh_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        for cell, data in self.sheet.cells.items():
            self.table.insert("", "end", values=(cell, data["value"], data["result"]))

    def delete_cell(self):
        selected_item = self.table.selection()
        if selected_item:
            cell = self.table.item(selected_item)["values"][0]
            self.sheet.delete_value(cell)
            self.refresh_table()
        else:
            messagebox.showwarning("Selection Error", "No cell selected!")
