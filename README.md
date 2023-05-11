# Scrap Walmart Products

This Python script retrieve the name and price information from a given products page of the grocery store [Walmart Mexico](https://super.walmart.com.mx/). The output is a json file which contains the name and price for all the products in the page.

To run this script, clone this repo in your computer:
```bash
git clone git@github.com:jjsantos01/scrap_products.git
cd scrap_products
```

You need to have installed and running Docker in your system. Then, run in the terminal the next command to build the image:
```bash
docker build -t scrap-products .
```
Then, run the next command to execute the script. Note that you have to provide the URL from the Walmart Mexico website to scrape.
```bash
docker run -v $(pwd)/data:/app/data scrap-products URL_TO_SCRAP
```
for example:
```bash
docker run -v $(pwd)/data:/app/data scrap-products https://super.walmart.com.mx/browse/cuidado-de-la-ropa/detergente/detergente-liquido/3680083_3570057_3570058
```

A new JSON file with the information will be saved in the `data/` folder and the content printed in the terminal. The file looks like this:

```json
{
    "url": "https://super.walmart.com.mx/browse/cuidado-de-la-ropa/detergente/detergente-liquido/3680083_3570057_3570058",
    "products": [
        {
            "name": "Detergente L\u00edquido Ariel RevitaColor para ropa blanca y de color concentrado 2",
            "price": "$119.00"
        },
        {
            "name": "Detergente l\u00edquido Great Value para ropa de color 7 l",
            "price": "$129.00"
        },
        {
            "name": "Detergente l\u00edquido Persil gel universal 6.64 l",
            "price": "$211.00"
        },
        {
            "name": "Detergente l\u00edquido MAS colores intensos 6.64 l",
            "price": "$230.00"
        },
        {
            "name": "Detergente l\u00edquido MAS color 3 l",
            "price": "$111.00"
        },
    ]
}
```

For this project I used the libraries [`requests`](https://requests.readthedocs.io/en/latest/) y [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
