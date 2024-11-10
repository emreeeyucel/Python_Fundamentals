# region Task 1


from pprint import pprint

my_dict = {
   'Full Name': 'Emre Yücel',
    'Age': '30',
    'Interested Sport': ['Boxing', 'Wrestling', 'UFC'],
    'Favori Books': {
        'Bilimsel': 'The Logic Scientfic Discovery',
        'Savaş Tarihi': {
            'Napoleon A Life': 'Andrew Robert',
            'Cambridge War History': 'J.J Halt'
        }
    },
    'Programming Language': ('Python', 'Sql', 'C#')
}

# Emre Yücel'i Ekrana Çıktı Verelim.
print(my_dict['Full Name'])



# ['Boxing', 'Wrestling', 'UFC'] Çağıralım.
print(my_dict['Interested Sport'])



# Boxing Değerini Çıktı Verelim.
print(my_dict['Interested Sport'][0])
# Not : Interested Sport yazdıktan sonra artık Listenin İçindeyiz ve Listenin Kuralları Geçerlidir.



# ['Boxing', 'Wrestling', 'UFC'] İçine  Kick Boks " Kelimesini Ekleyelim ve Tüm Bilgilerin Çıktısını Ekrana Yazdıralım.
my_dict['Interested Sport'].append('Kick Boks')
pprint(my_dict)


# Programming Language Değerini Çağıralım ve En Sevdiği Dil Bilgisini Ekrana Yazdıralım.
print(f'Kullanmayı Bildiği Diller :  {my_dict["Programming Language"]}\n'
      f'En sevdiğim Dil : {my_dict["Programming Language"][0]}')



# J.J Halt Değerini Ekrana Yazdıralım.
print(my_dict['Favori Books']['Savaş Tarihi']['Cambridge War History'])    # Çağırdıkça Sözlük Çıktığı İçin Karşımıza Sözlükten Çağırma Kuralına Göre Hareket Edilmelidir.



# 'Napoleon A Life ' Bölmesine Basım Yılı Olan 2014 Yıl Bilgisini Ekleyelim ve Tüm Bilgilerin Çıktısını Ekrana Yazdıralım.
my_dict['Favori Books']['Savaş Tarihi']['Napoleon A Life'] = 'Andrew Robert, 2014'
pprint(my_dict)

# endregion




# region Task 2

realese_year_movie = {
    'Fight Club': 1999,
    'The Matrix': 1999,
    'Interstaller': 2014,
    'Inception ': 2010,
    'Dune': 2021
}

# Herhangi Bir Değeri Ekrana Yazdıralım
# 1. Yol
print(f'Year :  {realese_year_movie.get('The Matrix')}')
# 2. Yol
print(f'Year : {realese_year_movie['Fight Club']}')



# Tüm Anahtarları Ekrana Yazdıralım.
for item in realese_year_movie.keys():
    print(item)


# Sözlüğün Tüm Değerlerini Ekrana Yazdıralım.
for item in realese_year_movie.values():
    print(item)

# Sözlüğün Anahtar Ve Değer Bilgilerini Ekrana Yazdıralım
for key, value in realese_year_movie.items():
    print(f'Movie Name : {key}\n'
          f'Realese Year : {value}')

# endregion




# region Task 3

products = [
    {'name': 'Everlast Pro Boxing Gloves','price': 245},
    {'name': 'Everlast Tranining Gloves', 'price': 200} ,
    {'name': 'Bagy' , 'price': 645},
    {'name': 'Iphone', 'price': 95000},
    {'name': 'Samsung', 'price': 85000},
    {'name': 'Lonova', 'price': 15000},
    ]

# Listenin Sonuna Benzer Bir Sözlük Ekleyelim Ve Ekrana Çıktı Verelim (Eklenen İsim ve Tüm Liste Ayrı Ayrı Basılsın)

products.append({'name': 'Nokia', 'price': 1000})
print(products[6]['name'])
pprint(products)



# Products Listesindeki Tüm Ürünlerin Fiyatlarının Toplamlarının Çıktısını Ekrana Yazdıralım.

toplam = 0

for item in products:
    toplam += item['price']
print(f'Tüm Ürünlerin Toplamı : {toplam}')

# Products Listesindeki Fiyatı 50000 TL'den Fazla Olan ürünlerin Çıktısını Ekrana Yazdıralım.

for item in products:
    if item['price'] >= 5000:

        print(f'Ürün İsmi : {item["name"]}\n'          
              f'Değer :{item["price"]}')
        print()


#  Products Listesindeki Everlast Geçen Tüm Ürünlerin Fiyatlarının Toplamlarının Çıktısını Ekrana Yazdıralım.

toplam = 0
for i in products:
    if 'everlast' in i['name'].lower():
        toplam += i['price']

print(toplam)

# Ürün Adı İçerisinde Everlast Geçen Ve Fiyat Aralığı 200 ile 600 Arasında Olan Ğrünleri Listeleyelim

for item in products:
    if 'Everlast' in item['name'] and item ['price'] >= 200 and item ['price'] <= 600 :
        print(f'Product Name : {item["name"]}\n'
          f'price :{item["price"]}')
        print()
        print(item)   # Output ->  {'name': 'Everlast Pro Boxing Gloves', 'price': 245} ve  {'name': 'Everlast Tranining Gloves', 'price': 200} Aynı Sonuç Çıktı Farkı ..

# endregion




# region Task 4

realese_year_movie = [{
    'Fight Club': 1999,
    'The Matrix': 2000,
    'Interstaller': 2014,
    'Inception ': 2010,
    'Dune': 2021
}]

# Tüm Değerleri Ekrana Yazdıralım.
for movie in realese_year_movie:
    for value in movie.values():
        print(value,  end=' ')

# endregion