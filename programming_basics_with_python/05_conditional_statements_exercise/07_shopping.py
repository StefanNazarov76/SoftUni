budget = float(input())
gpus_count = int(input())
cpus_count = int(input())
ram_count = int(input())

total_gpus_price = gpus_count * 250
total_cpus_price = cpus_count * (total_gpus_price * 0.35)
total_ram_count = ram_count * (total_gpus_price * 0.10)
total_price = total_gpus_price + total_cpus_price + total_ram_count

if gpus_count > cpus_count:
    total_price *= 0.85

diff = abs(total_price - budget)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
