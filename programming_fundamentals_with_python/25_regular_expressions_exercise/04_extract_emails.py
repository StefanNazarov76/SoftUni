import re

emails = input()

pattern = r'\b(([a-z][a-z\.\-\_]+)@([a-z][a-z\-]+)(\.[a-z]+)+)\b'
valid_emails = re.findall(pattern, emails)

for email in valid_emails:
    print(email[0])
