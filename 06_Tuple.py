
# region Tuple (Demetler) ;

# Listler gibi benzer bir mantığa sahiptirler yani listelerdeki index mantığı tuplelerde de geçerlidir.
# Lakin Tupleler , listler gibi built -in fonksiyonlara sahip değildir. (append , insert , pop vb.)
# Hem Listlerde hemde tuple da ortak olan bir husus dilimlemedir (slicing)



# region Task 1
tuple_1 = ('Galatasaray', 'Beşiktaş', 'Trabzonspor', 'Fenerbahçe')
tuple_2 = ('12', '35.5', '3', ' b', 'Eagels', 'Patrioyt', 'Red Skins')
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
#endregion



# region Task 2

tuple_3 = ('Galatasaray', 'Beşiktaş', 'Trabzonspor', 'Fenerbahçe', '12', '35.5', '3', ' b', 'Eagels', 'Patrioyt', 'Red Skins')

print(tuple_3[0:3])        #   ('Galatasaray', 'Beşiktaş', 'Trabzonspor')
print(tuple_3[2:4])        #   ('Trabzonspor', 'Fenerbahçe')
print(tuple_3[::2])        #   ('Galatasaray', 'Trabzonspor', '12', '3', 'Eagels', 'Red Skins')
print(tuple_3[-1])         #   Red Skins SON
print(tuple_3[-2])         #   Patrioyt SONDAN 2.
print(tuple_3[3::2])       #  ('Fenerbahçe', '35.5', ' b', 'Patrioyt')
print(tuple_3[::-1])       #  ('Red Skins', 'Patrioyt', 'Eagels', ' b', '3', '35.5', '12', 'Fenerbahçe', 'Trabzonspor', 'Beşiktaş', 'Galatasaray')
print(tuple_3[3::-1])      #  ('Fenerbahçe', 'Trabzonspor', 'Beşiktaş', 'Galatasaray')
print(tuple_3[4::-2])      #  ('12', 'Trabzonspor', 'Galatasaray')
#endregion



# region Task 3

tuple_4 = (
    'Sarıyer',
           ('Suadiye', 'Erenköy'),
           (' Yeniköy', 'Bebek', ('Etiler', 'RNispetiye'))
            )

print(tuple_4[2][1][0])       #  B
#endregion




# region Task 4

my_family = [
    ('Burak yılmaz', '35', 'forvet'),
    ('hakan yılmaz', '38', 'gundi'),
    ('ipek yılmaz', '40', 'nankör')
]

for full_name, age, alias in my_family :
    print(f'Name : {full_name}\n'
          f'AGE  :{age}\n'
          f'Alias : {alias}')
    print()
    print()




#endregion











