str = str(input("Enter any string: "))
rvd = str[::-1]

print(rvd, str)
if str == rvd:
    print("palindrome")
else:
    print('just a string')

