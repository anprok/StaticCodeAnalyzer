import re

word_1 = input()
word_2 = input()
if re.match(word_1, word_2):
    print(len(word_1) * 2)
else:
    print('no matching')