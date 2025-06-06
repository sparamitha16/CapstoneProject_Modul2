# Capstone Project Modul 2 - Stock & Sales Management System Program FMCG
# Soya Paramitha

#---------- Data Preparation ----------
# Database for Consumer Goods Products
goods = {
    "P001": {"product_name": "Instant Noodles - Chicken", "category": "Food", "price": 3500, "stock": 100},
    "P002": {"product_name": "Bottled Water 600ml", "category": "Beverage", "price": 12000, "stock": 200},
    "P003": {"product_name": "Chocolate Bar", "category": "Snack", "price": 11000, "stock": 150},
    "P004": {"product_name": "Toothpaste 100g", "category": "Personal Care", "price": 8500, "stock": 80},
    "P005": {"product_name": "Shampoo 200ml", "category": "Personal Care", "price": 17000, "stock": 60},
    "P006": {"product_name": "Laundry Detergent 1kg", "category": "Household", "price": 33000, "stock": 40},
    "P007": {"product_name": "Potato Chips - Salted", "category": "Snack", "price": 10800, "stock": 90},
    "P008": {"product_name": "Canned Sardines", "category": "Food", "price": 24000, "stock": 120},
    "P009": {"product_name": "Soft Drink 330ml", "category": "Beverage", "price": 10000, "stock": 180},
    "P010": {"product_name": "Bar Soap", "category": "Personal Care", "price": 7000, "stock": 150},
    "P011": {"product_name": "Dish Soap 250 ml", "category": "Household", "price": 32000, "stock": 55}
}

sales = [] # to store data of sales dynamically if any updates happen

# Generate new product ID - add product menu
def make_product_id():
    return f"P{len(goods)+1:03}"

#---------- Main Menu -----------
def main_menu():
    while True:
        print("-"*90)
        print("\t ===== ** Welcome to YES STORE Stock & Sales Management System ** =====")
        print("-"*90)
        print("Main Menus:")
        print("1. View Product Database")
        print("2. Add Product to Database")
        print("3. Update Product in Database")
        print("4. Delete Product from Database")
        print("5. Sales Management")
        print("0. Exit Program")

        try:
            main_input = input("Please choose a menu: ").strip()
            if main_input == "1":
                view_db()
            elif main_input == "2":
                add_product()
            elif main_input == "3":
                update_product()
            elif main_input == "4":
                delete_product()
            elif main_input == "5":
                sales_menu()
            elif main_input == "0":
                print("Thank you for using YES STORE Stock & Sales Management System. Exiting Program..")
                break
            else:
                print("Invalid choice. Please try again!")
        except:
            print("Invalid choice. Please check again your choice.")

# ----------- 1. View Product Database -----------
def view_db():
     while True:
        print("-"*45)
        print("\t  ** View Product Database ** ")
        print("Menus:")
        print("1. View All Products")
        print("2. View by Category")
        print("3. View by Price Range")
        print("4. View by Stock")
        print("5. Sort Products")
        print("0. Back to Main Menu")
        print("-"*45)

        view_input = input("Please choose a menu: ").strip()
        if view_input == "1":
            view_all()
        elif view_input == "2":
            view_category()
        elif view_input == "3":
            view_price()
        elif view_input == "4":
            view_stock()
        elif view_input == "5":
            sort()
        elif view_input == "0":
            break
        else:
            print("Invalid choice. Please try again!")
    

# View All Product
def view_all():
    if not goods:
        print("No products available.")
        return
    print("\nALL PRODUCT DATABASE")
    print("-"*90)
    print(f"{"Product ID":<10} | {"Product Name":<25} | {"Category":<20} | {"Price":<10}  | {"Stock"}")
    print("-"*90)
    for id, p in goods.items():
        print(f"{id:<10} | {p['product_name']:<25} | {p['category']:<20} | Rp{p['price']:<10,.2f} | {p['stock']}")

