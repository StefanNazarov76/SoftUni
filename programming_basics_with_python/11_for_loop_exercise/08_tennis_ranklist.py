from math import floor

games_count = int(input())
initial_points = int(input())

W = 0
F = 0
SF = 0

for _ in range(games_count):
    current_game = input()
    if current_game == 'W':
        W += 1
    elif current_game == 'F':
        F += 1
    elif current_game == 'SF':
        SF += 1

total_points = initial_points + (W * 2000) + (F * 1200) + (SF * 720)
average_points = (total_points - initial_points) / games_count
wins_percentage = (W / games_count) * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{wins_percentage:.2f}%')
