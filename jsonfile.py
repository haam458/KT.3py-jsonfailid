import json

with open("products.json", "r",encoding="utf-8") as file:
    products = json.load(file)
for products in products:
    lipstick = products["lipstick"]
    price = products["price"]

    print(f"Toode: {lipstick}")
    print(f"Hind: {price}")
    #print("-" * 40)
    #print(type(products))
    #print(products)