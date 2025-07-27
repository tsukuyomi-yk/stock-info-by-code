import yfinance as yf
import json
from datetime import datetime

companies = {
    "7203": "トヨタ自動車",
    "6758": "ソニーグループ",
    "9984": "ソフトバンクグループ",
    "9432": "日本電信電話（NTT）",
    "8306": "三菱UFJフィナンシャル・グループ"
}

output = {}

for code, name in companies.items():
    try:
        ticker = yf.Ticker(f"{code}.T")
        data = ticker.history(period="1d")
        last = data["Close"].iloc[-1]
        prev = data["Close"].iloc[-2]
        diff = round(last - prev, 2)
        pct = round((diff / prev) * 100, 2)
        output[code] = {
            "name": name,
            "price": round(last, 2),
            "change": diff,
            "percent": pct,
            "updated": datetime.now().isoformat()
        }
    except Exception as e:
        output[code] = {
            "name": name,
            "error": str(e)
        }

with open("public/stock_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
