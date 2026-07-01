VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_order(symbol, side, order_type, quantity, price=None):
    """
    Validate order input before sending it to Binance.
    Raises ValueError if any validation fails.
    """

    # Symbol
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    # Side
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    # Order Type
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    # Quantity
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    # Price (required only for LIMIT orders)
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    return True