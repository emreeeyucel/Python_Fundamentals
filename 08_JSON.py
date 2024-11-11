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




# region Task 3
# "Region: 'articles', 'status' ve 'totalResults' anahtarları hariç kalan veriyi bir sözlükte saklayalım ve bunu yeni bir değişkende tutalım."
new_data = data['articles'][0]
pprint(new_data)

# endregion




# region Tüm anahtarların isimlerini Türkçe karşılığı ile değiştirelim.

# Yeni anahtarlar listesi
key_map = ['kaynak', 'yazar', 'başlık', 'tanım', 'url', 'urlRresim', 'yayınlanmaTarihi', 'içerik']

# map ile anahtarları değiştirme
yeni_sozluk = dict(zip(key_map, new_data.values()))             # Yeni anahtarımız ile varolan değerleri birleştir.
pprint(yeni_sozluk)


# zip() fonksiyonu, Python'da birden fazla iterable (örneğin, listeler veya demetler) üzerinde elemanları birleştirerek yeni bir iterable oluşturur.  Örneğimizde anahtarları değiştirip, var olan değerlerimiz ile birleştirerek yeni bir sözlük yaratarak bu problemi çözdük. Map fonksiyonu ilede çözebilirdik.
# map() fonksiyonu ise, bir iterable (örneğin bir liste) üzerinde her bir öğeye belirli bir fonksiyonu uygulayarak dönüşüm yapar.
# endregion

