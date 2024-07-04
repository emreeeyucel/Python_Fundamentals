# region Büyük olan sayıyı bul ve ekrana yazdır.

sayi_1 = int(input('Sayi Giriniz: '))
sayi_2 = int(input('Sayi Giriniz: '))

if sayi_1 > sayi_2:
    print(f'{sayi_1} sayısı {sayi_2} sayısından büyüktür. ')
else:
    print(f'{sayi_2} sayısı {sayi_1} sayısından büyüktür. ')
# endregion




# region Kullanıcıdan alınan sayı tek mi çift mi ?
sayi = int(input(f'Sayi : '))

if sayi % 2 == 0:
    print(f'{sayi} Sayısı Çifttir.')
else:
    print(f'{sayi} Sayısı Tektir.')
# endregion



# region Kullanıcıdan alınan sayı pozitif , negatif ve nötr ayrımı yap ekrana yazdır
sayi = float(input(f'Sayı : '))

if sayi < 0:
    print(f'{sayi} sayısı sıfırdan küçük olduğundan dolayı negatiftir.')
elif sayi > 0:
    print(f'{sayi} sayısı sıfırdan büyük olduğundan dolayı pozitiftir.')
elif sayi == 0:
    print(f'{sayi} sayısı sıfıra eşit olduğundan dolayı nötr.')
# endregion




# region Kullanıcıdan alınan mevsim bilgisini alalım ve matc - case ile hangi ayları içerdiğini ekrana yazalım
season = input('Mevsim : ')

match season:
    case 'ILKBAHAR':
        print('Mart, Nisan, Mayıs')
    case 'YAZ':
        print(' Haziran, Temmuz, Ağustos')
    case 'SONBAHAR':
        print(' Eylül, Ekim, Kasım')
    case 'KIŞ':
        print(' Aralık, Ocak, Şubat')
    case _:
        print('Girmiş olunan mevsim bulunmamaktadır.')
# endregion





# region Kullanıcıdan bir gün adı girişi al  match - case ile haftanın kaçıncı gününe geldiğini ekrana yazdır.
day = input('Gün Bilgisi : ')

match day:
    case 'pazartesi' | 'ptesi':
        print(f'haftanın 1. günüdür.')
    case 'salı':
        print(f'haftanın 2. günüdür.')
    case 'çarşamba':
        print(f'haftanın 3. günüdür.')
    case 'perşembe':
        print(f'haftanın 4. günüdür.')
    case 'cuma' :
        print(f'haftanın 5. günüdür.')
    case 'cumartesi':
        print(f'haftanın 6. günüdür.')
    case 'pazar':
        print(f'haftanın 7. günüdür.')
    case _:
        print('uzaylısın')
# endregion




# region Kullanıcıdan alınan 3 adet sayının en büyüğünü ekrana yazdır
a = int(input('1. Sayı : '))
b = int(input('2. Sayı : '))
c = int(input('3. Sayı : '))

if a < b and b > c:
    print(f'{b} en büyük sayıdır')
elif a > b and a > c:
    print(f'{a} en büyük sayıdır')
elif c > a and c > b:
    print(f'{c} en büyük sayıdır')
else:
    print(f'Sayılardan bazıları birbirine eşittir.')
# endregion




# region Kullanıcıdan araç türü ve hız bilgisi alalım.
# Otomobil 60'dan Büyükse Cezalı
# Motosiklet 70'den Büyükse Cezalı
# Kamyon 30'Dan Büyükse Cezalı

vehicle = input('Vehicle: ')
speed = int(input('Speed : '))

if speed > 0:
    if vehicle == 'car':
        if speed >= 60:
            print('Ceza Kaydı Bulunmaktadır.')
        else:
            print('Ceza Kaydı Bulunmamaktadır.')
    elif vehicle == 'mootcyle':
        if speed >= 80:
            print('Ceza Kaydı Bulunmaktadır.')
        else:
            print('Ceza Kaydı Bulunmamaktadır.')
    elif vehicle == 'truck':
        if speed >= 30:
            print('Ceza Kaydı Bulunmaktadır.')
        else:
            print('Ceza Kaydı Bulunmamaktadır.')
    else:
        print(f'Geçerli araç türü giriniz')
else:
    print('Pozitif Tutar Bilgisi Girmelisiniz.')
