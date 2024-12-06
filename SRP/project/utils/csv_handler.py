import csv

def load_from_csv(file_path, sheet):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cell = row["Cell"]
            value = row["Value"]
            sheet.add_value(cell, value)

def save_to_csv(file_path, sheet):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Cell", "Value", "Result"])
        for cell, data in sheet.cells.items():
            writer.writerow([cell, data["value"], data["result"]])
