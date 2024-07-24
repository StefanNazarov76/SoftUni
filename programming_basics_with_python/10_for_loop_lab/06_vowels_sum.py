text = input()

vowels_sum = 0

for letter in text:
    if letter in 'a':
        vowels_sum += 1
    elif letter in 'e':
        vowels_sum += 2
    elif letter in 'i':
        vowels_sum += 3
    elif letter in 'o':
        vowels_sum += 4
    elif letter in 'u':
        vowels_sum += 5

print(vowels_sum)
