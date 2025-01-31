import requests

url = 'https://api.forismatic.com/api/1.0/'

params = {
    'method': 'getQuote',
    'format': 'json',
    'lang': 'ru'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Цитата: {data['quoteText']}")
    print(f"Автор: {data['quoteAuthor']}")
else:
    print(f"Ошибка: {response.status_code}")

import pandas as pd

data = pd.read_csv('sales_data.csv')

print("Данные о продажах:")
print(data.head())

total_sales = data.groupby('Product')['Sales'].sum().reset_index()

print("\nОбщий объем продаж по продуктам:")
print(total_sales)
