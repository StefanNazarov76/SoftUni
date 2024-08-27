distance_to_pokemon = [int(d) for d in input().split()]

result = []

while distance_to_pokemon:
    index = int(input())
    captured_pokemon = ''

    if index < 0:
        captured_pokemon = distance_to_pokemon.pop(0)
        distance_to_pokemon.insert(0, distance_to_pokemon[-1])

    elif index >= len(distance_to_pokemon):
        captured_pokemon = distance_to_pokemon.pop(-1)
        distance_to_pokemon.append(distance_to_pokemon[0])

    if not captured_pokemon:
        captured_pokemon = distance_to_pokemon.pop(index)

    result.append(captured_pokemon)

    for pos, pokemon in enumerate(distance_to_pokemon):
        if pokemon <= captured_pokemon:
            distance_to_pokemon[pos] += captured_pokemon

        else:
            distance_to_pokemon[pos] -= captured_pokemon

print(sum(result))
