import logging

from src.local_stream import LocalStream
from src.stream_producer import produce_events
from src.stream_consumer import consume_events
from src.logger_config import setup_logger


def run_pipeline(number_of_events=3):
    logger = setup_logger()

    local_stream = LocalStream()

    logger.info("STARTING SALES STREAMING PIPELINE")
    logger.info("Generating %s sales events", number_of_events)

    try:
        produce_events(
            local_stream,
            number_of_events=number_of_events
        )

        logger.info(
            "Events waiting in stream: %s",
            local_stream.size()
        )

        consume_events(
            local_stream,
            max_events=number_of_events
        )

        logger.info(
            "PIPELINE COMPLETED | Remaining events: %s",
            local_stream.size()
        )

    except Exception:
        logger.exception("PIPELINE FAILED")
        raise


if __name__ == "__main__":
    run_pipeline(number_of_events=5)