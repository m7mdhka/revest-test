from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_inventory_oversell_protection():
    """
    AI Scenario: There is only 1 PS5 in stock.
    The user tries to buy 5.
    The system SHOULD reject the order (400 Bad Request).
    """
    payload = {"item": "PS5", "quantity": 1}
    
    response = client.post("/checkout", json=payload)
    
    # The AI expects a 400 error because stock is insufficient
    assert response.status_code == 400
    assert response.json()["detail"] == "Not enough stock"