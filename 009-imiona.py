meskie = ['Artur' , 'Adam' , 'Andrzej']
damskie = ['Monika' , 'Natalia', 'Malgorzata']

imie = input('Podaj imie: ')

if imie.endswith('a'):
    print('Imie zenskie')
    if imie in damskie:
        print(imie+' znajduje sie juz na liscie imion')
    else:
        damskie.append(imie)
        print(imie+' dodane do listy imion')
        print(damskie)
else:
    print('imie meskie')