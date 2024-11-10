
# region Entry

number = [1, 34.5, 3, 45]
print(number)     # output ==> [1, 34.5, 3, 45]
print(number[1])  # output ==> 34.5
print(number[0])  # output ==> 1
print(number[3])  # output ==> 45
# endregion




# region George Foreman Bilgisini Listenin En Sonuna Built-in Bir Fonksyon İle Ekleyen Program Yazalım.

top_boxer = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfield', 'Rock Marciano']

top_boxer.append('George Foreman')
print(top_boxer)

# endregion




# region Floyd Mayweather Bilgisini 3. İndexe Ekleyen Program Yazalım.

top_boxer = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfield', 'Rock Marciano']

top_boxer.insert(3, 'Floyd Meyweather')
print(top_boxer)
# endregion




# region 3. İndeksten 5. İndexe kadar Silen Program Yazalım.

top_boxer = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfield', 'Rock Marciano']

del top_boxer[3:6]
print(top_boxer)
# endregion




# region  Current_boxer Listesi ile top_boxer Listesini Birleştiren Program Yazalım.

current_boxer = ['Antony jasua', 'Deantony Wilder', 'Tyson Fury']

top_boxer.extend(current_boxer)
print(top_boxer)
# endregion




# region Boş Bir Liste İçerisinde 0 - 100 Arasında Random Olacak Şekilde 10 Adet Sayı Üretip Listeye Sıralayan Program Yazalım.
from random import randint

sayilar = []

for i in range(10):
    sayilar.append(randint(a=0, b=100))
print(sayilar)
# endregion




# region Emre Kelimesinin Boşluklar Hariç Harfleri Listeye Ekleyen Program Yazalım.

kelime = 'emre yücel'
lst = []

for i in kelime:
    if i == ' ':
        continue
    lst.append(i)

print(lst)
# endregion




# region Kullancıdan Alınan Kelimede Geçen Sesli Harfleri Listeleyerek Ayıran Program Yazalım.

sesli_harfler = []
kelime = input('Kelime : ')
for harf in kelime:
    if harf.lower() in "aeıioöuü":
        sesli_harfler.append(harf)

print(f"{kelime} kelimesinin sesli_harfleri:", sesli_harfler)
# endregion




# region Kullancıdan Alınan Kelimede Geçen Sessiz Harfleri Listeleyerek Ayıran Program Yazalım.

sessiz_harfler = []
kelime = input('Kelime : ')
for harf in kelime:
    if harf.lower() not in "aeıioöuü":
        sessiz_harfler.append(harf)

print(f"{kelime} kelimesinin sessiz harfleri:", sessiz_harfler)
# endregion




# region "Merhaba Ben Emre Yücel Python Öğreniyorum" Cümlesindeki Sesli ve Sessiz Harfleri,  Boşluklar ve Harfler Dışında Başka Bir İfade Olmayacak Şekilde Listelere Ekleme Yapan Program Yazalım.
sesli = []
sessiz = []

for harf in 'ben emre  yücel python öğreniyorum':
    if harf.lower() in 'aeıioöuü' and harf != ' ':
        sesli.append(harf)
    if harf.lower() not in  'aeıioöuü' and harf != ' ':
        sessiz.append(harf)

print('sesli harfler :', sesli)
print('sessiz harfler :', sessiz)
# endregion




#region Bir Liste İçindeki Sayıların Toplamını Bulan Program Yazalım.

numbers = [1, 2, 3, 4, 5]
toplam = 0

for i in numbers:
    toplam += i
# endregion




# region Liste İçindeki Çift Sayıların Toplamlarını Ekrana Basalım ve Çift Olan Sayıları Listeye Ekleyen Program Yazalım.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toplam = 0
cift = []

for i in liste:
    if i % 2 == 0:
        toplam += i
        cift.append(i)
# endregion




#region Bir Metnin İçindeki Boşluk Sayısını Sayan Program Yazalım.

metin = "Python ile algoritma öğreniyorum"

toplam = 0
for i in metin:
    if i in ' ':
        toplam += 1
print(toplam)
# endregion




# region Listedeki Elemanları Büyükten Küçüğe Sıralayan Program Yazalım.

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort(reverse=True)
print(numbers)
# endregion




# region Kullanıcıdan Bir Başlangıç ve Bitiş Sayısı Alın, Bu Aralıktaki Sayıların Çift ve Tek Olanlarını Ekrana Yazdıran Program Yazalım.

x = int(input('Başlangıç : '))
y = int(input('Bitiş : '))

liste = [x, y]
tek = []
cift = []
for i in range(x, y):
    if i % 2 == 0:
        cift.append(i)
    else:
        tek.append(i)
print(tek, cift)
# endregion




# region İki Listenin İçerisini 10 Adet Random Sayı ile Dolduralım ve  Listedeki Aynı İndeksleri Toplayarak Farklı Listeye At.

from random import randint

lst_1 = []
lst_2 = []
lst_3 = []

for i in  range(10):
    lst_1.insert(i, randint(a=0, b=10))
    lst_2.insert(i, randint(a=0, b=10))
    lst_3.insert(i, (lst_1[i] + lst_2[i]))

print(lst_1)
print(lst_2)
print(lst_3)

# NOT --> list_2 + list_1  input == > [0, 3, 4, 4, 6, 5, 0, 1, 0, 7] iki listeyi birleştirir.
# endregion





# region  Random 10 Adet Atama Yapılan Listede Benzer Olan Sayılar İle Benzer Olmayan Sayıları Farklı Listelere Ekleyerek Ekrana Çıktı Veren Program Yazalım.
from random import randint
lst_1 = []
lst_2 = []
benzer_sayilar = []
farkli_sayilar = []

