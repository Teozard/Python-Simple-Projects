def reverse_word_order(foo):
    bar = foo.split()
    return " ".join(bar[::-1])


user_line = input("Please enter long sets of string: \n")
print(reverse_word_order(user_line))
