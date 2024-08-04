
# region File I/O Introduction

# Dosya yaratma, açma ve içerisinde ki değerleri okuma, yazma, güncelleme ve silme işlemleri yapıyoruz.
# Sonuç olarak dosya üzerinden CRUD operasyonlarını yapıyoruz.

# Python'da dosya açmak için kullanılan modlar:

# 'r': Okuma modu. Dosya yalnızca okunabilir. Dosya mevcut değilse hata verir.
# 'w': Yazma modu. Dosya yazma için açılır. Dosya zaten varsa, içeriği silinir. Dosya yoksa yeni bir dosya oluşturulur.
# 'a': Ekleme modu. Dosya yazma için açılır. Dosya zaten varsa, içeriğin sonuna yazılır. Dosya yoksa yeni bir dosya oluşturulur.
# 'x': Oluşturma modu. Yeni bir dosya oluşturur ve yazma için açar. Dosya zaten varsa hata verir.
# 'b': Binary (ikili) modu. Dosyayı ikili modda açar (örneğin, rb veya wb).
# 't': Text (metin) modu. Dosyayı metin modunda açar (varsayılan). Örneğin, rt veya wt.
# '+': Güncelleme modu. Dosyayı okuma ve yazma için açar. Örneğin, r+, w+, a+.

# Bu modlar birleştirilerek kullanılabilir. Örneğin:

# 'rb': Dosyayı binary modda okuma için açar.
# 'wb': Dosyayı binary modda yazma için açar.
# 'r+': Dosyayı okuma ve yazma için açar.
# 'w+': Dosyayı yazma ve okuma için açar.
# 'a+': Dosyayı ekleme ve okuma için açar.
# 'xb': Dosyayı binary modda oluşturur ve yazma için açar.

# Dosya Açma
file = open(
    file='new_file.txt',  # yaratılacak dosyanın adı,
    mode='w',  # dosyanın açılma amacını belirtiyoruz. 'w' -> write yani yazma anlamaına gelmektedir
    encoding='utf-8',  # bu argüman vasıtasıylada dosyamıza türkçe karakter desteği veriyoruz
)
file.write('Full Name: Burak Yılmaz\nOccupation: Developer\n')
file.close()


# Yukarıda yaratılan dosya üzerinde yeni bir kayıt ekleyelim
file = open(
    file='new_file.txt',
    mode='a',
    encoding='utf-8',
)
file.write('Programing Language: Python\n')
file.close()


# Dosya içerisinde ki verileri okuyalım
try:
    file = open(
        file='new_file.txt',
        mode='r',
        encoding='utf-8',
    )
    for line in file.readlines():
        print(line)
except FileExistsError:
    print('Dosya bulunamadı')
finally:
    file.close()
# endregion



# region Task 1
# exam_grades.txt dosyasını yaratın
def create_exam_grades(file_name: str) -> None:
    file = open(
        file=f'{file_name}.txt',
        mode='w',
        encoding='utf-8'
    )
    file.close()
# endregion



# region Task 2
# Kullanıcıdan first name, last name, midterm, final, homework bilgilerini alalım.
# exam_grades.txt dosyasına yazalım.
# Aşağıdaki formatta yazalım
# Burak Yılmaz:30,30,30
# exam_grades dosyasını with open yönetmi ile açın
def type_grades(first_name: str, last_name: str, midterm: float, final: float, homework: float):
    with open(
        file='exam_grades.txt',
        mode='a',
        encoding='utf-8'
    ) as file:
        file.write(f'{first_name} {last_name}:{midterm},{final},{homework}\n')

    print(f'Record has been created!')
# endregion



# region Task 3
# aşağıdaki fonksiyona exam_grades.txt içerisinde ki bilgiler row halinde gelencek
# sample row => Burak Yılmaz:30,30,30
# Harf Notunu hesaplayın
# sampla return Burak Yılmaz: AA
def calculate_grades(row: str) -> str:
    values = row.split(':')
    full_name = values[0]
    grades_list = values[1].split(',')

    avg = float(grades_list[0]) * 0.3 + float(grades_list[1]) * 0.6 + float(grades_list[2]) * 0.1

    if 90 <= avg <= 100:
        return f'{full_name}: AA'
    elif 85 <= avg <= 89:
        return f'{full_name}: BA'
    elif 80 <= avg <= 84:
        return f'{full_name}: BB'
    elif 75 <= avg <= 79:
        return f'{full_name}: CB'
    elif 70 <= avg <= 74:
        return f'{full_name}: CC'
    elif 65 <= avg <= 69:
        return f'{full_name}: CD'
    elif 60 <= avg <= 64:
        return f'{full_name}: DC'
    elif 55 <= avg <= 59:
        return f'{full_name}: DD'
    elif 50 <= avg <= 54:
        return f'{full_name}: FD'
    else:
        return f'{full_name}: FF'
# endregion



# region Task 4
# exam_grades.txt dosyasındna verileri satır satır okuyalım
# harf notlarını hesaplatalım ve bir listeye ekleyelim
# ilgil listeyi return edelim
def get_note_to_list() -> list:
    lst = []

    with open(
        file='exam_grades.txt',
        mode='r',
        encoding='utf-8'
    ) as file:
        for row in file:
            grade = calculate_grades(row)
            lst.append(grade)

    return lst
# endregion



# region Task 5
# result.txt dosyası açılarak örpencilerin harf notları yazın
def register_grades(grades_list: list) -> None:
    with open(
        file='result.txt',
        mode='w',
        encoding='utf-8'
    ) as file:
        for item in grades_list:
            file.write(f'{item}\n')

    print('Note has been registered!')
# endregion



# region Task 6
# result.txt dosyasının verilerini ekrana basalım
def read_result():
    with open(
        file='result.txt',
        mode='r',
        encoding='utf-8'
    ) as file:
        for row in file:
            print(row)
# endregion



# region Task 7
def read_exam_grades() -> None:
    with open(
        file='exam_grades.txt',
        mode='r',
        encoding='utf-8'
    ) as file:
        for row in file:
            print(row)
# endregion



# region Task 8
# Menü Oluşturalım
def menu() -> None:
    print(f"""
    Menu
    ==============
    Enter Grades   --> 1
    Calculate Note --> 2
    Read Note      --> 3
    """)
# endregion



def main():
    # Note: Proje ilk kez çalıştıktan sontra aşağıdaki kodu yoruma alın. Yoksa ilk teste girilen bilgiler gider. Bilgilerin gitmesinin sebebi fonksiyonda ki dosya açma modu 'w'
    create_exam_grades(file_name='exam_grades.txt')

    menu()

    while True:
        process = input('Please choose a process upon menu : ')

        match process:
            case '1':
                try:
                    type_grades(
                        input('First Name : '),
                        input('Last Name : '),
                        float(input('Midterm : ')),
                        float(input('Final : ')),
                        float(input('Homework : '))
                    )
                except ValueError:
                    print('Please type all input!')
            case '2':
                read_exam_grades()
            case '3':
                lst = get_note_to_list()
                register_grades(lst)
            case '4':
                read_result()
            case '5':
                print('Application has been closing!')
                break
            case _:
                print('Please choose valid option on menu!')


main()


















