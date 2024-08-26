data = input().split()
command = input().split()

while command[0] != '3:1':
    if command[0] == 'merge':
        start = int(command[1])
        end = int(command[2])

        if start < 0:
            start = 0

        if end > len(data):
            end = len(data)

        merged_element = ''.join(data[start:end + 1])
        data[start:end + 1] = [merged_element]

    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        element = data[index]

        substring_length = len(element) // partitions
        divided_partition = []

        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(
                    element[current_element_index * substring_length:(current_element_index + 1) * substring_length])
            else:
                divided_partition.append(element[current_element_index * substring_length:])

        data[index:index + 1] = divided_partition

    command = input().split()

print(*data)
