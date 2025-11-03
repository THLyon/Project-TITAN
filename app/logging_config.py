# app/logging_config.py
import logging

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

def configure_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("titan")
    if not logger.handlers:  # avoid duplicate handlers on --reload
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(handler)
        logger.propagate = False
    logger.setLevel(level)
    return logger

# export a module-level logger for `from app.logging_config import logger`
logger = configure_logging()
