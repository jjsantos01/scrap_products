import json
import sys
import hashlib
from bs4 import BeautifulSoup
import requests

def get_products_info(url: str):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = [
        {
        "name": p.select_one('span[data-automation-id="product-title"]').text,
        "price": p.select_one('div[data-automation-id="product-price"] > div').text
        }
        for p in soup.select('div[data-item-id]')
        ]

    return {"url": url, "products": products}

url = sys.argv[1]
products = get_products_info(url)
filename = hashlib.md5(url.encode()).hexdigest()
with open(f'data/{filename}.json', 'w') as f:
    json.dump(products, f, indent=4)
print(products)
