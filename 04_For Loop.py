# region 0 İle 100 Arasındaki Çift Ve Tek Sayıların Ayrı Ayrı Toplamlarını Ekrana Yazdıralım
cift_sayi = 0
tek_sayi = 0

for i in range(0, 101):
    if i % 2 == 0:

        cift_sayi += i

    else :
        tek_sayi += i
print(f'Çift sayıların toplamı {cift_sayi} \nTek sayıların toplamı : {tek_sayi}')
# endregion



# region  0 İle 100 Arasındaki Çift Ve Tek Sayıların Ayrı Ayrı Toplamlarını Ve Hangi Sayıların Tek-Çift Olduğunu Listede Göstererek Ekrana Yazdıralım

cift = 0
tek = 0
cift_list = []
tek_list = []

for number in range(101):
    if number % 2 == 0:
        cift += number
        cift_list.append(number)
    else:
        tek += number
        tek_list.append(number)

print(f'Çift Sayılar Listesi : {cift_list}')
print(f'Tek Sayılar Listesi : {tek_list}')
print()
print(f'Çift Sayıların Toplamı : {cift}')
print(f'Çift Sayıların Toplamı : {tek}')

# endregion



# region Kullanıcıdan Alınan Başlangıç Ve Bitiş Sayılarının Karesini Hesaplayan Program Yazalım

baslangic = int(input('Başlangıç : '))
bitis = int(input('Bitiş. : '))
artis = int(input('Artış : '))

sayac = 0

for i in range(baslangic, bitis, artis):
    sayac += 1
    print(f'{sayac}. adımdaki  sonuç : {i ** 2}')

# endregion



# region Kullanıcıdan Alınan Kelimenin Harf Sayısını Bulan Program Yazalım

kelime = input("Bir kelime girin: ")
harf_sayisi = 0

for harf in kelime:
    if harf.isalpha():
        harf_sayisi += 1

print("Girilen kelimenin harf sayısı (boşluklar hariç):", harf_sayisi)

# endregion



# region Kullanıcıdan İki Karakter Dizisi Alın Ve Birinci Kelimenin İkinci Kelimenin İçinde Olup Olmadığını Kontrol Eden Program Yazalım.

ilk_dizi = input("İlk Karakter Dizisini Girin: ")
ikinci_dizi = input("İkinci Karakter Dizisini Girin: ")

if ilk_dizi.lower() in ikinci_dizi.lower():
    print(f"{ilk_dizi} dizesi, {ikinci_dizi} dizesinin içinde bulunuyor.")
else:
    print(f"{ilk_dizi} dizesi, {ikinci_dizi} dizesinin içinde bulunmuyor.")
# endregion



# region İki Karakter Dizisinde Harflerin Birbirinin İçinde Olup Olmadığını Kontrol Eden Program Yazalım.
kelime_1 = 'emre  '
kelime_2 = 'EMRE '

for i in kelime_2.lower():
    if i in kelime_1.lower():
        if i ==' ':
            continue
        print(f'{i} harfi {kelime_1} içinde GEÇMEKTEDİR..')
    else:
        print(f'{i} harfi {kelime_1} içinde GEÇMEMEKTEDİR..')
# endregion



# region Kullanıcıdan Bir Kelime Alın Ve Kullanıcının Belirlediği Harf veya İfade Bu Kelimenin İçinde Kaç Kez Tekrarlandığını Kontrol Eden Program Yazalım.

kelime = input('Kelime: ')
tekrarlanan = input('Tekrar Kontrolü İçin İfade Bilgisi : ')
toplam = 0

for i in kelime:
    if i == tekrarlanan:
        toplam += 1
print(f'{tekrarlanan} ifadesi {toplam} kere tekrar etmiştir.')

# endregion



# region Kullanıcıdan Alınan Bir Karakterin Harf Mi, Rakam Mı Yoksa Özel Bir Karakter Mi Olduğunu Kontrol Eden Bir Program Yazın.

kelime = input('İfade : ')

if kelime.isalpha():
    print('Kelimede Harf Var')
elif kelime.isdigit():
    print('Kelimede Rakam Var')
else:
    print('Özel Karakter İçeririr Boşluk Dahil')

# endregion



# region Cümle İşlemleri
# Cümledeki Her Kelimeyi Ters Çevir.
# Ters Çevrilen Kelimeleri ve Toplam Uzunluğu Ekrana Yazdır.

kelime = 'ben emre yücel python çalışmalarımı sizler ile paylaşıyorum.'

ters_kelime = kelime[::-1]
toplam = 0
for harf_sayisi in ters_kelime:
    if harf_sayisi ==' ':
        continue
    toplam += 1

print(f'Girilen kelime =  {kelime} Ters çevrilmiş hali = {ters_kelime}\n'
      f'Toplam harflerin sayısı : {toplam}')

# endregion



# region Cümle İşlemleri 2
# Cümledeki Her Kelimeyi Ters Çevir Ve Kelime Kelime Ayrım Yaparak Uzunluklarını Hesapla

cumle = "ben emre yücel python çalışmalarımda geziniyorsunuz"
cumle_2 = cumle.split(' ')

for harfler in cumle_2:
    ters = harfler[::-1]
    uzunluk = len(ters)
    toplam_uzunluk = len(cumle)
    print(f"Orijinal kelime: {harfler} - Kelimenin Tersi : {ters} - Kelime uzunluğu: {uzunluk}")
toplam_uzunluk = len(cumle)
print(f"Ters çevrilen kelimelerin toplam uzunluğu: {toplam_uzunluk}")

# endregion

