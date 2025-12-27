from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock Database Inventory
INVENTORY = {
    "PS5": 1  # Only 1 left in stock!
}

class Order(BaseModel):
    item: str
    quantity: int

@app.post("/checkout")
def checkout(order: Order):
    if order.item not in INVENTORY:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # BUG: We forgot to check if order.quantity > INVENTORY[item]
    # We just process the payment immediately.
    
    remaining_stock = INVENTORY[order.item] - order.quantity
    return {"status": "confirmed", "remaining_stock": remaining_stock}