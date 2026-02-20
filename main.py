from inventory import add_product, update_stock, record_sale, generate_report, check_reorder_alerts, view_product_details, delete_product
from suppliers import add_supplier, view_supplier_products

def main():
    while True:
        print('\n' + '='*50)
        print("STOCKIT - Mini Inventory Management System")
        print('='*50)
        print('''
        1. Add New Product
        2. Update Product Stock
        3. Record a Sale
        4. Add Supplier
        5. View Supplier’s Products
        6. Generate Inventory Report
        7. Check Reorder Alerts
        8. View Product Details
        9. Delete a Product
        10. Exit
        ''')
        choice = input("Enter your choice (1-10): ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_stock()
        elif choice == '3':
            record_sale()
        elif choice == '4':
            add_supplier()
        elif choice == '5':
            view_supplier_products()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            check_reorder_alerts()
        elif choice == '8':
            view_product_details()
        elif choice == '9':
            delete_product()
        elif choice == '10':
            print("Exiting StockIt. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")
if __name__ == "__main__":
    main()