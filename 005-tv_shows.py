tvshows = { 'suits' : 9.5, 'chuck' : 10.0, 'Orange is the new black' : 9.5}
tvshows.keys()
print(tvshows.keys())
print(tvshows.values())
print('Which TV show do you want to watch?')
a = int(input('1 - Suits, 2 - Chuck, 3 - Orange is the new black'))

if a==1:
    print(tvshows['suits'])
else:
    if a==2:
        print(tvshows['chuck'])
    else:
        print(tvshows['Orange is the new black'])

b = input('Please add title of reviewed TV show')
c = float(input('Please add a grade'))
tvshows[b] = c
print(tvshows.keys())
print(tvshows.values())