import json
import os

def test_stock_data_file_exists():
    assert os.path.exists("public/stock_data.json")

def test_stock_data_format():
    with open("public/stock_data.json", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    for code, entry in data.items():
        assert "name" in entry
        assert "price" in entry or "error" in entry
