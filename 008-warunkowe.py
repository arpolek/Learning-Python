a = int(input('Podaj pierwsza liczbe'))
b = int(input('Podaj druga liczbe'))
c = int(input('Podaj trzecia liczbe'))

print('Nie sprawdzamy przypadku gdy liczby sa sobie rowne')

if a > b and a > c:
    print('Pierwsza liczba jest najwieksza')
else:
    if b > c:
        print('Druga liczba jest najwieksza')
    else:
        print('Trzecia liczba jest najwieksza')


