import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

print("🌍 Currency Converter CLI Tool")

try:
    amount = float(input("Enter amount: "))
    print("Example currency codes: USD, INR, EUR, JPY, GBP, AUD, CAD")
    from_currency = input("From currency (e.g., USD): ").strip().upper()
    to_currency = input("To currency (e.g., INR): ").strip().upper()

    url = f"{BASE_URL}/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        rate = data["conversion_rate"]
        converted = round(amount * rate, 2)

        print(f"\n💱 {amount} {from_currency} = {converted} {to_currency}")
        print(f"📈 Exchange Rate: 1 {from_currency} = {rate} {to_currency}")

        save = input("Do you want to save this to history? (y/n): ").strip().lower()
        if save in ["y", "yes"]:
            with open("conversion_history.txt", "a", encoding="utf-8") as f:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{now}: {amount} {from_currency} → {converted} {to_currency} (Rate: {rate})\n")
            print("✅ Saved to conversion_history.txt")
        else:
            print("ℹ️ Skipped saving to history.")
    else:
        print("❌ API Error:", data.get("error-type", "Unknown"))

except ValueError:
    print("❌ Invalid number for amount. Please enter a valid number.")
