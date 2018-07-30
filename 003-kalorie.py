waga = float(input('Podaj swoja wage w kg'))
wzrost = int(input('Podaj swoj wzrost w cm'))
wiek = int(input('Podaj ile masz lat'))
a = int(input('Jesli jestes mezczyzna wprowadz 0, jesli kobieta wcisnij 1'))

if a==0:
    S = 5
else:
    S = -161

print('Wprowadz wspolczynnik Twojej aktywnosci fizycznej')
print('Praca siedzaca, brak aktywnosci\t1.2')
print('Praca niefizyczna, malo aktywny tryb zycia\t1.4')
print('Lekka praca fizyczna, regularne cwiczenia 3-4 razy w tyg. ok.5h\t1.6')
print('Praca fizyczna, regularne cwiczenia ok 7h w tyg\t1.8')
print('Ciezka praca fizyczna i regularne cwiczenia ok7h w tyg\t2.0')

wsp = float(input())

x = 10*waga + 6.25*wzrost - 5*wiek + S
print(x)