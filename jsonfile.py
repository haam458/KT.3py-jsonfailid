import json
import requests

url = 'https://dummyjson.com/products'
response = requests.get(url)

if response.status_code == 200:
    products_data = response.json()
    for products in products_data['products']:
        print(f"Hind: {products['price']}\nToode: {products['brand']}\n")
else:
    print("Päring ebaõnnestu, staatuskood:", response.status_code)

products = input("Millist toodet soovite: ")

for products in products['products']:
    if products['toode'].lower() == products.lower():
        print(f"{products} on {products['price']} €")
        break
if not products:
   print(f"{products} ei ole.")   
