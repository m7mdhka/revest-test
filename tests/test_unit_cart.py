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


def test_prevent_double_coupon_stacking():
    """AI generated this to prevent using the same coupon twice."""
    cart = ShoppingCart()
    cart.add_item("TV", 500, 1)

    # Apply 10% off twice
    cart.apply_coupon(10)
    cart.apply_coupon(10)

    # Should only be 10% off (450), not 20% off (400)
    assert cart.calculate_total() == 450, "Coupon incorrectly stacked!"
