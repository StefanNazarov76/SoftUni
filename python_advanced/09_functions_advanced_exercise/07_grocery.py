def grocery_store(**products):
    products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    result = []
    for name, quantity in products:
        result.append(f'{name}: {quantity}')

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
