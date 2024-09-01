materials = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_item = None
obtained = False

while not obtained:
    items = input().split()

    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i+1].lower()

        if material not in materials:
            materials[material] = 0
        materials[material] += quantity

        if materials['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            materials['shards'] -= 250
            obtained = True

        elif materials['fragments'] >= 250:
            legendary_item = 'Valanyr'
            materials['fragments'] -= 250
            obtained = True

        elif materials['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            materials['motes'] -= 250
            obtained = True

        if obtained:
            break

print(f'{legendary_item} obtained!')

for material in materials:
    print(f'{material}: {materials[material]}')
