class ShoppingCart:
    def __init__(self):
        self.items = {}  # {item_name: price}
        self.quantities = {} # {item_name: qty}
        self.discount_applied = 0.0

    def add_item(self, name: str, price: float, qty: int):
        if qty < 0:
            return

        self.items[name] = price
        self.quantities[name] = self.quantities.get(name, 0) + qty

    def apply_coupon(self, percent: float):
        # BUG 2: Coupon stacks infinitely if called multiple times!
        self.discount_applied += percent

    def calculate_total(self) -> float:
        total = 0.0
        for name, price in self.items.items():
            total += price * self.quantities[name]
        
        final_price = total - (total * (self.discount_applied / 100))
        return final_price