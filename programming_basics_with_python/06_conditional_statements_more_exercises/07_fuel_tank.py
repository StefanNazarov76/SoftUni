fuel_type = input().lower()
litres_in_tank = float(input())


if fuel_type == "diesel":
    if litres_in_tank >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "gasoline":
    if litres_in_tank >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
elif fuel_type == "gas":
    if litres_in_tank >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")
