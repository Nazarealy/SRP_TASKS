class Sheet:
    def __init__(self):
        self.cells = {}

    def add_value(self, cell, value):
        self.cells[cell] = {"value": value, "result": None}
        self.update_results()

    def get_value(self, cell):
        if cell not in self.cells:
            return {"value": None, "result": "ERROR"}
        return self.cells[cell]

    def edit_value(self, cell, value):
        if cell in self.cells:
            self.cells[cell]["value"] = value
            self.update_results()
        else:
            raise ValueError(f"Cell {cell} does not exist!")

    def delete_value(self, cell):
        if cell in self.cells:
            del self.cells[cell]
            self.update_results()

    def update_results(self):
        for cell in self.cells:
            value = self.cells[cell]["value"]
            if value.startswith("="):
                try:
                    formula = value[1:]
                    formula_with_values = formula
                    for ref_cell in self.cells:
                        formula_with_values = formula_with_values.replace(
                            ref_cell, str(self.cells[ref_cell].get("result", 0))
                        )
                    self.cells[cell]["result"] = eval(formula_with_values)
                except Exception:
                    self.cells[cell]["result"] = "ERROR"
            else:
                try:
                    self.cells[cell]["result"] = int(value) if value.isdigit() else value
                except ValueError:
                    self.cells[cell]["result"] = "ERROR"
