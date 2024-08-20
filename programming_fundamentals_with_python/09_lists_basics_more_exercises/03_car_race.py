sequence_of_numbers = input().split()

middle = len(sequence_of_numbers) // 2

left_car_time = 0
right_car_time = 0

for i in range(0, len(sequence_of_numbers)):
    sequence_of_numbers[i] = int(sequence_of_numbers[i])

for left_car_index in range(middle):
    if sequence_of_numbers[left_car_index] == 0:
        left_car_time *= 0.8
    else:
        left_car_time += sequence_of_numbers[left_car_index]

sequence_of_numbers.reverse()
for right_car_index in range(middle):
    if sequence_of_numbers[right_car_index] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += sequence_of_numbers[right_car_index]

if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')
