import random
import string
from random import randint


def pass_generator(get_power):
    if get_power == 1:
        words = ['asf', 'ret', 'erD', 'FDd', 'GRT', 'gDf']
        password = [random.choice(words) for _ in range(randint(1, 2))]

    elif get_power == 2:
        password = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(6)]

    else:
        password = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12)]

    return ''.join(password)


input_power = input("Get password power from 1 to 3: \n")
print(pass_generator(input_power))
