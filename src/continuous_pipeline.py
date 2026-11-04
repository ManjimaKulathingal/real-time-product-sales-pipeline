
import threading
import logging

from src.local_stream import LocalStream
from src.stream_producer import produce_events
from src.stream_consumer import consume_events
from src.logger_config import setup_logger


if __name__ == "__main__":

    logger = setup_logger()

    local_stream = LocalStream()
    stop_event = threading.Event()

    producer = threading.Thread(
        target=produce_events,
        args=(local_stream,),
        kwargs={"stop_event": stop_event}
    )

    consumer = threading.Thread(
        target=consume_events,
        args=(local_stream,),
        kwargs={"stop_event": stop_event}
    )

    logger.info("Starting continuous sales pipeline")

    producer.start()
    consumer.start()

    try:
        while producer.is_alive():
            producer.join(timeout=0.5)

    except KeyboardInterrupt:
        logger.info("Shutdown requested")

    finally:
        stop_event.set()

        producer.join()
        consumer.join()

        logger.info("Pipeline stopped successfully")
        logger.info("Remaining events: %s", local_stream.size())
