from pprint import pprint
from requests import get
import requests

response = get('https://newsapi.org/v2/everything?q=tesla&from=2024-06-19&sortBy=publishedAt&apiKey=33d1f9fd08b3449d81e67f0deb4c4469')
data = response.json()
pprint(data)

# region Task 1
# 0. index'den author, title ve publishedAt ifadelerini ekrana yazdıralım

pprint(f' Author : {data["articles"][0]["author"]}')
pprint(f' Title : {data["articles"][0]["title"]}')
pprint(f' Publis : {data["articles"][0]["publishedAt"]}')
# endregion

# region Task 2
# Kullanıcıdan Alınan Yazar İsminin Makalesini Ekrana Yazdıralım.

author_name = input('Author Name : ')

for article in data.get('articles'):
    if article.get('author') == author_name:
        pprint(article)
# endregion


