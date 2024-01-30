class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none" 

    def set_item(self, name, price, quantity, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description 
        

    def get_total_price(self):
        return self.item_price * self.item_quantity

    def display_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.get_total_price()}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart: 
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items: 
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")
            
    def modify_item(self, item_to_purchase):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_to_purchase.item_name:
                self.cart_items[i].item_quantity = item_to_purchase.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.get_total_price()
        return total_cost
    
    def print_total(self): 
        print(f"OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            print()
            print(f"Total: ${self.get_cost_of_cart()}")
        else:
            for item in self.cart_items:
                item.display_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")
            
        
    def print_description(self):
        print(f"OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
       
    


def prompt_for_item_info():
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    description = input("Enter the item description:\n")
    return name, price, quantity, description

def add_item_to_cart(cart):
    print("\nADD ITEM TO CART")
    name = input("Enter the item name:\n")
    description = input("Enter the item description:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    item = ItemToPurchase()
    item.set_item(name, price, quantity, description)
    cart.add_item(item)

def remove_item_from_cart(cart):
    print("\nREMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove:\n")
    cart.remove_item(item_name)

def modify_item_in_cart(cart):
    print("\nCHANGE ITEM QUANTITY")
    name = input("Enter the item name:\n")
    quantity = int(input("Enter the new quantity:\n"))
    item = ItemToPurchase()
    item.set_item(name, 0, quantity)
    cart.modify_item(item)


def print_menu(shopping_cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    print(menu)
    while True: 
        choice = input("Choose an option:\n")

        if choice == 'q':
            break
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'i':
            shopping_cart.print_description()
        elif choice == 'a':
            add_item_to_cart(shopping_cart)
        elif choice == 'r':
            remove_item_from_cart(shopping_cart)
        elif choice == 'c':
            modify_item_in_cart(shopping_cart)
        else:
            continue 

        print(menu)

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
