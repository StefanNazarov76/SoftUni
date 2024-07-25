loads_to_transport = int(input())

total_price = 0
microbus = 0
truck = 0
train = 0
total_tons = 0

for _ in range(loads_to_transport):
    tons_of_load = int(input())
    total_tons += tons_of_load

    if tons_of_load <= 3:
        total_price += tons_of_load * 200
        microbus += tons_of_load
    elif tons_of_load <= 11:
        total_price += tons_of_load * 175
        truck += tons_of_load
    else:
        total_price += tons_of_load * 120
        train += tons_of_load

average_price = total_price / total_tons
microbus_percentage = (microbus / total_tons) * 100
truck_percentage = (truck / total_tons) * 100
train_percentage = (train / total_tons) * 100

print(f'{average_price:.2f}')
print(f'{microbus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
