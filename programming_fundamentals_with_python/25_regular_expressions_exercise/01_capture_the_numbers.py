import re

input_line = input()

pattern = r'\d+'

while input_line:
    matches = re.findall(pattern, input_line)

    if matches:
        for match in matches:
            print(matches, end=' ')

    input_line = input()
