import random


# don't modify this code or variable `n` may not be available
n = int(input())
a = -100
b = 100
random.seed(n)
print(random.randint(a, b))
