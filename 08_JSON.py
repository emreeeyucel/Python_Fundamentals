from pprint import pprint
from requests import get
import requests

response = get('https://newsapi.org/v2/everything?q=tesla&from=2025-08-11&sortBy=publishedAt&apiKey=33d1f9fd08b3449d81e67f0deb4c4469')
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



# region Task 4
# region Tüm anahtarların isimlerini Türkçe karşılığı ile değiştirelim.

# Yeni anahtarlar listesi
key_map = ['kaynak', 'yazar', 'başlık', 'tanım', 'url', 'urlRresim', 'yayınlanmaTarihi', 'içerik']

# map ile anahtarları değiştirme
yeni_sozluk = dict(zip(key_map, new_data.values()))             # Yeni anahtarımız ile varolan değerleri birleştir.
pprint(yeni_sozluk)


# zip() fonksiyonu, Python'da birden fazla iterable (örneğin, listeler veya demetler) üzerinde elemanları birleştirerek yeni bir iterable oluşturur.  Örneğimizde anahtarları değiştirip, var olan değerlerimiz ile birleştirerek yeni bir sözlük yaratarak bu problemi çözdük. Map fonksiyonu ilede çözebilirdik.
# map() fonksiyonu ise, bir iterable (örneğin bir liste) üzerinde her bir öğeye belirli bir fonksiyonu uygulayarak dönüşüm yapar.
# endregion




# region Task 5
# region toplam kaç author bulunmaktadır?
toplam = 0
for article in data['articles']:
    if article['author']:                       # Yazar varsa (None ya da boş değilse)
        toplam += 1

# print(toplam)
# endregion




# region Task 6
# region toplam kaç adet description bilgisi bulunmaktadır? (None içerir)
toplam = 0
for article in data['articles']:
    # Eğer 'author' alanı boş değilse
    if article['description']:
        toplam += 1
# print(toplam)
# endregion





# region Task 7
# toplam kaç author bulunmaktadır? (len formülü)
# Boş olmayan 'author' değerine sahip makaleleri listele
authors_with_values = []  # Boş bir liste başlatıyoruz

# Makaleler üzerinde döngü başlatıyoruz
for article in data['articles']:
    if article['author']:
        # Makaleyi listeye ekliyoruz
        authors_with_values.append(article)                     # author varsa makaleyi listeye ekle. Ardından listedeki dictleri say.
pprint(authors_with_values)

# listeyi kullanarak toplam sayıyı buluyoruz
toplam = len(authors_with_values)

print(toplam)
# endregion




# region Task 8
# Eğer bir haberin author bilgisi None olanları bulalım ve makaleyi yazalım

for item in data['articles']:
    if item['author'] is None:
        print(item)
# endregion




# region Task 9
# Eğer bir haberin author bilgisi None ise "Unknown Author" olarak güncelleyen bir kod nasıl yazılır?


# Path 1
for item in data['articles']:
    if item['author'] is None:
        item['author'] = 'Unknown Author'

# Path 2
for item in data['articles']:
    if item['author'] is None:
        item.update({'author': 'Unknown Author'})
# endregion




# region Task 10
# description uzunluğu 100 karakterden fazla olan haberlerin listesini al.

description_list = []

for item in data['articles']:
    if len(item['description']) > 100:
        description_list.append(item)

pprint(description_list)
print(len(description_list))

# endregion