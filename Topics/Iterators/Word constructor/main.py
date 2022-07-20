first_word = input()
second_word = input()
result = ""
for first_char, second_char in zip(first_word, second_word):
    result += first_char + second_char
print(result)
