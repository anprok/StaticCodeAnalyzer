# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
tiny_dict = {'a': 1, 'b': 2, 'c': 3}

for obj in tiny_dict:
    print(obj)


print(tiny_dict.keys())  # dict_keys(['a', 'b', 'c'])
for obj in tiny_dict.keys():
    print(obj)
for value in tiny_dict.values():
    print(value)

print(tiny_dict.values())
for obj in tiny_dict.items():
    print(obj)
print(tiny_dict.items())