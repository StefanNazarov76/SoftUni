countries = input().split(', ')
capitals = input().split(', ')


countries_and_capitals = {country:capital for (country, capital) in zip(countries, capitals)}

for country in countries_and_capitals:
    print(f'{country} -> {countries_and_capitals[country]}')
