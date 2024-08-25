text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

text_without_vowels = [char for char in text if char.lower() not in vowels]
print(''.join(text_without_vowels))
