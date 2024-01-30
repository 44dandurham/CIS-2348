class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def set_item(self, name, price, quantity):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def get_total_price(self):
        return self.item_price * self.item_quantity

    def display_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.get_total_price()}")

def prompt_for_item_info():
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    return name, price, quantity

def main():
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    
    print('Item 1')
    name, price, quantity = prompt_for_item_info()
    item1.set_item(name, price, quantity)
    
    print('\nItem 2')
    name, price, quantity = prompt_for_item_info()
    item2.set_item(name, price, quantity)
    
    print('\nTOTAL COST')
    item1.display_item_cost()
    item2.display_item_cost()
    total_cost = item1.get_total_price() + item2.get_total_price()
    print(f"\nTotal: ${total_cost}")

if __name__ == "__main__":
    main()
