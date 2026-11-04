from src.sales_producer import generate_sales_event


def test_event_has_required_fields():
    event = generate_sales_event()

    required_fields = [
        "event_id",
        "event_type",
        "product_id",
        "product_name",
        "quantity",
        "unit_price",
        "total_amount",
        "event_timestamp",
    ]

    for field in required_fields:
        assert field in event


def test_total_amount_calculation():
    event = generate_sales_event()

    expected_total = event["quantity"] * event["unit_price"]

    assert event["total_amount"] == expected_total


def test_event_id_is_unique():
    event1 = generate_sales_event()
    event2 = generate_sales_event()

    assert event1["event_id"] != event2["event_id"]