# ------------------------------------------
# Final Project Part 1
# Name: Daniel Durham
# PISD: 1851947
# ------------------------------------------
import csv
from datetime import datetime

# Create an empty dictionary to store product details.
products = {}
# List of filenames expected to be processed.
file_names = [
    'ManufacturerList.csv',
    'PriceList.csv',
    'ServiceDatesList.csv'
]
product_ids = []
# Capture today's date to compare with service dates.
current_date = datetime.now()
year, month, day = current_date.year, current_date.month, current_date.day

# Process each file in the list to gather product information.
for file_name in file_names:
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        
        for row in reader:
            # The first element in each row is considered the product ID.
            prod_id = row[0].strip()

            if prod_id not in product_ids:
                product_ids.append(prod_id)

            if file_name == file_names[0]:
                # Extract manufacturer details, item type, and condition status.
                products[prod_id] = {
                    'manufacturer': row[1].strip(),
                    'type': row[2].strip(),
                    'condition': row[3].strip()
                }

            elif file_name == file_names[1]:
                # Update product dictionary with pricing information.
                products[prod_id]['price'] = int(row[1])

            elif file_name == file_names[2]:
                # Update product dictionary with service date.
                products[prod_id]['service_date'] = row[1]

product_ids.sort()

# Collect unique manufacturer names and product types, and identify damaged items.
manufacturers, types, damaged_products = [], [], []

for prod_id in product_ids:
    if products[prod_id]['manufacturer'] not in manufacturers:
        manufacturers.append(products[prod_id]['manufacturer'])

    if products[prod_id]['type'] not in types:
        types.append(products[prod_id]['type'])

    if products[prod_id]['condition'] == 'damaged':
        damaged_products.append(prod_id)

manufacturers.sort()
types.sort()

# Generate a full inventory report.
with open('FullInventory.csv', 'w', newline='') as full_inventory:
    writer = csv.writer(full_inventory)

    for mfr in manufacturers:
        for prod_id in product_ids:
            if products[prod_id]['manufacturer'] == mfr:
                data = [
                    prod_id,
                    products[prod_id]['manufacturer'],
                    products[prod_id]['type'],
                    products[prod_id]['price'],
                    products[prod_id]['service_date'],
                    products[prod_id]['condition']
                ]
                writer.writerow(data)

# Generate inventory reports by item type.
for type in types:
    with open(f'{type.capitalize()}Inventory.csv', 'w', newline='') as type_file:
        writer = csv.writer(type_file)

        for prod_id in product_ids:
            if products[prod_id]['type'] == type:
                data = [
                    prod_id,
                    products[prod_id]['manufacturer'],
                    products[prod_id]['price'],
                    products[prod_id]['service_date'],
                    products[prod_id]['condition']
                ]
                writer.writerow(data)

# Generate a report for items past service date.
with open('PastServiceDateInventory.csv', 'w', newline='') as overdue_services:
    writer = csv.writer(overdue_services)

    #this list will contain the ID's of products that are overdue for services
    overdue_services_list = []

    for prod_id in product_ids:
        service_date = datetime.strptime(products[prod_id]['service_date'], '%m/%d/%Y')
        if service_date < current_date:
            data = [
                prod_id,
                products[prod_id]['manufacturer'],
                products[prod_id]['type'],
                products[prod_id]['price'],
                products[prod_id]['service_date'],
                products[prod_id]['condition']
            ]
            writer.writerow(data)

# Generate a report for damaged items, sorted by price in descending order.
with open('DamagedInventory.csv', 'w', newline='') as damaged_report:
    writer = csv.writer(damaged_report)
    damaged_products.sort(key=lambda id: products[id]['price'], reverse=True)

    for prod_id in damaged_products:
        data = [
            prod_id,
            products[prod_id]['manufacturer'],
            products[prod_id]['type'],
            products[prod_id]['price'],
            products[prod_id]['service_date']
        ]
        writer.writerow(data)
