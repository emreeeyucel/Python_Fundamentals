from pprint import pprint
from requests import get
import requests

response = get('https://newsapi.org/v2/everything?q=tesla&from=2025-08-11&sortBy=publishedAt&apiKey=33d1f9fd08b3449d81e67f0deb4c4469')
data = response.json()
pprint(data)


# 0. index'den author, title ve publishedAt ifadelerini ekrana yazdıralım

pprint(f' Author : {data["articles"][0]["author"]}')
pprint(f' Title : {data["articles"][0]["title"]}')
pprint(f' Publis : {data["articles"][0]["publishedAt"]}')
# endregion





# Kullanıcıdan Alınan Yazar İsminin Makalesini Ekrana Yazdıralım.

author_name = input('Author Name : ')

for article in data.get('articles'):
    if article.get('author') == author_name:
        pprint(article)
# endregion





# "Region: 'articles', 'status' ve 'totalResults' anahtarları hariç kalan veriyi bir sözlükte saklayalım ve bunu yeni bir değişkende tutalım."
new_data = data['articles'][0]
pprint(new_data)
# endregion





# region Oluşturduğumuz 'new_data' adlı datamızdaki anahtarların isimlerini Türkçe karşılığı ile değiştirelim.

# Yeni anahtarlar listesi
key_map = ['kaynak', 'yazar', 'başlık', 'tanım', 'url', 'urlRresim', 'yayınlanmaTarihi', 'içerik']

# map ile anahtarları değiştirme
yeni_sozluk = dict(zip(key_map, new_data.values()))             # Yeni anahtarımız ile varolan değerleri birleştir.
pprint(yeni_sozluk)


# zip() fonksiyonu, Python'da birden fazla iterable (örneğin, listeler veya demetler) üzerinde elemanları birleştirerek yeni bir iterable oluşturur.  Örneğimizde anahtarları değiştirip, var olan değerlerimiz ile birleştirerek yeni bir sözlük yaratarak bu problemi çözdük. Map fonksiyonu ilede çözebilirdik.
# map() fonksiyonu ise, bir iterable (örneğin bir liste) üzerinde her bir öğeye belirli bir fonksiyonu uygulayarak dönüşüm yapar.
# endregion




# region Datamızdaki tüm anahtarların isimlerini Türkçe karşılığı ile değiştirelim.
haberler = []
key_map = ['kaynak', 'yazar', 'başlık', 'tanım', 'url', 'urlResim', 'yayınlanmaTarihi', 'içerik']

# Tüm makaleleri listeye ekle
for makale in data['articles']:
    haberler.append(makale)

# Her makale için Türkçe anahtarlarla yeni sözlük oluştur
for haber in haberler:
    yeni_haber = dict(zip(key_map, haber.values()))
    pprint(yeni_haber)
# endregion




# region toplam kaç author bulunmaktadır?
toplam = 0
for article in data['articles']:
    if article['author']:                       # Yazar varsa (None ya da boş değilse)
        toplam += 1

# print(toplam)
# endregion





# region toplam kaç adet description bilgisi bulunmaktadır? (None içerir)
toplam = 0
for article in data['articles']:
    # Eğer 'author' alanı boş değilse
    if article['description']:
        toplam += 1
# print(toplam)
# endregion






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





# Eğer bir haberin author bilgisi None olanları bulalım ve makaleyi yazalım
for item in data['articles']:
    if item['author'] is None:
        print(item)
# endregion





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





# region description uzunluğu 100 karakterden fazla olan haberlerin listesini al.

description_list = []

for item in data['articles']:
    if len(item['description']) > 100:
        description_list.append(item)

pprint(description_list)
print(len(description_list))
# endregion




# region Her haberin content alanındaki karakter sayısını hesaplayalım ve ortalama uzunluğu bulalım.
import statistics

content_list = []
content_len = []

for item in data['articles']:
    content_list.append(item['content'])

for item in content_list:
    content_len.append(len(item))

print(content_list)
print(content_len)

content_mean = statistics.mean(content_len)
print(content_mean)
# endregion




# region Her haberin yayın tarihini (publishedAt) alıp sadece yıl bilgilerini çıkarılım ve kaç kez tekrarlandığını bulalım
from collections import Counter

publishedAt_list = []
publishedAt_years = []

for item in data['articles']:
    publishedAt_list.append(item['publishedAt'])

print(publishedAt_list)


for i in publishedAt_list:
    publishedAt_years.append(i[:4])

print(publishedAt_years)
print(Counter(publishedAt_years))
# endregion




# region Her haberin yayın tarihini (publishedAt) alıp sadece yıl bilgilerini çıkarttıktan sonra aralarına '-' işareti koyarak birleştirelim
publishedAt_list = []
publishedAt_years = []
publishedAt_years_str = []

for item in data['articles']:
    publishedAt_list.append(item['publishedAt'])

for i in publishedAt_list:
    publishedAt_years.append(i[:4])

for item in publishedAt_years:
    publishedAt_years_str.append(str(item))

years_birleştirme = '-'.join(publishedAt_years_str) # join metodu, listedeki öğeleri birleştirirken araya koymak istediğiniz karakteri  kullanır; örneğin, yılları birleştirirken araya '-' konursa, sonuçta '2020-2021' gibi bir string elde edilir.

print(years_birleştirme)
# joın() sadece string ifadeler kullanımı için uygundur publishedAt içindeki değerler str ifade olarak geçmemekteydi önce str çevirdik sonra sonra join ile birleştirilmiştir.
# endregion




# region description metnindeki tüm kelimeri sayalım ve en çok tekrar eden kelimeyi bulalım.
from collections import Counter
import string

# Tüm description'ları listeye ekleme
description_list = []

for item in data['articles']:
    if item['description']:
        description_list.append(item['description'])

# Tüm description'ları birleştir
all_descriptions = ' '.join(description_list)

# Noktalama işaretlerini temizle, harfleri küçült                                     # Tüm metinlerdeki noktalamaları ve harf küçültmelerde kullanılcak fuction olarak kullanılabilir.
translator = str.maketrans('', '', string.punctuation)
clean_text = all_descriptions.translate(translator).lower()

# Kelimeleri ayır ve listeye eklenmesi
words = clean_text.split()

# Kelime frekanslarını say
word_counts = Counter(words)

# En sık geçen kelimeyi bul
most_common_word = word_counts.most_common(1)[0]

# Sonucu satır satır yazdır
print("En sık geçen kelime:")
print(most_common_word[0])
print("Geçme sayısı:")
print(most_common_word[1])
# endregion

