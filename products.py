# Placeholder for product management features
products = []

def add_product(name, price):
    product = {
        "name": name,
        "price": price
    }
    products.append(product)

def list_products():
    if not products:
        print("No products found.")
    else:
        print("Product List:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product['name']} - ${product['price']}")
