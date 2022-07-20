# the list "walks" is already defined
# your code here
walksum = 0
key = 7
for i in walks:
    walksum += int(i['distance'])
print(round(walksum / key))
