season = input()
kms_per_month = float(input())

salary_per_month = 0

if season == "Spring" or season == "Autumn":
    if kms_per_month <= 5000:
        salary_per_month = kms_per_month * 0.75
    elif kms_per_month <= 10000:
        salary_per_month = kms_per_month * 0.95
    elif kms_per_month <= 20000:
        salary_per_month = kms_per_month * 1.45
elif season == "Summer":
    if kms_per_month <= 5000:
        salary_per_month = kms_per_month * 0.9
    elif kms_per_month <= 10000:
        salary_per_month = kms_per_month * 1.1
    elif kms_per_month <= 20000:
        salary_per_month = kms_per_month * 1.45
elif season == "Winter":
    if kms_per_month <= 5000:
        salary_per_month = kms_per_month * 1.05
    elif kms_per_month <= 10000:
        salary_per_month = kms_per_month * 1.25
    elif kms_per_month <= 20000:
        salary_per_month = kms_per_month * 1.45

total_salary = (salary_per_month * 4) * 0.9

print(f"{total_salary:.2f}")
