animals = input().split(', ')
animals.reverse()

if 'wolf' == animals[0]:
    print('Please go away and stop eating my sheep')
else:
    wolf_index = animals.index('wolf')
    print(f'Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!')
