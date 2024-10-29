def age_assignment(*names, **kwargs):
    result = []

    for key, age in kwargs.items():
        for name in names:
            if key in name:
                result.append(f'{name} is {age} years old.')
                break

    return '\n'.join(result)


print(age_assignment('Peter', 'George', G=26, P=19))
