numbers = [int(num) for num in input()]
square_list = [sum(numbers[:x + 1]) for x in range(len(numbers))]
print(square_list)
