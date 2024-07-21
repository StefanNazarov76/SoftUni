from math import ceil

movie_name = input()
movie_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4

time_left = break_length - lunch_time - relax_time
diff = abs(movie_length - time_left)

if time_left >= movie_length:
    print(f'You have enough time to watch {movie_name} and left with {ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(diff)} more minutes.")
