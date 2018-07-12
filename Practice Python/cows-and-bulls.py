from random import randint


def get_randoms(diff):
    rand_nums = [str(randint(1, 4)) for _ in range(diff)]
    return rand_nums


def main():
    print("Welcome to the Cows and Bulls Game!")
    numbers = get_randoms(4)
    count = 0
    while True:
        count += 1

        # to debug
        print(numbers)

        # user prompt
        user_input = input("Enter a number: ")
        user_input_list = [user_input_list for user_input_list in user_input]
        # print(user_input_list)

        # check how many cows and bulls
        cows = [cows for cows, two_lists in zip(numbers, user_input_list) if cows in two_lists]

        # check how many  bulls
        bulls = [item for item in user_input_list if item in numbers]

        for i in cows:
            if i in bulls:
                bulls.remove(i)

        print("{} cows, {} bulls".format(len(cows), len(bulls)))

        if len(cows) == 4:
            print("Tries: {}".format(count))
            again = input("Try again? y/n\n")
            if again == 'y':
                numbers = get_randoms(4)
                continue
            else:
                break


if __name__ == "__main__":
    main()
