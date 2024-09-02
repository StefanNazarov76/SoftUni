command = input()

force_book = {}

while command != 'Lumpawaroo':
    if ' | ' in command:
        side, user = command.split(' | ')

        if side not in force_book:
            force_book[side] = []

        user_exists = False
        for users in force_book.values():
            if user in users:
                user_exists = True
                break

        if not user_exists:
            force_book[side].append(user)

    else:
        user, side = command.split(' -> ')

        for current_side, users in force_book.items():
            if user in users:
                users.remove(user)
                break

        if side not in force_book:
            force_book[side] = []

        force_book[side].append(user)
        print(f'{user} joins the {side} side!')

    command = input()

for side, users in force_book.items():
    members = len(users)

    if members > 0:
        print(f'Side: {side}, Members: {members}')
        for user in users:
            print(f'! {user}')
