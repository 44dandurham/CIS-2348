# -----------------------------------------
# Final Project Part 2
# Name: Daniel Durham
# ID: 1851947
# -----------------------------------------

# Importing data structures from the inventory management script
from FinalProjectPart1 import (
    products as all_items,
    product_ids as valid_ids,
    types as categories,
    manufacturers as brands,
    damaged_products,
    overdue_services_list
)
# Combining damaged and overdue service items into one list of excluded items
excluded_items = damaged_products + overdue_services_list 


# Exclude damaged and service-past items from consideration
for excluded_id in excluded_items:
    if excluded_id in valid_ids:
        valid_ids.remove(excluded_id)

# Function to process user queries
def process_query():
    query = input('Enter the item and brand you are searching for (or "q" to exit): ').lower()
    
    while query != 'q':
        found_brand = ''
        found_type = ''
        best_match = None
        best_price = 0

        search_terms = query.split()

        # Identify the desired brand and item type from the query
        for term in search_terms:
            if term in brands:
                found_brand = term
            elif term in categories:
                found_type = term

        if not found_brand or not found_type:
            print("No such item in inventory.")
        else:
            # Find the best matching item in inventory
            for item_id in valid_ids:
                item = all_items[item_id]
                if item['manufacturer'] == found_brand and item['type'] == found_type and item['price'] > best_price:
                    best_match = item_id
                    best_price = item['price']

            if best_match:
                print(f"Suggested item: {best_match}, {all_items[best_match]['manufacturer']}, {all_items[best_match]['type']}, ${all_items[best_match]['price']}")
                # Suggest alternative items
                suggest_alternatives(found_type, found_brand)
            else:
                print("No such item in inventory.")

        query = input('Enter the item and brand you are searching for (or "q" to exit): ').lower()

def suggest_alternatives(item_type, exclude_brand):
    alternatives = [id for id in valid_ids if all_items[id]['type'] == item_type and all_items[id]['manufacturer'] != exclude_brand]
    if alternatives:
        print("Consider also:")
        for alt in alternatives:
            print(f"{alt}, {all_items[alt]['manufacturer']}, {all_items[alt]['type']}, ${all_items[alt]['price']}")

# Execute the query processing function
if __name__ == '__main__':
    process_query()
