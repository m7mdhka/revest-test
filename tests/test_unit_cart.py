from app.cart_logic import ShoppingCart


def test_add_normal_items():
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000, 1)
    cart.add_item("Mouse", 50, 2)
    assert cart.calculate_total() == 1100


# --- The AI "Catch" Tests ---


def test_prevent_negative_quantity_hack():
    """AI generated this to ensure users can't add negative items to lower price."""
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000, 1)
    cart.add_item("Laptop", 1000, -5)
    assert cart.quantities["Laptop"] >= 0, "Stock cannot be negative"
