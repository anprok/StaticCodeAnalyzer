i = 0
minimum = ''
while True:
    input_float = input()
    if input_float == '.':
        break
    else:
        if i == 0 or minimum > float(input_float):
            minimum = float(input_float)
        i += 1
print(minimum)