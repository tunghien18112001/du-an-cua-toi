
import json
import os
import urllib.request
from pathlib import Path

api_key = os.environ["GOLD_API_KEY"]

url = "https://api-tools.hitechcloud.vn/api/gold/prices"

request = urllib.request.Request(
    url,
    headers={
        "X-API-Key": api_key,
        "Accept": "application/json",
        "User-Agent": "GoldPriceTracker/1.0",
    },
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = json.loads(response.read().decode("utf-8"))

if not isinstance(data, (dict, list)):
    raise ValueError("Du lieu API khong hop le")

output = Path("gia-vang.json")
new_content = json.dumps(
    data,
    ensure_ascii=False,
    indent=2,
) + "\n"

old_content = output.read_text(encoding="utf-8") if output.exists() else ""

if old_content == new_content:
    print("Gia vang khong thay doi, khong can cap nhat.")
else:
    output.write_text(new_content, encoding="utf-8")
    print("Da cap nhat gia vang.")
