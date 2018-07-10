# 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# 2
new_a = []
for i in a:
    if i < 5:
        new_a.append(i)

print(new_a)

# 3
print([aa for aa in a if aa < 5])

# 4
us_input = int(input("Enter value: "))
for i in a:
    if i < us_input:
        print(i)