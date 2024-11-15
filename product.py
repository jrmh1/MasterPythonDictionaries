
product_object1 = {
    "name": "Laptop",
    "category": "Electronics",
    "price": 30000.00,
    "stock": 50,
    "supplier_email": "supplier1@gmail.com"
}


product_object2 = {
    "name": "Desk Chair",
    "category": "Furniture",
    "price": 3000.00,
    "stock": 200,
    "supplier_email": "supplier2@gmail.com"
}


product_object3 = {
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 2500.00,
    "stock": 150,
    "supplier_email": "supplier3@gmail.com"
}


product_object4 = {
    "name": "Notebook",
    "category": "Stationery",
    "price": 100.00,
    "stock": 0,
    "supplier_email": "supplier4@gmail.com"
}


product_object5 = {
    "name": "Running Shoes",
    "category": "Apparel",
    "price": 4500.00,
    "stock": 100,
    "supplier_email": "supplier5@gmail.com"
}


products = [product_object1, product_object2, product_object3, product_object4, product_object5]


for product in products:
    print(f"Product: {product['name']}, Category: {product['category']}, Price: ₱{product['price']}, Stock: {product['stock']}, Supplier Email: {product['supplier_email']}")
