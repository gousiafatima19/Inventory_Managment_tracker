# add_supplier()

# get_supplier_products()
suppliers = [{
    'name': 'TechSupplier Inc.',
    'products': ['Laptop', 'Monitor', 'Mouse']
    },
    {
    'name': 'MobileWorld Ltd.',
    'products': ['Smartphone', 'Tablet', 'Smartwatch']
    },
    {
    'name': 'GadgetHub Inc.',
    'products': ['Tablet', 'E-reader', 'Portable Charger']
    },
    {
    'name': 'AudioTech Co.',
    'products': ['Headphones', 'Speakers', 'Soundbar']
    },
    {
    'name': 'TechGear Ltd.',
    'products': ['Keyboard', 'Mouse', 'Webcam']
}]
def add_supplier():
    print("\nAdd New Supplier")
    name = input("Enter supplier name: ")
    products_list = input("Enter products supplied (comma separated): ")
    products_supplied = [p.strip() for p in products_list.split(',')]
    new_supplier = {
        'name': name,
        'products': products_supplied
    }
    suppliers.append(new_supplier)
def view_supplier_products():
    print("\nView Supplier’s Products")
    supplier_name = input("Enter supplier name: ")
    for supplier in suppliers:
        if supplier['name'].lower() == supplier_name.lower():
            print(f"Products supplied by {supplier['name']}:")
            for product in supplier['products']:
                print(f"- {product}")
            return
    print("Supplier not found.")
    