# endregion




# region Vucud Kitle İndeksi Algoritması oluştur
# Kullanıcı Bilgisi -> user_name : beast , password : 123

full_name = input('Full name: ')
user_name = input('User name: ')
password = input('Password: ')

if user_name == 'beast' and password == '123':
    print(f'Welcome {full_name}')

    kg = float(input('Weight: '))
    hg = float(input('Height: '))

    bmi = kg / hg ** 2

    if 0 <= bmi <= 18.5:
        print(f'{full_name}, {bmi} rating is poor')
    elif 18.6 <= bmi <= 24.9:
        print(f'{full_name}, {bmi} rating is normal')
    elif 25 <= bmi <= 30:
        print(f'{full_name}, {bmi} rating is overweight')
    elif 31 <= bmi <= 39.9:
        print(f'{full_name}, {bmi} rating is obese')
    else:
        print('Type valid information..!')
else:
    print('Please type into valid credantials..!')
# endregion




# region Kullanıcıdan Midterm, Final, Homework Notlarını Alalım
# Avg Hesaplayalım, Midterm Yüzde 30, Final Yüzde 60, Homework Yüzde 10 Etkili Olacak Ortalama Hesaplarken Harf Notunu Ekrana Yazdıralım

midterm = float(input('Midterm: '))
final = float(input('Final: '))
homework = float(input('Homework: '))

avg = midterm * 0.3 + final * 0.6 + homework * 0.1

if 90 <= avg <= 100:
    print('AA')
elif 85 <= avg <= 89:
    print('BA')
elif 80 <= avg <= 84:
    print('BB')
elif 75 <= avg <= 79:
    print('CB')
elif 70 <= avg <= 74:
    print('CC')
elif 65 <= avg <= 69:
    print('CD')
elif 60 <= avg <= 64:
    print('DD')
elif 55 <= avg <= 59:
    print('DC')
elif 50 <= avg <= 54:
    print('FD')
else:
    print('FF')
# endregion




# Kullanıcıdan Aradığı Ürün Bilgisini Alalım.
# Ürün Domates Yada Biber Yada Patlıcan İse Sebze Reyonuna Yönlendirelim
# Notebook, Kindle, Tablet İse Teknoloji Reyonuna Yönlendirelim
# Şampuan, Parfüm, Sabun İse Kozmetik Reyonuna Yönlendirelim

product = input('Ürün giriniz: ')
if product == 'domates' or product == 'biber' or product == 'patlican':
    print('Sebze reyonuna gidiniz..!')
elif product == 'notebook' or product == 'kindle' or product == 'tablet':
    print('Teknoloji reyonuna gidiniz..!')
elif product == 'şampuan' or product == 'parfüm' or product == 'sabun':
    print('Kozmetik reyonu gidiniz..!')
else:
    print('Aradığınız ürün bulunmamaktadır..!')
# endregion




# region Kullanıcıdan Satın Aldığı Kitap Sayısını Alalım
# Bir Kitap Parası 5TL
# 20'den Az Kitap Aldıysa Yüzde 5 İndirim
# 21 İle 50 Kitap Aldıysa Yüzde 10 İndirim
# 51 İle 75 Kitap Aldıysa Yüzde 15 İndirim

kitap_sayisi = int(input('Kitap sayısı: '))

if kitap_sayisi <= 0:
    print('Geçerli bir miktar giriniz..!')
else:
    if 1 <= kitap_sayisi <= 20:
        print(f'Alınan kitap sayısı: {kitap_sayisi}\n'
              f'Toplam Ödenecek Tutar {kitap_sayisi * 5 * 0.95}')
    elif 21 <= kitap_sayisi <= 50:
        print(f'Alınan kitap sayısı: {kitap_sayisi}\n'
              f'Toplam Ödenecek Tutar {kitap_sayisi * 5 * 0.90}')
    elif 51 <= kitap_sayisi <= 75:
        print(f'Alınan kitap sayısı: {kitap_sayisi}\n'
              f'Toplam Ödenecek Tutar {kitap_sayisi * 5 * 0.85}')
    elif 76 <= kitap_sayisi <= 100:
        print(f'Alınan kitap sayısı: {kitap_sayisi}\n'
              f'Toplam Ödenecek Tutar {kitap_sayisi * 5 * 0.70}')
    else:
        print('Maksimum 100 kitap alabilirsiniz..!')
