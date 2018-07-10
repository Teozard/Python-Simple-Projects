print('Hint: Enter "x" for exit')
while True:
    user1 = input('Choice Rock(r), Paper(p) or Scissors(s): ')
    user2 = input('Choice Rock(r), Paper(p) or Scissors(s): ')

    if user1 == 'x' or user2 == 'x':
        break
    elif user1 == user2:
        print("DRAW!")
    elif user1 == 'r' and user2 == 'p':
        print('PLAYER 2 WINS')
    elif user1 == 'r' and user2 == 's':
        print('PLAYER 1 WINS')
    elif user1 == 'p' and user2 == 'r':
        print('PLAYER 1 WINS')
    elif user1 == 'p' and user2 == 's':
        print('PLAYER 2 WINS')
    elif user1 == 's' and user2 == 'r':
        print('PLAYER 2 WINS')
    elif user1 == 's' and user2 == 'p':
        print('PLAYER 1 WINS')
