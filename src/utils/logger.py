import logging
import os
from datetime import datetime

def setup_logger(log_file: str = '../logs/training.log', level=logging.INFO):
    """
    Set up logging configuration.
    """
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Also log to console
    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    return logging.getLogger(__name__)

def log_metrics(epoch: int, loss: float, accuracy: float = None):
    """
    Log training metrics.
    """
    logger = logging.getLogger(__name__)
    message = f"Epoch {epoch}: Loss = {loss:.4f}"
    if accuracy is not None:
        message += f", Accuracy = {accuracy:.4f}"
    logger.info(message)

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger initialized")
