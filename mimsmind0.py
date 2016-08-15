import random


n = random.randrange(1,1000)
guess = ''
guesscount = 0
print("Let's play the mimdmind0 game")
n_length = len(str(n))

while n != guess:
    try:
        guess = int(input(('Guess a {}-digit number: ').format(n_length)))
        if guess < n:
            print('Try again. Guess a higher number: ')
            guesscount += 1
        elif guess > n:
            print('Try again. Guess a lower number: ')
            guesscount += 1
    except:
        print('Please enter a number')

if guess == n:
    guesscount += 1
    print(('Congratulations. You guessed the correct number in {} tries.').format(guesscount))