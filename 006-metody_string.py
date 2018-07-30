firstname = input('What is your name?')
lastname = input('What is your name?')
number = input('What is your number?')

print('Czy imie sklada sie tylko z liter?', firstname.isalpha())
print('Czy nazwisko sklada sie tylko z liter?', lastname.isalpha())
print('Czy numer tel. sklada sie tylko z liczb?',number.isdigit())
firstname = firstname.capitalize()
lastname = lastname.capitalize()
number = number.replace(" ", "").replace("-","")
print(firstname, lastname, number)
print(firstname+lastname+number)
print('Czy imie konczy sie na a?',firstname.endswith('a'))
personal = firstname+lastname+number
print('Dane polaczone w jeden ciag', personal)
print('Dlugosc personal')
print(len(personal))
print('Dlugosc imienia i nazwiska')
letter = len(personal)-9
print(letter)





