from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# gen list 1
list_1 = []
for elem in range(0, 9):
    elem = randint(0, 9)
    list_1.append(elem)

# gen list 2
list_2 = []
for elem in range(0, 9):
    elem = randint(0, 9)
    list_2.append(elem)

print(list_1)
print(list_2)

ov_list = []
for i in list_1:
    if i in list_2:
        ov_list.append(i)

print(ov_list)
print(set([aa for aa in list_1 if aa in list_2]))


