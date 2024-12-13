with open('example1.txt', 'r') as f:
    lines = f.readlines()

list1 = []
list2 = []

for line in lines:

    a, b = line.split()

    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

res = 0
res2 = 0

for i in range(len(list1)):
    res += abs(list1[i] - list2[i])
    res2 += list1[i] * list2.count(list1[i])

print('Part 1:', res)
print('Part 2:', res2)