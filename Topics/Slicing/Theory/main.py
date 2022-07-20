#  You can experiment here, it won’t be checked

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[1::2])
print(nums[::-2])
print(nums[2::1])
print(nums[::2])
print(nums[1::])

numbers = [3, 2, 5, 4, 1]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

# Invoking sorted(list)
numbers = [3, 2, 5, 4, 1]
print(sorted(numbers))  # [1, 2, 3, 4, 5]
print(numbers.sort()) # None