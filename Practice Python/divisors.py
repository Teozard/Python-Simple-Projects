num = int(input("Submit your number: "))
x = list(range(1, num + 1))
new_list = []
for elem in x:
    if elem % num == 0:
        new_list.append(elem)
print(new_list)
