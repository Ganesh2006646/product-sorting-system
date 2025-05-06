import pandas as pd

# Converts the product dictionary into a Pandas DataFrame for easy data handling.
def get_products_as_df(products):
    return pd.DataFrame.from_dict(products, orient="index")

# Sort products by a specified entry 
def sort_products(df, by="price", ascending=True):# on based on rating or price
    if by in df.columns:
        return df.sort_values(by=by, ascending=ascending)# based on asending or decending
    else:
        print("Invalid sorting field.")
        return df

# Filter products by a price range and print the products in between the range 
def filter_price_range(df, min_price=0, max_price=float("inf")):
    return df[(df["price"] >= min_price) & (df["price"] <= max_price)]

# Filter products by category
def filter_category(df, category=""):
    return df[df["category"].str.lower() == category.lower()]
