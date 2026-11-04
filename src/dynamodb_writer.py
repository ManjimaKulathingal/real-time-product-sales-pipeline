import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

table = dynamodb.Table("SalesTransactions")


def save_transaction(event):
    converted_event = {
        key: Decimal(str(value)) if isinstance(value, float) else value
        for key, value in event.items()
    }

    try:
        response = table.put_item(Item=converted_event)
        return response

    except ClientError as error:
        print(f"DynamoDB error: {error}")
        raise

def get_transaction(event_id):
    response = table.get_item(
        Key={"event_id": event_id}
    )

    return response.get("Item")

def query_transaction(event_id):
    response = table.query(
        KeyConditionExpression=Key("event_id").eq(event_id)
    )

    return response.get("Items", [])