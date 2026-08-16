# cart-system
##Shopping Cart
###Description
A simple command-line Shopping Cart application built with Python. This project allows users to add items, remove items, view their cart, and calculate the total cost through an interactive menu.

Project Overview
This project demonstrates the use of Python classes, dictionaries, methods, loops, conditional statements, exception handling, and user input to create a functional shopping cart system.

Each item in the cart is stored with :

Item name
Price
Quantity

Features:

Add items to the shopping cart
Increase the quantity of an existing item
Remove a specific quantity of an item
Automatically remove an item when its quantity reaches zero
Display all items currently in the cart
Calculate the total cart value
Validate item prices and quantities
Interactive command-line menu
Handle invalid user input


=== Shopping Cart Menu ===
1. Add Item
2. Remove Item
3. Show Cart
4. Get Total Only
5. Exit
Add an Item

Select option 1 and enter the item name, price, and quantity.

Example:

Enter item name: Apple
Enter item price: $2.50
Enter quantity: 3

Added 3x 'Apple' to the cart.
Remove an Item

Select option 2 to remove a specific quantity.

Enter item name to remove: Apple
Enter quantity to remove: 1

Removed 1x 'Apple' from the cart.
View the Cart

Select option 3 to display the current items and total.

--- Current Shopping Cart ---
- Apple: 2x @ $2.50 = $5.00
- Bread: 1x @ $3.00 = $3.00
🛒 Total Cart Value: $8.00
-----------------------------
Check the Total

Select option 4 to get the current total without displaying all cart items.

Exit

Select option 5 to close the application.

Key Python Concepts Demonstrated
Object-Oriented Programming

The ShoppingCart class manages the cart and its operations.

class ShoppingCart:
Dictionary Data Structure

Items are stored using a dictionary:

self.items = {}

Each item contains its price and quantity.

Methods

The project uses methods for different cart operations:

add_item()
remove_item()
calculate_total()
show_cart()
Input Validation

The program checks that:

Price is not negative
Quantity is greater than zero
User input contains valid numbers
Users cannot remove items that are not in the cart
