words = input().split()
palindrome = input()

palindrome_words = [word for word in words if word == word[::-1]]

counter = palindrome_words.count(palindrome)

print(palindrome_words)
print(f'Found palindrome {palindrome_words.count(palindrome)} times')
