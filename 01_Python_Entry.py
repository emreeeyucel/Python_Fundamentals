# entry level Example


# region Python Entry_lv1
print(" Hello Python! ")

x = 8
print(x)
print(type(x))

x = " Mike Tyson "
print(x)
print(type(x))

x = 93.1
print(x)
print(type(x))
# endregion


# region Basit 4 işlem (farklı şekillerde print ifadesi içermektedir)
x = int(input(" Give a number: "))
y = int(input(" Give a number: "))

toplam = x + y
cikarma = x - y
carpma = x * y
bolme = x / y

print(f' Toplam = {toplam}')
print(f' Cıkarma = ', cikarma)
print(f' Carpma = {carpma}')
print(f' Bolme = ', bolme)
# endregion


# region karenin alan ve çevresi hesaplama
x = int(input(" Kenar bilgilerini giriniz: "))

kare_alan = x * x
kare_cevre = x * 4

print(f' Karenin alanı = {kare_alan} - Karenin cevresi = {kare_cevre}')
# endregion


# region dikdörtgen alan ve çevresi hesaplama (\n ile de yapıldı)
x = int(input(" Lütfen uzun kenar bilgisi giriniz: "))
y = int(input(" Lütfen kısa kenar bilgisi giriniz: "))

dikdortgen_alan = x * y
dikdortgen_cevre = (x + y) * 2

print(f' Dikdortgenin alanı = {dikdortgen_alan}')
print(f' Dikdortgen çevre = ', dikdortgen_cevre)


x = int(input(" Lütfen kenar bilgisi giriniz: "))
y = int(input(" Lütfen kenar bilgisi giriniz: "))

d_a = x * y
d_c = (x + y) * 2

print(f' Dikdörtgen alanı = {d_a}\n Dikdörtgen çevre = {d_c}')
# endregion