import re

word = input()
print(bool(re.match(r'\bthe\b', word)))