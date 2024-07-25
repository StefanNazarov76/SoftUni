n = int(input())

even_i_sum = 0
odd_i_sum = 0
diff = False
max_diff = 0

for i in range(1, n + 1):
    first_number = int(input())
    second_number = int(input())

    if i == 1:
        even_i_sum += first_number + second_number
        odd_i_sum += first_number + second_number
    elif i % 2 == 0:
        even_i_sum = first_number + second_number
    else:
        odd_i_sum = first_number + second_number

    if even_i_sum != odd_i_sum:
        diff = True

        if max_diff < abs(even_i_sum - odd_i_sum):
            max_diff = abs(even_i_sum - odd_i_sum)

if diff:
    print(f'No, maxdiff={max_diff}')
else:
    print(f'Yes, value={even_i_sum}')
