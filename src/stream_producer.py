
import time
import logging

from src.sales_producer import generate_sales_event


logger = logging.getLogger("sales_pipeline")


def produce_events(stream, number_of_events=None, stop_event=None):
    count = 0

    try:
        while (
            (number_of_events is None or count < number_of_events)
            and (stop_event is None or not stop_event.is_set())
        ):
            event = generate_sales_event()
            stream.put_event(event)
            count += 1

            logger.info(
                "Produced event %s | Product: %s | Amount: INR%s",
                event["event_id"],
                event["product_name"],
                event["total_amount"]
            )

            time.sleep(2)

    except Exception:
        logger.exception("Error while producing sales events")
        raise

    logger.info("Producer stopped. Total events produced: %s", count)
