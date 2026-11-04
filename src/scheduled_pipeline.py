import logging

from src.run_pipeline import run_pipeline
from src.logger_config import setup_logger


def main():
    setup_logger()

    logger = logging.getLogger("sales_pipeline")

    logger.info("SCHEDULED PIPELINE EXECUTION STARTED")

    try:
        run_pipeline(number_of_events=5)
        logger.info("SCHEDULED PIPELINE EXECUTION COMPLETED")

    except Exception:
        logger.exception("SCHEDULED PIPELINE EXECUTION FAILED")
        raise


if __name__ == "__main__":
    main()