# View by Category
def view_category():
    print("\nExisting Categories:")
    print(" | Beverage | Food | Household | Personal Care | Snack |")
    category = input("Enter category to view: ").strip().capitalize()
    filter_cat = {}
    for id, p in goods.items():
        if p['category'].lower() == category.lower():
            filter_cat[id] = p
    if not filter_cat:
        print(f"No products found in category '{category}'.")
        return
    print(f"\nDATABASE FOR CATEGORY: {category.upper()}")
    print("-"*90)
    print(f"{"Product ID":<10} | {"Product Name":<25} | {"Category":<20} | {"Price":<10}  | {"Stock"}")
    print("-"*90)
    for id, p in filter_cat.items():
        print(f"{id:<10} | {p['product_name']:<25} | {p['category']:<20} | Rp{p['price']:<10,.2f} | {p['stock']}")
# View by Price
def view_price():
    try:
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        filter_price = {}
        for id, p in goods.items():
            if min_price <= p['price'] and p["price"] <= max_price:
                filter_price[id] = p
        if not filter_price:
            print("No products found in this price range.")
            return
        print(f"\nDATABASE FOR PRICE RANGE: {min_price} - {max_price}")
        print("-"*90)
        print(f"{"Product ID":<10} | {"Product Name":<25} | {"Category":<20} | {"Price":<10}  | {"Stock"}")
        print("-"*90)
        for id, p in filter_price.items():
            print(f"{id:<10} | {p['product_name']:<25} | {p['category']:<20} | Rp{p['price']:<10,.2f} | {p['stock']}")
    except ValueError:
        print("Invalid input. Please check and try again")

# View by Stock
def view_stock():
    try:
        min_stock = int(input("Enter minimum stock: "))
        filter_stock = {}
        for id, p in goods.items():
            if min_stock <= p['stock']:
                filter_stock[id] = p
        if not filter_stock:
            print("No products found with that stock.")
            return
        print(f"\nDATABASE FOR MINIMUM STOCK: {min_stock}")
        print("-"*85)
        print(f"{"Product ID":<10} | {"Product Name":<25} | {"Category":<20} | {"Price":<10}  | {"Stock"}")
        print("-"*85)
        for id, p in filter_stock.items():
            print(f"{id:<10} | {p['product_name']:<25} | {p['category']:<20} | Rp{p['price']:<10,.2f} | {p['stock']}")
    except ValueError:
        print("Invalid input. Please check and try again")

# Sort Product
def sort():
    print("-"*45)
    print("\t  ** Options to Sort Product ** ")
    print("Menus:")
    print("1. Sort by Name")
    print("2. Sort by Price")
    print("3. Sort by Stock")
    print("-"*45)
    sort_input = input("Choose sort option for displaying database: ")
    
    if sort_input == "1":
        sorted_items = sorted(goods.items(), key=lambda item: item[1]['product_name'])
    elif sort_input == "2":
        sorted_items = sorted(goods.items(), key=lambda item: item[1]['price'])
    elif sort_input == "3":
        sorted_items = sorted(goods.items(), key=lambda item: item[1]['stock'])
    else:
        print("Invalid choice. Please check and try again.")
        return
   
    print("-"*90)
    print(f"{"Product ID":<10} | {"Product Name":<25} | {"Category":<20} | {"Price":<10}  | {"Stock"}")
    print("-"*90)
    for id, p in sorted_items:
        print(f"{id:<10} | {p['product_name']:<25} | {p['category']:<20} | Rp{p['price']:<10,.2f} | {p['stock']}")

# ----------- 2. Add Product to Database -----------
def add_product():
        view_all()
        print("-"*45)
        print("\t  ** Add Product to Database ** ")
        print("-"*45)
        name = input("Product Name: ").capitalize()
        print("\nExisting Categories:")
        print(" | Beverage | Food | Household | Personal Care | Snack | ")
        print("or Define NEW Category")
        category = input("Category: ").capitalize()
        try:
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            product_id = make_product_id()
            goods[product_id] = {"product_name": name, "category": category, "price": price, "stock": stock}
            print(f"Product '{name}' has been added successfully!")
            success_add = input("Do you want to view updated database? (Y/N): ").upper()
            if success_add == "Y":
               view_all()
            else:
                main_menu() 
        except ValueError:
            print("Invalid price or stock input. Please check and try again.")

