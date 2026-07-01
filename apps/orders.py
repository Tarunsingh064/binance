from binance.exceptions import BinanceAPIException, BinanceOrderException

from apps.client import client
from apps.logger import logger


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order on Binance Futures Testnet.
    """

    try:
        logger.info(
            f"Sending MARKET order | Symbol={symbol}, Side={side}, Qty={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(f"Market order successful: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except BinanceOrderException as e:
        logger.error(f"Order Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise
def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order on Binance Futures Testnet.
    """

    try:
        logger.info(
            f"Sending LIMIT order | Symbol={symbol}, Side={side}, Qty={quantity}, Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Limit order successful: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except BinanceOrderException as e:
        logger.error(f"Order Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise