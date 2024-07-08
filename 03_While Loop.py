# region 0 -100 arasındaki sayıları ekrana yazdıralım

sayac = 0
while sayac <= 100:
    print(sayac)
    sayac += 1
# endregion



# region 0-100 Arası Kaçar Adet Çift Ve Tek Sayı Olduğunu Bulalım.

x = 0
cift_sayilar = 0
tek_sayilar = 0

while x <= 100:
    if x % 2 == 0:
        cift_sayilar += 1
    else :
        tek_sayilar += 1
    x += 1
print(f'Toplam Çift Sayısı : {cift_sayilar}\nToplam Tek Sayısı : {tek_sayilar}')
# endregion



# region 0 İle 100 Arasındaki Çift Ve Tek Sayıların Ayrı Ayrı Toplamlarını Ekrana Yazdıralım

x = 0
toplam_cift = 0
toplam_tek = 0

while x <= 100:
    if x % 2 == 0:
        toplam_cift += x
    else:
        toplam_tek += x
    x += 1
print(f'Çift sayıların toplamı : {toplam_cift}\n Tek sayıların Toplamı : {toplam_tek}')
# endregion



# region Kullanıcıdan 2 Tam Sayı Ve İşlem Türü Alalım. Kullanıcı Exit Diyene Kadar İşleme Devam Edilsin
# İşlem türleri --> exit , + , - , / , *

try:
    while True:
        process = input('işlem Türü : ')

        if process == 'exit':
            print('Uygulama kapatılıyor.')
            break
        else:
            sayi_1 = float(input('1. Sayı : '))
            sayi_2 = float(input('2.Sayı  : '))
            if process == '+':
                print(f'{sayi_1 + sayi_2}')
            elif process == '-':
                print(f'{sayi_1 - sayi_2}')
            elif process == '*':
                print(f'{sayi_1 * sayi_2}')
            elif process == '/':
                print(f'{sayi_1 / sayi_2}')
except ZeroDivisionError as err:
    print('İşlem Hatası Sayılar Sıfıra Bölünmez')
except ValueError as err:
    print('Yanlış Karakter Girişi Yapıldı Rakam Girilmelidir.')
# endregion



# region Kullanıcıdan Alınan Sayının Asal Bilgisini Bulalım.

sayi = int(input('Sayı : '))

if sayi <= 0:
    print('Sıfır ve Nehatif Sayılar Asal Değildir..')
else:
    is_prime = True
    if sayi == 1:
        is_prime = False
    sayac = 2
    while sayac < sayi:
        if sayi % sayac == 0:
            is_prime = False
            break
        sayac += 1
    if is_prime:
        print('Asal')
    else:
        print('Asal Değil')
# endregion



# region Kullanıcıdan Alınan Sayının Föktöriyelini Hesaplayalım

x = int(input('Sayı : '))

if x < 0:
    print('Sıfırdan küçük sayıların faktöriyeli hesaplanamaz')
else:
    result = 1
    if x == 0 or x == 1:
        print(f'Sonuç : {result}')
    else:
        while x > 1:
            result *= x
            x -= 1
        print(f'Sonuç : {result}')

# endregion



# region Kullanıcıdan Bir Metin Girişi Alın Ve Metindeki Her Bir Karakteri Alt Alta Yazdıran Bir Program Yazın.

kelime = input('Kelime : ')

while True:
    print(kelime)
# endregion



# region Kullanıcıdan Alınan Sayıdan Geriye Doğru Sayım Yaparak Ekrana Her Adımda Kalan Sayıyı Yazdıran Bir Program Yazın.

sayi = int(input(f'Sayı : '))
while sayi >= 0:
    print(f' Kalan adım sayısı {sayi}')
    sayi -= 1

# endregion



# region Kullancıdan Bir Tuşa Basmasını Sağlayan Sonsuz Bir Döngü Oluşturan Program Yazın. Program " q " Harfine Basana Kadar Devam Etsin.

while True:
    harf = input('Bir tuşa basınız : ')
    if harf == 'q':
        print('Uygulama Kapatılıyor.')
        break


# endregion



# region 10'dan Geri Sayım Yaparak Ekrana Her Adımda Kalan Sayıyı İkişer İkişer Azaltarak Yazdıran Bir Program Yazın.

sayi = 10
while sayi > 0 :
    sayi -= 2
    print(f'Kalan sayı adeti :  {sayi}')
# endregion



# region Kullanıcı Tarafından Girilen Bir Sayıya Kadar Olan Sayıların Toplamını Hesaplayan Bir Program Yazın, Ancak Bu Toplama Sadece 2'ye Bölünebilen Sayılar Dahil Edilmelidir.

x = int(input('Sayi : '))

sayac = 1
toplam = 0
list = []
while sayac <= x:
    if sayac % 2 == 0:
        list.append(sayac)
        toplam += sayac
    sayac += 1
print(f"{x} Sayısını 2'ye Bölen Sayıların Toplamı {toplam}")
print(list)
# endregion
