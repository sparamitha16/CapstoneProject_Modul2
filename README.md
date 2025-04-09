CapstoneProject_Modul2
# **Sales & Stock Management Program for Retail**
____

## **Background**

This Sales & Stock Management Program is designed as a beginner-to-intermediate level project for learning and practicing Python through a real-world use case. It simulates a basic inventory and sales tracking system for FMCG (Fast-Moving Consumer Goods) businesses, such as mini markets or retail stores.

It was built to help users manage products, keep track of inventory, and record sales with ease using a simple command-line interface. This program uses Python dictionaries and lists for storing data, and it provides full CRUD (Create, Read, Update, Delete) functionality, along with sorting, filtering, and sales recording features.

## **Menu Overview & Function Explanations**

### **Main Menu (main_menu)**
This is the entry point of the program, where users can navigate to all available features:
    a. View Products
    b. Add Product
    c. Update Product
    d. Delete Product
    e. Sales Management
    f. Exit

    a. View Products (view_products): This menu allows users to view and organize the product list using different filters or sorting rules.
        Sub-Menu:
        * View All Products: Lists all products with details (ID, name, category, price, stock)
        * View by Category: Filters products by a specific category
        * View by Price Range: Filters products between two prices
        * View by Stock: Filters products with stock greater than or equal to a value
        * Sort Products: Allows sorting by Name, Price, or Stock
        * Back to Main Menu: Returns to the main menu


    b. Add Product (add_product): Adds a new product to the system. The program asks for such as Name, Category, Price, Stock quantity
    A product ID is auto-generated (P001, P002, etc.) using the generate_product_id() function.

    c. Update Product (update_product): Allows updating existing product information. The user inputs a product ID, and then:
        * Can modify name, category, price, and/or stock
        * Leave any field blank to keep the current value

    d. Delete Product (delete_product): Removes a product from the database using the product ID. Once deleted, the product is no longer available for viewing or sale.

    e. Sales Management (sales_menu): Handles all operations related to product sales.
        Sub-Menu:
        * Record a Sale: Inputs a product ID and quantity sold. Updates the stock and saves the sale record
        * View Sales Records: Displays all sales with Product ID, Name, and Quantity Sold. Sales are stored in the sales list.

    f. Exit: Closes the program with a farewell message.
