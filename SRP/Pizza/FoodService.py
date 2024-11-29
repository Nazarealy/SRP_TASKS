class Food:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def describe(self):
        return f"Dish: {self.name}\nIngredients: {', '.join(self.ingredients)}"


class Pizza(Food):
    def __init__(self, name, ingredients):
        super().__init__(name, ingredients)


class FoodService:
    def create_food(self, food_type):
        raise NotImplementedError("This method should be overridden by subclasses")


class PizzaFoodService(FoodService):
    def create_food(self, food_type):
        if food_type == "New York Pizza":
            return Pizza("New York Pizza", ["Tomato Sauce", "Cheese", "Pepperoni", "Olives"])
        elif food_type == "Deluxe Pizza":
            return Pizza("Deluxe Pizza", ["Tomato Sauce", "Cheese", "Mushrooms", "Olives", "Peppers", "Onions"])
        elif food_type == "Vegan Pizza":
            return Pizza("Vegan Pizza", ["Tomato Sauce", "Cheese", "Mushrooms", "Peppers", "Olives", "Spinach"])
        elif food_type == "Margarita":
            return Pizza("Margarita", ["Tomato Sauce", "Cheese", "Basil", "Olives"])
        elif food_type == "Diablo":
            return Pizza("Diablo", ["Tomato Sauce", "Cheese", "Spicy Sausage", "Jalapenos", "Peppers"])
        else:
            return None


# Тестування
pizza_service = PizzaFoodService()

pizza1 = pizza_service.create_food("New York Pizza")
if pizza1:
    print(pizza1.describe())

pizza2 = pizza_service.create_food("Vegan Pizza")
if pizza2:
    print(pizza2.describe())

pizza3 = pizza_service.create_food("Margarita")
if pizza3:
    print(pizza3.describe())

pizza4 = pizza_service.create_food("Nonexistent Pizza")
if pizza4:
    print(pizza4.describe())
else:
    print("Pizza type not found.")
