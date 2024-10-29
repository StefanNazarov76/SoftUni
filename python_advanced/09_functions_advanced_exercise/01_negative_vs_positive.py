def negative_and_positive_numbers(nums):
    positive_sum = 0
    negative_sum = 0

    for num in nums:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    print(negative_sum)
    print(positive_sum)

    if positive_sum > abs(negative_sum):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = [int(num) for num in input().split()]

negative_and_positive_numbers(numbers)
