from collections import deque

gas_stations_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

gas_stations_data_copy = gas_stations_data.copy()
gas_in_tank = 0
index = 0

while gas_stations_data_copy:
    petrol, distance = gas_stations_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        gas_stations_data.rotate(-1)
        gas_stations_data_copy = gas_stations_data.copy()
        index += 1
        gas_in_tank = 0

print(index)
