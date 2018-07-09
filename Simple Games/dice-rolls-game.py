import random

def yourRoll_dice():
  diceOne = random.randint(1, 6)
  diceTwo = random.randint(1, 6)
  diceSum = diceOne + diceTwo
  print("You rolled {} + {} = {}".format(diceOne, diceTwo, diceSum))
  return diceSum


def botRoll_dice():
  diceOne = random.randint(1, 6)
  diceTwo = random.randint(1, 6)
  diceSum = diceOne + diceTwo
  print("Your opponent rolled {} + {} = {}".format(diceOne, diceTwo, diceSum))
  return diceSum

nu1 = yourRoll_dice()
nu2 = botRoll_dice()

if(nu1 > nu2):
  print("You win!")
elif(nu2 > nu1):
  print("You lose!")
else:
  print("Draw!")


