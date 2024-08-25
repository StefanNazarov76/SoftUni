notes = [0] * 10
command = input().split('-')

while command[0] != 'End':
    priority = int(command[0]) - 1
    note = command[1]

    notes.pop(priority)
    notes.insert(priority, note)

    command = input().split('-')

result = [note for note in notes if note != 0]
print(result)