for number in range(10):
    lst_1.append(randint(1, 10))
    lst_2.append(randint(1, 10))

for numbers in lst_1:
    if numbers in lst_2:
        benzer_sayilar.append(numbers)
    else:
        farkli_sayilar.append(numbers)

print(lst_1)
print(lst_2)
print(benzer_sayilar)
print(farkli_sayilar)
# endregion





# region Bir Listedeki En Sık Tekrar Eden Elemanı Bulan Program Yazalım.
from collections import Counter

kelime = 'emre yücel'
elemansayisi = Counter(kelime)
ensiktekrar = elemansayisi.most_common((3))               # En Çok Tekrar Eden 3 Harfi Çıktı Verir.

print(elemansayisi)
print(ensiktekrar)
# endregion





# region Bir Listedeki Elemanların Kullanıcıdan Alınan Sayıya H Bölüp Bölünemeyeceğini Kontrol Eden ve Listeye Ekleyen Python Programı Yazın.

list_1 = []
list_2 = []
sayi = int(input('Sayı giriniz : '))

for i in range(20):
    if i % sayi == 0:
        list_1.append(i)
    if i % sayi != 0:
        list_2.append(i)

print(f'{sayi} rakamı 0 ile 20 arasındaki bölebildiği rakamlar :  {list_1}\n'
      f'{sayi} rakamı 0 ile 20 arasındaki bölemediği rakamlar : {list_2}')
# endregion




# region Bir Listenin Elemanlarını Toplayan ve Bu Toplamı Bir Önceki Toplama Ekleyen Bir Python Programı Yazın.

liste = [1, 2, 3, 4, 5]
toplam = 0
onceki_toplam = 0

for eleman in liste:
    onceki_toplam += toplam
    toplam += eleman
    print("Eleman:", eleman, "Toplam:", toplam, "Önceki Toplam:", onceki_toplam)
# endregion




# region  Bir Listenin Elemanlarının Karesinin Toplamını Bulan Python Programı Yazın.

liste = [1, 2, 3, 4, 5]
kare = 0

for i in liste:
    kare += i ** 2

print(kare)
# endregion




# region İç İçe Geçmiş Listelerin Her Bir Indexine " A " Harfini Ekleyelim

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

for i in nested_list:
    i.append('A')
    print(i)
# endregion




# region İç İçe Geçmiş Listeleri For İle Çıktı Farklarını İnceleyelim.
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

print(nested_list)                # Output -> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

for i in nested_list:
    for j in i:                   # Output -> [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]  Her Bir Liste Alt Alta Sıralanarak Çıktı Verir.
        for k in j:
            print(k)              # TypeError: 'int' object is not iterable -> Yinelenemeyen Dizi Hatası Alırız. 3. Bir Döngü Bulunamadı.

# endregion




# region İç İçe Geçmiş Listeleri For İle Çıktı Farklarını İnceleyelim.

nested_list = [
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ],
    [
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16]]
    ],
    [
        [[17, 18], [19, 20]],
        [[21, 22], [23, 24]]
    ],
    [
        [[25, 26], [27, 28]],
        [[29, 30], [31, 32]]
    ],
    [
        [[33, 34], [35, 36]],
        [[37, 38], [39, 40]]
    ],
    [
        [[41, 42], [43, 44]],
        [[45, 46], [47, 48]]
    ]
]


for outer_list in nested_list:
    for middle_list in outer_list:
        for inner_list in middle_list:
            print(inner_list)                             #   [1, 2]
                                                          #   [3, 4]
                                                          #   [5, 6]  Şeklinde Çıktı Alırız.Eğer bir for daha eklenseydi 1 - 2 - 3 Şeklinde Çıktı almış olacaktık.
# endregion




# region İç İçe Geçmiş Listenin İçindeki [37, 38] Listesinin İçine "BEN EMRE" Kelimesini Ekleyelim

nested_list = [
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ],
    [
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16]]
    ],
    [
        [[17, 18], [19, 20]],
        [[21, 22], [23, 24]]
    ],
    [
        [[25, 26], [27, 28]],
        [[29, 30], [31, 32]]
    ],
    [
        [[33, 34], [35, 36]],
        [[37, 38], [39, 40]]
    ],
    [
        [[41, 42], [43, 44]],
        [[45, 46], [47, 48]]
    ]
]

nested_list[4][1][0].append('BEN EMRE')
print(nested_list)
# endregion




# region İç İçe Geçmiş Listenin Çıktısını  [[1, 2], [3, 4]] Şeklinde Verelim.

nested_list = [
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ],
    [
        [[9, 10], [11, 12]],
        [[13, 14], [15, 16]]
    ],
    [
        [[17, 18], [19, 20]],
        [[21, 22], [23, 24]]
    ],
    [
        [[25, 26], [27, 28]],
        [[29, 30], [31, 32]]
    ],
    [
        [[33, 34], [35, 36]],
        [[37, 38], [39, 40]]
    ],
    [
        [[41, 42], [43, 44]],
        [[45, 46], [47, 48]]
    ]
]


for i in nested_list:
    for k in i:
        print(k)
# endregion




# region Liste İçinde Sunulan İsimlerden Hazır Mail Şablonu Oluşturalım

users = ['burak yilmaz', 'mustafa gökhan dalgıç', 'kerim abdul cabbar okkes', ' ertugrul', ' ']
mail_address = []

for i in users:
    if i == ' ' or i == '':
        continue
    user_names = i.split()
    if len(user_names) >= 2:
        mail_address.append(f'{user_names[0]}.{user_names[-1]}@hotmail.com')

print(mail_address)

# endregion

