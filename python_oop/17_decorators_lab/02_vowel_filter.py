def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [letter for letter in result if letter.lower() in 'aeiou']

    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']


print(get_letters())
