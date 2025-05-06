# TradingView Telegram Botas

Šis botas priima signalus iš TradingView per webhook ir siunčia juos į Telegram kanalą.

## Kaip naudoti

1. Sukurk `.env` failą su šiuo turiniu:

```
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_TELEGRAM_CHAT_ID
```

2. Įjunk serverį:

```
pip install -r requirements.txt
python main.py
```

3. Nustatyk TradingView webhook'ą į: `https://tavo-boto-url.onrender.com/webhook`

## Signalų formatas

```json
{
  "symbol": "ETHUSDT",
  "direction": "LONG",
  "entry": 1768,
  "sl": 1755,
  "tp1": 1785,
  "tp2": 1800
}
```