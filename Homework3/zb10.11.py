class FoodItem:
    def __init__(self, name="None", fat='0', carbs='0', protein='0'):
        self.name=  name
        self.fat = float(fat)
        self.carbs = float(carbs)
        self.protein = float(protein)

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print("Nutritional information per serving of {}:".format(self.name))
        print("   Fat: {:.2f} g".format(self.fat))
        print("   Carbohydrates: {:.2f} g".format(self.carbs))
        print("   Protein: {:.2f} g".format(self.protein))

if __name__ == '__main__':
    food_item1 = FoodItem()

    item_name = input()
    amount_fat = input()
    amount_carbs = input()
    amount_protein = input()

    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_serving = float(input())

    food_item1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_serving, food_item1.get_calories(num_serving)))

    print()

    food_item2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_serving, food_item2.get_calories(num_serving)))
