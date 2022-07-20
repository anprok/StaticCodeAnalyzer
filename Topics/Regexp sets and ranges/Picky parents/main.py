import re

test = input()

template = '[B-N][aoieu].*'
if re.match(template, test):
    print("Suitable!")