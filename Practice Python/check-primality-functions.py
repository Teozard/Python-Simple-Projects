def get_number(prompt):
    return int(input(prompt))


def check_num(num):
    if num == 1:
        prime = False
    elif num == 2:
        prime = True
    else:
        prime = True
        for check_number in range(2, int((num / 2) + 1)):
            if num % check_number == 0:
                prime = False
                break
    if prime:
        descriptor = ""
    else:
        descriptor = "not "

    print(num, " is ", descriptor, "prime.", sep="", end="\n\n")


check_num(get_number("Enter a number to check. Ctl-C to exit. "))
