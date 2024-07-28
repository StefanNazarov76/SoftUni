men_count = int(input())
woman_count = int(input())
tables = int(input())

current_tables = 0

for men in range(1, men_count + 1):
    for women in range(1, woman_count + 1):
        if current_tables == tables:
            break
        else:
            print(f'({men} <-> {women})', end=' ')
            current_tables += 1
