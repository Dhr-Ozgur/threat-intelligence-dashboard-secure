import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = 'data/app.log'
os.makedirs('data', exist_ok=True)

logger = logging.getLogger('dashboard_logger')
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
