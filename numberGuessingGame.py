import random

guessTaken = 0

print('Hello, want to play a game?')
answer = input()
while answer ==('yes'):

    print('please tell me your name.')
    myName = input()
    number = random.randint(1, 20)
    print('well, ' + myName + ', I am thinking of a number between 1 and 20.')
    while guessTaken < 6:
        print('Take a guess ' + myName + '.')
        guess = input()
        guess = int(guess)
        guessTaken = guessTaken + 1

        if guess < number:
            print ('your guess was too low, try again.')

        if guess > number:
            print('your guess was too high, try again.')

        if guess == number:
            break

    if guess == number:
        guessTaken =str(guessTaken)
        print('Good job, ' + myName + ': you guessed my number in ' + guessTaken + ' guesses!')
        break

    if guess != number:
        number = str(number)
        print('Too bad, you did not guess my number. My number was '+ number)
        break

    if answer !=('yes'):
        break
