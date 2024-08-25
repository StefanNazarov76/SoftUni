employees_happiness = [int(num) for num in input().split()]
happiness_factor = int(input())

improved_happiness = [happiness * happiness_factor for happiness in employees_happiness]

average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
total_count = len(employees_happiness)

if happy_count >= len(improved_happiness) / 2:
    print(f'Score: {happy_count}/{len(improved_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{len(improved_happiness)}. Employees are not happy!')
