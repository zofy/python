import random


def guess_number(randomNum):
    guess = int(raw_input('Try to guess my integer in range (0,99): '))
    if guess < randomNum:
        print('too low')
    elif guess > randomNum:
        print('too high')
    return randomNum == guess


def play():
    num = random.randint(0, 99)
    while not guess_number(num):
        pass
    print('You guessed it!')
    print(num)

play()