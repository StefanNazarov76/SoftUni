actor_name = input()
points_from_academy = float(input())
jury_count = int(input())

total_points = points_from_academy

for _ in range(jury_count):
    jury_name = input()
    points_from_jury = float(input())
    total_points += points_from_jury * (len(jury_name)) / 2

    if total_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    diff = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
