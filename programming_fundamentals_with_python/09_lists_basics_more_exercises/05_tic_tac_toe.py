first_row = input().split()
second_row = input().split()
third_row = input().split()

first_player_won = False
second_player_won = False

# rows
if first_row[0] == first_row[1] == first_row[2] == '1':
    first_player_won = True
elif first_row[0] == first_row[1] == first_row[2] == '2':
    second_player_won = True
elif second_row[0] == second_row[1] == second_row[2] == '1':
    first_player_won = True
elif second_row[0] == second_row[1] == second_row[2] == '2':
    second_player_won = True
elif third_row[0] == third_row[1] == third_row[2] == '1':
    first_player_won = True
elif third_row[0] == third_row[1] == third_row[2] == '2':
    second_player_won = True

# columns
elif first_row[0] == second_row[0] == third_row[0] == '1':
    first_player_won = True
elif first_row[0] == second_row[0] == third_row[0] == '2':
    second_player_won = True
elif first_row[1] == second_row[1] == third_row[1] == '1':
    first_player_won = True
elif first_row[1] == second_row[1] == third_row[1] == '2':
    second_player_won = True
elif first_row[2] == second_row[2] == third_row[2] == '1':
    first_player_won = True
elif first_row[2] == second_row[2] == third_row[2] == '2':
    second_player_won = True

# diagonals
elif first_row[0] == second_row[1] == third_row[2] == '1':
    first_player_won = True
elif first_row[0] == second_row[1] == third_row[2] == '2':
    second_player_won = True
elif first_row[2] == second_row[1] == third_row[0] == '1':
    first_player_won = True
elif first_row[2] == second_row[1] == third_row[0] == '2':
    second_player_won = True

if first_player_won:
    print('First player won')
elif second_player_won:
    print('Second player won')
else:
    print('Draw!')
