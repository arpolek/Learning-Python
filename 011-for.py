for i in range(0, 5):
    print('krok: ', i+1)

names = ['Monika', 'Artur', 'Frodo', 'Bilbo']
for name in names:
    print('Czesc', name)

for i in range(2, 10):
    k=1
    for j in range(1, i-1):
        k = k + j
    print(k)