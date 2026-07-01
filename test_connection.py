from apps.client import client

try:
    account = client.futures_account()

    print("✅ Connected Successfully!")
    print("Account Alias:", account["accountAlias"])

except Exception as e:
    print("Connection Failed")
    print(e)