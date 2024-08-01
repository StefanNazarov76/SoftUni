years = int(input()) + 1

is_year_found = False

while not is_year_found:
    is_year_found = True
    for num in range(len(str(years))):
        if str(years).count(str(years)[num]) != 1:
            years = int(years) + 1
            is_year_found = False
            break

print(years)
