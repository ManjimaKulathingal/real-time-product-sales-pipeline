import boto3
import pytest

from moto import mock_aws
from src.dynamodb_writer import save_transaction, get_transaction, query_transaction


@pytest.fixture
def dynamodb_table():
    with mock_aws():
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="ap-south-1"
        )

        dynamodb.create_table(
            TableName="SalesTransactions",
            KeySchema=[
                {
                    "AttributeName": "event_id",
                    "KeyType": "HASH"
                }
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "event_id",
                    "AttributeType": "S"
                }
            ],
            BillingMode="PAY_PER_REQUEST"
        )

        yield


def test_save_transaction(dynamodb_table):
    event = {
        "event_id": "test-101",
        "product_name": "Laptop",
        "quantity": 1,
        "unit_price": 55000.0,
        "total_amount": 55000.0
    }

    response = save_transaction(event)

    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


def test_get_transaction(dynamodb_table):
    event = {
        "event_id": "test-102",
        "product_name": "Mouse",
        "quantity": 2
    }

    save_transaction(event)

    result = get_transaction("test-102")

    assert result["product_name"] == "Mouse"


def test_query_transaction(dynamodb_table):
    event = {
        "event_id": "test-103",
        "product_name": "Monitor"
    }

    save_transaction(event)

    result = query_transaction("test-103")

    assert len(result) == 1
    assert result[0]["product_name"] == "Monitor"