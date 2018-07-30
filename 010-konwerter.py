cm = float(input('Podaj dlugosc w cm: '))
m = cm / 100
cale = 0.393701
inch = cm*cale

print('{} cm to {} metrow oraz {:.4f} cali'.format(cm, m, inch))
