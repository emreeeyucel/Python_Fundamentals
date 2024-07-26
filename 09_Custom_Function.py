# Entry
# Python'da özel fonksiyonlar tanımlamak, kodunuzu daha düzenli, okunabilir ve tekrar kullanılabilir bir hale getirir.
# 'def' anahtar kelimesi ile tanımlanır.


# region Task 1
def greeting_people():
    print('Hello Emre..!')

greeting_people()
# endregion




# region Task 2
def greeting_people(Full_name: str):
    print(f'Hello  {Full_name}')

greeting_people(input('Full name : '))
# endregion




# region Task 3
# 2 Sayının Toplamını Yapan Fonksiyon Yaz
def sum_two_number(x: int, y: int):
    print(f'Sum : {x + y}')

sum_two_number(
    int(input('Number 1 : ')),
    int(input('Number 2 : '))
)
# endregion




# region Task 4
# Kullanıcıdan Alınan Sayının Çift Mi Tek Mi Olduğunu Söyleyen Fonksiyon Yaz
def mode_number(sayi: int):

    if sayi % 2 == 0:
        print('sayı Çift')
    else:
        print('sayı tek ')

sayi = int(input('Sayı : '))
mode_number(sayi)
# endregion



# region Task 5
# Kullanıcıdan Fullname Alalım Ve Verilen Tam Addan Mail Adresi Oluşturalım
def mail_creator(full_name: str) -> None:
    """
    This function creat nail adres via full name.
    :param full_name: this argumant must be string
    :return: none
    """
    splited_name = full_name.lower().split(' ')
    print(f'{splited_name[0]}.{splited_name[-1]}@bilgeadam.com ')

tam_ad = input('full name : ')
mail_creator(tam_ad)
# endregion




# region Task 6
# Login Girişi Yapalım.

user = [
    ('beast', '123'),
    ('bear', '234'),
    ('savange', '987'),
]
def login(user_name: str, password: str):
    is_active = False

    for userName, pwd in user:
        if userName == user_name and pwd == password:
            is_active = True
            break

    if is_active:
        print(f'{user_name} Hoşgeldin')
    else:
        print('Kullanıcı adınız yada Şifreniz hatalı ..! ')


login('beast', '123')
login('bear', '234')
login('savange', '987')

# endregion




# region Task 7
# Liste İçerisine Random Atanan Sayılardan Çiftleri 2 İle, Tek Sayıları 3 İle Çarparak Farklı Listelere Ekleyin.
from random import randint
number = []
cift = []
tek = []
def append_lst() -> list:
    for i in range(5):
        number.append(randint(1, 10))

    return number

def tek_cift(sayi: int) -> str:

    if sayi % 2 == 0:
        return 'cift'
    elif sayi % 2 != 0:
        return 'tek'

def ekran_bas(sonuc: str, sayi: int) -> None:

    if sonuc == 'cift':
        cift.append(sayi * 2)

    elif sonuc == 'tek':
        tek.append(sayi * 3)


def main():

    append_lst()
    for i in number:
        sonuc = tek_cift(i)
        ekran_bas(sonuc, i)
    print(number)
    print(cift)
    print(tek)

main()
# endregion




# region Task 8
# Kullanıcıdan Alınan 3 Adet Sayıyı Topladıktan Sonra Karesini Ekrana Yazalım

def toplam(x: int, y: int, z: int) -> int:
    return x+y+z

def karesini_hesapla(toplam_sonuc: int) -> None:
    print(f'Sonuç : {toplam_sonuc ** 2}')

def main():
    x = int(input('1. Sayi : '))
    y = int(input('2. Sayi : '))
    z = int(input('3. Sayi : '))

    sonuc = toplam(x, y, z)
    karesini_hesapla(sonuc)
main()
# endregion




# region Task 9
# Bir Liste İçerisine Random 20 Tane Rakam Ekleyelim Bu Rakamların Liste İçerisinde Geçme Sıklığını Bulun Ve Sözlük İçerisinde Çıktı Verin.

from random import randint

# 1.YOL
def create_random_number(numbers: list) -> list:

    for i in range(20):
        numbers.append(randint(a=0, b=10))
    return numbers

def frequncay_counter(numbers: list) -> dict:
    freq_count = {}
    for number in numbers:
        if number in freq_count:
            freq_count[number] += 1
        else:
            freq_count[number] = 1
    return freq_count

def output_freq(frequncy_dict: dict) -> None:
    for key, value in frequncy_dict.items():
        print(f'{key} : {value}')

def main():
    rakamlar = []
    rakamlar = create_random_number(rakamlar)
    freq_count = frequncay_counter(rakamlar)
    output_freq(freq_count)

main()

# 2.YOL

from random import randint
from collections import Counter

def create_random_number(numbers: list) -> list:
    for i in range(10):
        numbers.append(randint(1, 10))
    return numbers

def siklik_bul(liste: list) -> None:
    siklik = Counter(liste)
    for item , value in siklik.items():
        print(f'{item} Rakamı {value} Kere Tekrar  Edilmştir.')

def main():
    numbers = []
    araba = create_random_number(numbers)
    siklik_bul(araba)
    print(araba)

main()

# endregion




# region Task 10
# örnek input --> Merhaba ben emre emre ben emre
# Bir söz öbeğinde tekrar eden kelimelerden arındırarak çıktı verelim
def remove_duplicate_word(sentence: str) -> None:
    lst = []
    result = ''

    for item in sentence.split(' '):
        if item not in lst:
            lst.append(item)

    result = ' '.join(lst)

    print(result)

remove_duplicate_word('Merhaba ben emre emre ben emre')
# endregion



