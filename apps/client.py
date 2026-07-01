from binance.client import Client

from apps.config import API_KEY, API_SECRET, BASE_URL
from apps.logger import logger

try:
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL

    logger.info("Connected to Binance Futures Testnet")

except Exception as e:
    logger.error(f"Client initialization failed: {e}")
    raise