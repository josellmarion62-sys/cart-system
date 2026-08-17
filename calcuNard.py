def calculate_total(self):
        total = sum(details["price"] * details["quantity"] for details in self.items.values())
        return total