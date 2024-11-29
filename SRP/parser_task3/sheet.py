import csv

class Sheet:
    def __init__(self):
        self.cells = {}  # Зберігає значення та формули осередків

    def add_value(self, cell, value):
        """Додає значення або формулу до осередка."""
        self.cells[cell] = {"value": value, "result": None}
        self.update_results()

    def get_value(self, cell):
        """Отримує значення та результат для конкретного осередка."""
        if cell not in self.cells:
            return {"value": None, "result": "ERROR"}
        return self.cells[cell]

    def edit_value(self, cell, value):
        """Редагує значення або формулу осередка."""
        if cell in self.cells:
            self.cells[cell]["value"] = value
            self.update_results()
        else:
            raise ValueError(f"Cell {cell} does not exist!")

    def delete_value(self, cell):
        """Видаляє осередок із таблиці."""
        if cell in self.cells:
            del self.cells[cell]
            self.update_results()

    def update_results(self):
        """Оновлює результати всіх осередків."""
        for cell in self.cells:
            value = self.cells[cell]["value"]
            if value.startswith("="):
                try:
                    formula = value[1:]  # Видаляємо знак '='
                    # Підставляємо значення змінних у формулу
                    formula_with_values = formula
                    for ref_cell in self.cells:
                        formula_with_values = formula_with_values.replace(
                            ref_cell, str(self.cells[ref_cell].get("result", 0))
                        )
                    # Обчислюємо формулу
                    self.cells[cell]["result"] = eval(formula_with_values)
                except Exception:
                    self.cells[cell]["result"] = "ERROR"
            else:
                try:
                    self.cells[cell]["result"] = int(value) if value.isdigit() else value
                except ValueError:
                    self.cells[cell]["result"] = "ERROR"

    def load_from_csv(self, file_path):
        """Завантажує дані з CSV файлу."""
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cell = row["Cell"]
                value = row["Value"]
                self.add_value(cell, value)

    def print_sheet(self):
        """Виводить усі осередки з їх значеннями та результатами."""
        for cell, data in self.cells.items():
            print(f"{cell}: {data}")

# --- Основна програма ---
def main():
    sheet = Sheet()
    file_path = "test_sheet.csv"  # Назва твоєї таблиці
    sheet.load_from_csv(file_path)

    # Демонстрація роботи
    print("Таблиця після завантаження:")
    sheet.print_sheet()

    # Додаємо нові значення
    sheet.add_value("A11", "=A1+A9")
    print("\nПісля додавання A11 = A1 + A9:")
    sheet.print_sheet()

    # Редагуємо значення A1
    sheet.edit_value("A1", "50")
    print("\nПісля редагування A1:")
    sheet.print_sheet()

    # Видаляємо A3
    sheet.delete_value("A3")
    print("\nПісля видалення A3:")
    sheet.print_sheet()

if __name__ == "__main__":
    main()
