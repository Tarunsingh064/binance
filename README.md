# Binance Futures Testnet CLI

A Python CLI application to place MARKET and LIMIT orders on the Binance USDT-M Futures Testnet.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- API logging
- Error handling
- Clean project structure

---

## Project Structure

```
binance-futures-cli/
│
├── app/
├── logs/
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Run Examples

### MARKET BUY

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### MARKET SELL

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### LIMIT BUY

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 95000
```

### LIMIT SELL

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Assumptions

- Uses Binance USDT-M Futures Testnet.
- API credentials are stored in a `.env` file.
- LIMIT orders require a price.
- MARKET orders execute immediately.
- Logging is stored inside the `logs` directory.

---

## Logging

All API requests, responses, and errors are logged.

Example log files are included:

- market_order.log
- limit_order.log