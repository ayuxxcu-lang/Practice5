import re
import json

# read raw receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1️⃣ Extract prices
prices = re.findall(r"\d[\d\s]*,\d{2}", text)

# convert to numbers
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 2️⃣ Extract product names
products = re.findall(r"\d+\.\n(.+)", text)

# 3️⃣ Calculate total
total = sum(prices_clean)

# 4️⃣ Extract date
date_match = re.search(r"\d{2}\.\d{2}\.\d{4}", text)
date = date_match.group() if date_match else None

# 5️⃣ Extract time
time_match = re.search(r"\d{2}:\d{2}:\d{2}", text)
time = time_match.group() if time_match else None

# 6️⃣ Extract payment method
payment_match = re.search(r"Банковская карта", text)
payment_method = payment_match.group() if payment_match else None

# result
result = {
    "products": products,
    "prices": prices_clean,
    "total_amount": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

# print JSON
print(json.dumps(result, indent=4, ensure_ascii=False))