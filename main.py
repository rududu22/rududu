from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if not data:
        return "No JSON payload received", 400

    # Išformuok žinutę pagal signalą
    try:
        symbol = data["symbol"]
        direction = data["direction"]
        entry = data["entry"]
        sl = data["sl"]
        tp1 = data["tp1"]

        message = (
            f"**Naujas signalas**\n"
            f"Symbolis: {symbol}\n"
            f"Kryptis: {direction}\n"
            f"Entry: {entry}\n"
            f"Stop Loss: {sl}\n"
            f"Take Profit: {tp1}"
        )

        # Siunčiam į Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            return f"Telegram error: {response.text}", 500

        return "Signal received and sent to Telegram", 200

    except KeyError as e:
        return f"Missing key in payload: {e}", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
