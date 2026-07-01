import argparse

from apps.validators import validate_order
from apps.orders import place_market_order, place_limit_order


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Order CLI"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (required for LIMIT orders)"
    )

    return parser.parse_args()


def print_order_summary(args):
    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price    : {args.price}")

    print("===================================")


def print_order_response(response):
    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")

    avg_price = response.get("avgPrice")
    if avg_price:
        print(f"Average Price : {avg_price}")

    print("====================================")
    print(" Order placed successfully!")


def main():
    args = parse_arguments()

    try:
        # Validate input
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Print request summary
        print_order_summary(args)

        # Place order
        if args.type == "MARKET":
            response = place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )

        else:
            response = place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        # Print response
        print_order_response(response)

    except ValueError as e:
        print(f"\n Validation Error: {e}")

    except Exception as e:
        print(f"\n Failed to place order: {e}")


if __name__ == "__main__":
    main()