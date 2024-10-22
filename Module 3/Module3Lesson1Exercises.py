"""
1. E-Commerce Product Catalog Management

Develop a program to manage a product catalog for an e-commerce platform.
The program should facilitate adding new product categories, adding products to existing categories, displaying all available categories,
and searching for products within the catalog.

1. Initialize a dictionary to represent the product catalog
2. Implement functions for:
    Adding a new product category
    Adding a product to an existing category
    Displaying all categories & their respective products
    Searching for a product across all categories (case sensitive)
3. Use exception handling to address potentional errors, such as adding product to non-existent categories
4. Implement case-insensitive search functionality for product queries.

HINTS:
Start with a pre-populated dictionary for ease of testing
Utilize string methods like lower() for case-insensitive comparisons
In the search function, iterate through all categories to find the product
Implement try and except blocks to gracefully handle situations where a specified category does not exist in the catalog
"""

def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category: '{category}' added.")
    else:
        print(f"Category '{category}' already exists")

def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product '{product}' added to category '{category}'.")
        else:
            print(f"Product '{product}' already exists in category '{category}'.")
    except KeyError:
        print(f"Category '{category}' does not exist.")

def display_categories(catalog):
    for category, products in catalog.items():
        print(f"{category}: {', ' .join(products)}")

def search_product(catalog, product):
    found = False
    for category, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            print(f"Product '{product}' found in '{category}' .")
            found = True
            break
    if not found:
        print(f"Product '{product}' not found. ")

catalog = {
    "Electronics": ["Laptop", "Smartphone"],
    "Books": ["Fiction", "Non-Fiction"]
}

add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Tablet")
display_categories(catalog)
search_product(catalog, "laptop")
print(catalog)