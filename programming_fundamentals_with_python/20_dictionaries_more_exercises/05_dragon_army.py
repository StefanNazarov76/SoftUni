def check_for_null_values(damage, health, armor):
    if damage is None:
        damage = 45

    if health is None:
        health = 250

    if armor is None:
        armor = 10

    return damage, health, armor


number_of_dragons = int(input())
dragons = {}

for _ in range(number_of_dragons):
    color, name, damage, health, armor = [x if x.isalpha() else int(x) for x in input().split()]

    damage, health, armor = check_for_null_values(damage, health, armor)

    dragons[color] = dragons.get(color, {})
    dragons[color][name] = {'damage': damage, 'health': health, 'armor': armor}


for color in dragons:
    total_dragons_in_color = len(dragons[color])
    avg_damage, avg_health, avg_armor = 0, 0, 0

    for stats in dragons[color].values():
        avg_damage += stats['damage']
        avg_health += stats['health']
        avg_armor += stats['armor']

    avg_damage /= total_dragons_in_color
    avg_health /= total_dragons_in_color
    avg_armor /= total_dragons_in_color

    print(f'{color}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})')
    for name, stats in sorted(dragons[color].items()):
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
