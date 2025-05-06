import json
from product_manager import get_products_as_df, sort_products, filter_price_range, filter_category

# Load products from JSON  text file
def load_products(file="products.json"):
    with open(file, "r") as f:
        return json.load(f)

# Main loop to apply multiple sort and filter actions in one session
def filter_and_sort(products):
    df = get_products_as_df(products)  # we will start with full data
    
    while True:#these are the sorting meathods 
        print("Choose an option:")
        print("1. Sort by price or rating")
        print("2. Filter by price range")
        print("3. Filter by category")
        print("4. Show current data")
        print("5. Reset to original data")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":#we will sort the products based on rating and price
            by = input("Sort by 'price' or 'rating': ")
            order = input("Enter 'a' for ascending or 'd' for descending: ")#in asending order or decending order
            df = sort_products(df, by=by, ascending=(order == "a"))
            print(df)

        elif choice == "2":
            min_price = int(input("Enter minimum price: "))#we can sort by a range of price 
            max_price = int(input("Enter maximum price: "))
            df = filter_price_range(df, min_price, max_price)
            print(df)

        elif choice == "3":
            category = input("Enter category to filter by: ")#we can sort by a category
            df = filter_category(df, category)
            print(df)

        elif choice == "4":
            print("Current data", df)#to complete the loop and print our sorted data

        elif choice == "5":
            df = get_products_as_df(products)  # Reset to original data
            print("Data has been reset to original.")

        elif choice == "6":# exit from our program
            print("Exiting program.")
            break

        else:# for invaid inputs
            print("Invalid choice. Please select a valid option.")

# Run the program
products = load_products()
filter_and_sort(products)
