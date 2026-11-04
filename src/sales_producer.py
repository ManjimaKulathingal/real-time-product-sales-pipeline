
import json
import random
import uuid
from datetime import datetime, timezone


PRODUCTS = [
    {"product_id": "P1001", "product_name": "Laptop", "price": 55000.00},
    {"product_id": "P1002", "product_name": "Headphones", "price": 2500.00},
    {"product_id": "P1003", "product_name": "Keyboard", "price": 1500.00},
    {"product_id": "P1004", "product_name": "Mouse", "price": 800.00},
    {"product_id": "P1005", "product_name": "Monitor", "price": 12000.00},
]


def generate_sales_event():
    """Generate one realistic product sales event."""

    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 3)

    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": "product_sale",
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total_amount": round(product["price"] * quantity, 2),
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    return event


if __name__ == "__main__":
    events = []

    for _ in range(5):
        event = generate_sales_event()
        events.append(event)

    with open("data/sales_events.json", "w") as file:
        json.dump(events, file, indent=4)

    print(f"Successfully generated {len(events)} sales events!")
    print("Saved to data/sales_events.json")
