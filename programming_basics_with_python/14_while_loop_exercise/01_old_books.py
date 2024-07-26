book_name = input()
current_book = input()

books_count = 0

while current_book != 'No More Books':
    if current_book == book_name:
        print(f'You checked {books_count} books and found it.')
        break
    books_count += 1
    current_book = input()
else:
    print('The book you search is not here!')
    print(f'You checked {books_count} books.')
