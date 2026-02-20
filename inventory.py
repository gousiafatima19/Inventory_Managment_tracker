products = [{
    'id': 1,
    'name': 'Laptop',
    'category': 'Electronics',
    'quantity': 10,
    'price': 999.99,
    'supplier': 'TechSupplier Inc.',
    'reorder_level': 5
    },{
    'id': 2,
    'name': 'Smartphone',
    'category': 'Electronics',
    'quantity': 20,
    'price': 499.99,
    'supplier': 'MobileWorld Ltd.',
    'reorder_level': 10
    },{
    'id': 3,
    'name': 'Tablet',
    'category': 'Electronics',
    'quantity': 15,
    'price': 299.99,
    'supplier': 'GadgetHub Inc.',
    'reorder_level': 5
    },{
    'id': 4,
    'name': 'Headphones',
    'category': 'Electronics',
    'quantity': 25,
    'price': 199.99,
    'supplier': 'AudioTech Co.',
    'reorder_level': 5
    },{
    'id': 5,
    'name': 'Keyboard',
    'category': 'Electronics',
    'quantity': 30,
    'price': 79.99,
    'supplier': 'TechGear Ltd.',
    'reorder_level': 5
    }]
def add_product():
    print("\nAdd New Product")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    supplier = input("Enter supplier name: ")
    reorder_level = int(input("Enter reorder level: "))
    new_id = max([p['id'] for p in products]) + 1 if products else 1
    new_product = {
        'id': new_id,
        'name': name,
        'category': category,
        'quantity': quantity,
        'price': price,
        'supplier': supplier,
        'reorder_level': reorder_level
    }
    products.append(new_product)
    print(f"Product '{name}' added successfully with ID {new_id}.")
def update_stock():
    print("\nUpdate Product Stock")
    product_id = int(input("Enter product ID to update: "))
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        new_quantity = int(input(f"Enter new quantity for '{product['name']}': "))
        product['quantity'] = new_quantity
        print(f"Stock for '{product['name']}' updated to {new_quantity}.")
    else:
        print("Product not found.")

def record_sale():
    print("\nRecord a Sale")
    product_id = int(input("Enter product ID sold: "))
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        quantity_sold = int(input(f"Enter quantity sold for '{product['name']}': "))
        if quantity_sold <= product['quantity']:
            product['quantity'] -= quantity_sold
            print(f"Sale recorded. Remaining stock for '{product['name']}': {product['quantity']}.")
        else:
            print(f"Insufficient stock. Only {product['quantity']} units available.")
    else:
        print("Product not found.")
def delete_product():
    print("\nDelete a Product")
    product_id = int(input("Enter product ID to delete: "))
    global products
    products = [p for p in products if p['id'] != product_id]
    print(f"Product with ID {product_id} deleted successfully.")
def view_product_details():
    print("\nView Product Details")
    product_id = int(input("Enter product ID to view details: "))
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        print(f"\nProduct ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Supplier: {product['supplier']}")
        print(f"Reorder Level: {product['reorder_level']}")
    else:
        print("Product not found.")
def generate_report():
    print("\nInventory Report")
    print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Quantity':<10} {'Price':<10} {'Supplier':<20}")
    print("-"*80)
    for product in products:
        print(f"{product['id']:<5} {product['name']:<20} {product['category']:<15} {product['quantity']:<10} ${product['price']:<10.2f} {product['supplier']:<20}")
def check_reorder_alerts():
    print("\nReorder Alerts")
    alerts = [p for p in products if p['quantity'] <= p['reorder_level']]
    if alerts:
        print(f"{'ID':<5} {'Name':<20} {'Quantity':<10} {'Reorder Level':<15}")
        print("-"*50)
        for product in alerts:
            print(f"{product['id']:<5} {product['name']:<20} {product['quantity']:<10} {product['reorder_level']:<15}")
    else:
        print("No products need reordering.")
