electrons = int(input())

shells = []

for current_shell in range(1, electrons + 1):
    maximum_electrons_for_current_shell = 2 * current_shell ** 2

    if maximum_electrons_for_current_shell <= electrons:
        shells.append(maximum_electrons_for_current_shell)
        electrons -= maximum_electrons_for_current_shell
        if electrons == 0:
            break
    else:
        shells.append(electrons)
        break

print(shells)
