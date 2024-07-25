period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for current_day in range(1, period + 1):
    patients = int(input())

    if current_day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if doctors >= patients:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
