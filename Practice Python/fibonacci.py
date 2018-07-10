def my_fibonacci(user_input):
    i = 0
    n = [1, 1]
    while i < user_input:
        i += 1
        result = n[i] + n[i - 1]
        n.append(result)
    return n


number = int(input("How many Fibonnaci numbers to generate: "))
print(my_fibonacci(number))
