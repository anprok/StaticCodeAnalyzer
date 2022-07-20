file = open('data/dataset/input.txt', 'r')
a = file.readlines()
b = a.count("summer")
c = 0
for i in a:
    if i.strip() == 'summer':
        c += 1
print(c)
file.close()
