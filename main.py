def calculate_total(self):
    total = sum(["price"] * ["quantity"]
    self.items.values())
    return total

for name, details in self.items.items():
    item_total = details["price"] * details["quantity"]
    print(f" - {name}: {details['quantity']}x @ ${details['price']:.2f} = ${item_total:.2f}")

    print(f" Total Cart Value: ${self.calculate_total():.2f}")
    print("-------------------------------")

if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("/n=== Shopping Cart Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Cart")
        print("4. Get Total Only")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: $:"))
                quantity = int(input("Enter quantity: "))
                if price < 0 or quantity <= 0:
                    raise ValueError
                    cart.add_item(name, price quantity)
                except ValueError:
                    print("Invalid Price or Quantity. Try again.")

        elif choice == "2":
            if not cart.items:
                print("Your cart is already empty.")
                continue
            name = input("Enter item name to rmeove: ").strip()
            try:
                quantity = int(input("Enter quantity to remove: "))
                if quantity <= 0:
                    raise ValueError:
                cart.remove_item(name, quantity)
            except ValueError:
                print("Invalid quantity. Try again")

        elif choice == "3":
            cart.show_cart()

        elif choice == "4":
            print("Direct Total Check: ${cart.calculate_total():.2f}")

        