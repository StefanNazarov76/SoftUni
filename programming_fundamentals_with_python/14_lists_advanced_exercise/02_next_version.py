version = [int(ver) for ver in str(input()).split('.')]

version[-1] += 1

for i in range(len(version) - 1, 0, -1):
    if version[i] > 9:
        version[i] = 0
        version[i - 1] += 1

print('.'.join(str(number) for number in version))
