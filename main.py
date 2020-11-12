from random import randint


def get_number():
    num = randint(0, 20)
    return num


def play_again():
    print("Thanks for playing! Would you like to try again?")
    confirm = input("Enter 'Yes', or 'No' to exit: ")
    if confirm.upper() == 'YES':
        main()
    else:
        SystemExit()


def main():
    print('Hello there, welcome to Guess The Number!')
    user_name = input('Please enter player name: ')
    print('')
    print('Nice to meet you, {}'.format(user_name))
    print('Let us begin!...')
    num = get_number()
    print('I am thinking of a number between 1 and 20...')
    print('...')
    print('Can you guess what it is within 5 tries?')
    counter = 0
    while counter < 5:
        counter += 1
        guess = input('Guess #{}: '.format(counter))
        if int(guess) < num:
            print('Too low! Try again.')
        elif int(guess) > num:
            print('Too high! Try again.')
        else:
            print('You got it! Congratulations!')
            play_again()
    if counter == 5:
        print("Oh no! You didn't guess the number in time!")
        play_again()


main()
