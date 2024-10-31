def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_element = numbers[mid_index]

        if mid_element == target:
            return mid_index
        elif mid_element < target:
            left = mid_index + 1
        elif mid_element > target:
            right = mid_index - 1

    return -1


nums = [int(el) for el in input().split()]
target = int(input())

print(binary_search(nums, target))
