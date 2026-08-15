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