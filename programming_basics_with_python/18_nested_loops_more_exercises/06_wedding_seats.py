last_sector = ord(input())
rows = int(input())
odd_seats = int(input())

total_seats = 0

for sector in range(65, last_sector + 1):
    for row in range(1, rows + 1):
        extra_seats = odd_seats

        if row % 2 == 0:
            extra_seats += + 2

        for letter in range(97, 97 + extra_seats):
            print(f'{chr(sector)}{row}{chr(letter)}')
            total_seats += 1

    rows += 1

print(total_seats)
