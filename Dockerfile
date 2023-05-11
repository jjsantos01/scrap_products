FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY scrap_products.py /app/scrap_products.py

VOLUME /app/data

ENTRYPOINT ["python", "scrap_products.py"]
