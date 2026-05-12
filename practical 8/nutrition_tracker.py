
class food_item:
    """
    A class to represent a food item with nutrition info.
    """
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def daily_total(food_list):
    """
    Input: food_list, a list of food_item objects
    Returns: None, prints total nutrition and warnings
    """
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_cal = total_cal + food.calories
        total_pro = total_pro + food.protein
        total_carbs = total_carbs + food.carbs
        total_fat = total_fat + food.fat

    print("Total calories:", total_cal)
    print("Total protein:", total_pro, "g")
    print("Total carbohydrates:", total_carbs, "g")
    print("Total fat:", total_fat, "g")

    if total_cal > 2500:
        print("Warning: Over 2500 calories!")
    if total_fat > 90:
        print("Warning: Over 90g fat!")

# Example usage
apple = food_item("apple", 60, 0.3, 15, 0.5)
bread = food_item("bread", 265, 9, 49, 3.2)
milk = food_item("milk", 150, 8, 12, 8)

today_food = [apple, bread, milk]
daily_total(today_food)