# 1
from random import randint
a = [randint(1, 10) for i in range(9)]
b = [randint(1, 10) for i in range(9)]

c = list(set([i for i in a if i in b]))
print(a)
print(b)
print(c)