# endregion




# region Kullanıcıdan İki Sayı Alın Ve Bu Sayıların Birbirine Tam Bölünüp Bölünmediğini Kontrol Edin.
sayi_1 = float(input('1.sayıyı giriniz : '))
sayi_2 = float(input('2.sayıyı giriniz : '))

if sayi_1 % sayi_2 == 0 or sayi_2 % sayi_1 == 0 :
    print(f'Sayılar Birbirine Bölünebilmektedir.')
else:
    print(f'Sayılar Birbirine Sölünmemektedir.')
# # endregion




# region linear bir doğrunun reel köklerini hespalayalım

from math import sqrt

a = float(input('(a) katsayısını girin: '))
b = float(input('(b) katsayısını girin: '))
c = float(input('(c) katsayısını girin: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = - b - sqrt(delta) / 2 * a
    x2 = - b + sqrt(delta) / 2 * a
    print(f'Reel kök: {x1}')
    print(f'Reel kök: {x2}')
elif delta == 0:
    x1 = - b - sqrt(delta) / 2 * a
    print(f'Reel kök: {x1}')
else:
    print('Reel kök bulunmammaktadır..!')
# endregion




# region Mesafe Hesaplama

from math import sqrt
import math
x1 = float(input("Birinci noktanın x koordinatını girin: "))
y1 = float(input("Birinci noktanın y koordinatını girin: "))
x2 = float(input("İkinci noktanın x koordinatını girin: "))
y2 = float(input("İkinci noktanın y koordinatını girin: "))

mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'2 Nokta arasındaki mesafe : {mesafe} : ')

# Not Öklid formulü, düzlemsel bir koordinat sistemi için kullanılır ve Dünya'nın yüzeyi kavisli olduğu için hassas sonuçlar vermez.
# Ancak, Dünya yuvarlak olduğu için daha karmaşık bir formül olan Haversine formülünü kullanmak gerekir.

# Almanya'nın koordinatları (Berlin)
lat1 = 52.5200  # Enlem (Latitude)
lon1 = 13.4050  # Boylam (Longitude)

# Türkiye'nin koordinatları (Ankara)
lat2 = 39.9334
lon2 = 32.8597

# Haversine formülünü uygula
R = 6371  # Dünya'nın yarıçapı (km)

dlat = math.radians(lat2 - lat1)
dlon = math.radians(lon2 - lon1)

a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
mesafe = R * c

print("Almanya ile Türkiye arasındaki mesafe:", mesafe, "km")
# endregion




#region Kullanıcıdan İki Tarih Alın Ve Bu Tarihler Arasındaki Gün Sayısını Hesaplayın.

from datetime import datetime
# İlk tarihi kullanıcıdan al
tarih1_str = input("İlk tarihi (GG.AA.YYYY formatında) girin: ")
tarih1 = datetime.strptime(tarih1_str, "%d.%m.%Y")

# İkinci tarihi kullanıcıdan al
tarih2_str = input("İkinci tarihi (GG.AA.YYYY formatında) girin: ")
tarih2 = datetime.strptime(tarih2_str, "%d.%m.%Y")

# Tarih farkını hesapla
tarih_farki = tarih2 - tarih1

# Sadece gün olarak al
gun_farki = tarih_farki.days

print("İki tarih arasındaki gün farkı:", gun_farki)
#endregion




#region Bir Karakter Al Ve Bu Karakterin Büyük Harf, Küçük Harf veya Özel Bir Karakter Olup Olmadığını Kontrol Et.
karakter = input('Bir karakter giriniz : ')
ascii_deger = ord(karakter)

if 65 <= ascii_deger <= 90:
    print("Girilen karakter bir büyük harftir.")
elif 97 <= ascii_deger <= 122:
    print("Girilen karakter bir küçük harftir.")
else:
    print("Girilen karakter özel bir karakterdir.")
# endregion




# region Bir sayının Mutlak Değerini Hesaplama
sayi = float(input('Sayı : '))

if sayi >= 0:
    print(f'Mutlak değer sonucu : {sayi}')
else:
    print(f'Mutlak değer sonucu : {sayi * -1}')
# endregion
















