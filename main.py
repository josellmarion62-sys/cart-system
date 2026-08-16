class ShoppingCart: 

    def add_item(self, name, price, quantity=1):
        if name is self.items:
            self.items[name]["quantity"] =+ quantity
        
        else:
            self.items[name]={"price": price, "quantity": quantity}
            print(f"Added {quantity}x '{name}' to the cart")

name = input ("Enter an Item: ")
price = float(input("Enter the Price: ₱" ))
quantity = int(input("Enter Quantity: "))
if price < 0 or quantity <= 0:
    print [add_item]
else:
    print("Invalid Quantity or Price")

def remove_item (self, name, new_price=None, new_quantity=):
    if name not in self.items:
        print(f"x'{name}'is not in your cart.")
        retun

    if new price is not None [][]
       self.items[name][price] 

    if quantity >=self.items[name][quantity]:
        del self.items[name]
    print (f"Remove all'{name}'"

remove_item()

if __name__ == "__main__":
    cart = ShoppingCart()
    
    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Cart")
        print("4. Get Total Only")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: $"))
                quantity = int(input("Enter quantity: "))
                if price < 0 or quantity <= 0:
                    raise ValueError
                cart.add_item(name, price, quantity)
            except ValueError:
                print("⚠️ Invalid price or quantity. Try again.")
                
        elif choice == "2":
            if not cart.items:
                print("⚠️ Your cart is already empty.")
                continue
            name = input("Enter item name to remove: ").strip()
            try:
                quantity = int(input("Enter quantity to remove: "))
                if quantity <= 0:
                    raise ValueError
                cart.remove_item(name, quantity)
            except ValueError:
                print("⚠️ Invalid quantity. Try again.")
                
        elif choice == "3":
            cart.show_cart()
            
        elif choice == "4":
            print(f"💰 Direct Total Check: ${cart.calculate_total():.2f}")
            
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose between 1 and 5.")