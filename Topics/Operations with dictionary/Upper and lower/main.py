# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
key_dict = dict.fromkeys(some_iterable)
new_dict = {key.upper(): key.lower() for (key, value) in
            key_dict.items()}
print(new_dict)  # {'Earth': 7917.53, 'Mars': 4212.29}
