import random

a = 1
b = 5
guess = False
count = 0

def random_number():
  number = random.randint(a, b)
  return number

while(guess == False):
  num = random_number()
  user_num = int(input("Guess the number from 1 to 5: "))

  if(num == user_num):
    print("You win!")
    guess = True
  else:
    print("Try again")
    count += 1
    print("Number of trials: {}".format(count))




