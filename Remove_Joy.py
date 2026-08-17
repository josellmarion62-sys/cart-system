def remove_item(self, name, quantity=1):
        if name not in self.items:
            print(f"❌ '{name}' is not in your cart.")
            return

        if quantity >= self.items[name]["quantity"]:
            del self.items[name]
            print(f"🗑 Removed all '{name}' from the cart.")
        else:
            self.items[name]["quantity"] -= quantity
            print(f"➖ Removed {quantity}x '{name}' from the cart.")