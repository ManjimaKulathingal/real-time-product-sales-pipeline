import boto3
import json
from datetime import datetime, timezone

S3_BUCKET = "manjima-imdb-movie-pipeline-2026"
AWS_REGION = "ap-south-1"

s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION
)


def check_s3_connection():
    response = s3_client.head_bucket(
        Bucket=S3_BUCKET
    )

    print("Successfully connected to S3!")
    print(f"Bucket: {S3_BUCKET}")
    print(f"Region: {AWS_REGION}")

    return response

def archive_sales_event(event):
    event_date = datetime.now(timezone.utc)

    object_key = (
        f"sales-events/"
        f"{event_date.year}/"
        f"{event_date.month:02d}/"
        f"{event['event_id']}.json"
    )

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=object_key,
        Body=json.dumps(event, default=str),
        ContentType="application/json"
    )

    print(f"Event archived successfully: {object_key}")

    return object_key


if __name__ == "__main__":
    check_s3_connection()

    sample_event = {
        "event_id": "s3-test-001",
        "event_type": "product_sale",
        "product_id": "P1001",
        "product_name": "Laptop",
        "quantity": 1,
        "unit_price": 55000.0,
        "total_amount": 55000.0,
        "event_timestamp": datetime.now(timezone.utc).isoformat()
    }

    archive_sales_event(sample_event)