from random import randint


def take_list_loop(a):
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)
    return b


def take_list_comp(a):
    b = []
    [b.append(i) for i in a if i not in b]
    return b


def take_list_set(a):
    b = list(set(a[:]))
    return b


new_list = [randint(1, 11) for _ in range(0, 10)]
print(new_list)

print(take_list_loop(new_list))
print(take_list_set(new_list))
print(take_list_comp(new_list))
