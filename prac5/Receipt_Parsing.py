import re
import json

with open ("raw.txt" , "r" , encoding = "utf-8" ) as file:
    text = file.read()

cost = re.findall(r"Стоимость\n(.+)", text)
print(cost)

name = re.findall(r"\d+\.\s*(.+)" , text )

print(name , end ="\n" )

total = 0
for price in cost :
    clean_price = price.replace(" ", "").replace(",", ".")
    total += float(clean_price) 
print(total)

date = re.findall(r"Время:\s*(.+)" , text)
print(*date)

payment = re.findall(r"(Банковская карта|Наличные)", text)
print(*payment)


sale_items = [
    {
        "number": m[0] ,
        "name": m[1].strip(),
        "quantity": m[2],
        "unit_price": m[3],
        "total_price": m[4]
    }
    for m in re.findall(r"(\d+)\.\n(.+?)\n([\d,]+) x ([\d\s,]+)\n([\d\s,]+)", text)
]

receipt_data = {
    "sale_items": sale_items,
    "payment_method": re.search(r"(Банковская карта|Наличные)", text).group(1),
    "total": re.search(r"ИТОГО:\s*([\d\s,]+)", text).group(1),
    "time": re.search(r"Время:\s*([\d.: ]+)", text).group(1),
    "operator": re.search(r"Оператор фискальных данных:\s*(.+?)Для проверки", text).group(1).strip()
}


print(json.dumps(receipt_data, ensure_ascii=False , indent=4 ))