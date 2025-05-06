import json  # Import JSON module to handle file reading and writing products from tha file

# Function to read products from a JSON file
def read_products_from_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Function to write products to a JSON file
def write_products_to_file(file_name, products):
    with open(file_name, 'w') as file:
        json.dump(products, file, indent=4)

