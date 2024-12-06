import tkinter as tk
from core.sheet import Sheet
from ui.app import App

if __name__ == "__main__":
    root = tk.Tk()
    sheet = Sheet()
    app = App(root, sheet)
    root.mainloop()
