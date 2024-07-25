username = input()
password = input()
text = input()

while text != password:
    text = input()
else:
    print(f'Welcome {username}!')
