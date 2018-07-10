'''

Create a program that asks the user for a number and then prints out a
list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

x = list(range(2, 11))
print(x)
user = int(input("Submit your number"))

for elem in x:
    if elem % user == 0:
        print(elem)
