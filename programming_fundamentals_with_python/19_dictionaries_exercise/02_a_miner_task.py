string = input()

resources = {}

while string != 'stop':
    resource = string
    quantity = int(input())

    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity

    string = input()

for resource in resources:
    print(f'{resource} -> {resources[resource]}')