# ----------- 3. Update Product in Database ----------
def update_product():
    print("-"*45)
    print("\t  ** Update Product in Database ** ")
    print("-"*45)
    view_all()
    product_id = input("Enter Product ID to update: ").upper()
    if product_id in goods:
        p = goods[product_id]
        print("\nCurrent Product Info:")
        print(f"{'Field':<10} | {'Value'}")
        print("-" * 25)
        print(f"{'Name':<10} | {p['product_name']}")
        print(f"{'Category':<10} | {p['category']}")
        print(f"{'Price':<10} | Rp{p['price']:,.2f}")
        print(f"{'Stock':<10} | {p['stock']}")
        name = input("New Name (leave blank to keep current): ")
        category = input("New Category (leave blank to keep current): ")
        try:
            price = input("New Price (leave blank to keep current): ")
            stock = input("New Stock (leave blank to keep current): ")
            confirmation1 = input("Do you confirm to update the data? (Y/N): ").upper()
            if confirmation1 == "Y":
                if name != "":
                    p['name'] = name
                if category != "":
                    p['category'] = category
                if price != "":
                    p['price'] = float(price)
                if stock != "":
                    p['stock'] = int(stock)
                print(f"Product '{product_id}' updated successfully!")
                success_update = input("Do you want to view updated database? (Y/N): ").upper()
                if success_update == "Y":
                    view_all()
                else:
                    main_menu() 
            else:
                main_menu()
        except ValueError:
            print("Invalid input. Please check and try again.")
    else:
        print("Product not found.")

# ----------- 4. Delete Product from Database ----------
def delete_product():
    print("-"*45)
    print("\t  ** Delete Product from Database ** ")
    print("-"*45)
    view_all()
    product_id = input("Enter Product ID to delete: ").upper()
    confirmation2 = input("Are you sure you want to remove this product? (Y/N): ").upper()
    if confirmation2 == "Y":
        if product_id in goods:
            del goods[product_id]
            print(f"Product '{product_id}' deleted successfully!")
            success_delete = input("Do you want to view updated database? (Y/N): ").upper()
            if success_delete == "Y":
                view_all()
            else:
                main_menu()
        else:
            print("Product not found.")
    else:
        main_menu()


# ---------- 5. Sales Management Menu ----------------
def sales_menu():
    while True:
        print("-"*45)
        print("\t  ** Sales Management ** ")
        print("Menus:")
        print("1. Record a Sale")
        print("2. View Sales Records")
        print("0. Back to Main Menu")
        print("-"*45)
        sales_input = input("Choose an option: ")

        if sales_input == "1":
            record_sale()
        elif sales_input == "2":
            view_sales()
        elif sales_input == "0":
            break
        else:
            print("Invalid choice.")

# Record a Sale
def record_sale():
    while True:
        print("-"*45)
        print("\t  ** Input Sales Record ** ")
        print("-"*45)
        view_all()
        product_id = input("Enter Product ID to sell: ").upper()
        if product_id in goods:
            try:
                quantity = int(input("Enter quantity sold: "))
                if quantity <= goods[product_id]['stock']:
                    goods[product_id]['stock'] -= quantity
                    sales.append({"product_id": product_id, "quantity": quantity, "sales": sales})
                    print(f"Sale for {goods[product_id]['product_name']} has been recorded successfully!")
                    success_record = input("Do you want to record a sale data again? (Y/N): ").upper()
                    if success_record == "N":
                        break
                else:
                    print("Sales unsuccessful due to insufficient stock. Please contact the warehouse team.")
            except ValueError:
                print("Invalid quantity input. Please check and try again!")
        else:
            print("Product not found.")

# View Sales Records
def view_sales():
    print("-"*45)
    print("\t  ** View Sales Record ** ")
    print("-"*45)

    if not sales:
        print("No sales recorded.")
        return
    
    total_gross_sales = 0 # Setting up initial sales
    print("")
    print(f"{"Product ID":<10} | {"Product Name":<25} | {"Quantity Sold":<15} | {"Gross Sales":<20}")
    print("-"*80)

    for trx in sales:
        id = trx['product_id']
        name = goods[id]['product_name']
        quantity = trx['quantity']
        gross_sales = goods[id]['price']*quantity
        total_gross_sales += gross_sales
        print(f"{id:<10} | {name:<25} | {trx['quantity']:<15} | Rp{gross_sales:<20,.2f}")

    print("-"*80)
    print(f"{'Total Gross Sales':<58} Rp{total_gross_sales:,.2f}")

# Run the program
main_menu()
