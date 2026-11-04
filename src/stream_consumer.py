import logging
from queue import Empty

from src.s3_archiver import archive_sales_event
from src.dynamodb_writer import save_transaction

logger = logging.getLogger("sales_pipeline")


def consume_events(stream, max_events=None, stop_event=None):
    count = 0

    try:
        while max_events is None or count < max_events:

            if stop_event is not None and stop_event.is_set():
                if stream.size() == 0:
                    break

            try:
                event = stream.events.get(timeout=1)

                # Save transaction to DynamoDB
                save_transaction(event)

                # Archive event in S3
                archive_sales_event(event)

                count += 1

                logger.info(
                    "Consumed and saved event %s | Product: %s | Amount: INR %s",
                    event["event_id"],
                    event["product_name"],
                    event["total_amount"]
                )

            except Empty:
                if max_events is None:
                    break

                if stop_event is not None and stop_event.is_set():
                    break

    except Exception:
        logger.exception("Error while consuming sales events")
        raise

    logger.info("Consumer stopped. Total events consumed: %s", count)