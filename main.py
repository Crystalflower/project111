name = input('Add you name: ')
sur = input('Add you surname: ')
old = float(input('Add you age: '))
weight = float(input('Add you weight: '))


if old >= 30 and old < 40 and (weight <= 50 or weight >= 120):
    print(name, sur, old, 'years old', 'weight ', weight, ' - should take care of yourself')
elif old >= 40 and (weight <= 50 or weight >= 120):
    print(name, sur, old, 'years old', 'weight ', weight, ' - you need to go hospital')
else:
    print(name, sur, old, 'years old', 'weight ', weight, ' - good game')