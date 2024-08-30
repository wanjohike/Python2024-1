import random
# Generating a radom number
randomNum = random.randint(1, 10)

# asking the user to guess a number in the range of 1 to 10
while True:
    guessNum = input("Guess a number form 1 - 10: ")
    guessNum = int(guessNum)
    if guessNum == "":
        print()
    elif randomNum < guessNum:
        print('Too High! Try again')
    elif randomNum > guessNum:
        print('Too Low! Try again')
    elif randomNum == guessNum:
        print('Congratulations! You guessed the number')
        choice = input('Would you like to continue playing? yes/no')
        while choice == 'yes':
            True
            if choice == 'no':
                print('Thanks for playing')
                break
            elif choice != 'yes' or choice !='no':
                print(choice)


