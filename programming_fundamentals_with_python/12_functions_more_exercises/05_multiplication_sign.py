def multiplication_sign(num1, num2, num3):
    if 0 in [num1, num2, num3]:
        return 'zero'
    elif ((num1 < 0 < num2 and num3 > 0) or (num1 > 0 > num2 and num3 > 0) or
          (num1 > 0 > num3 and num2 > 0) or (num1 < 0 and num2 < 0 and num3 < 0)):
        return 'negative'
    else:
        return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())

sign = multiplication_sign(first_number, second_number, third_number)
print(sign)
