import random


n = random.randrange(1,10)
guess = ''
guesscount = 0
n_length = len(str(n))
maxrounds = (2**n_length) + n_length
bullcount = 0
cowcount = 0


print(("Let's play the mimdmind0 game. You have {} guesses").format(maxrounds))
while (n != guess) and (guesscount < maxrounds):
    notice = ''
    try:
        print(notice)
        guess = int(input(('Guess a {}-digit number: ').format(n_length)))
        guess_str = str(guess)
        guess_str_list = guess_str.split()
        n_str = str(n)
        n_str_list = n_str.split()
        for item_guess in guess_str_list:
            for item_n in n_str_list:
                if item_guess == item_n:
                    bullcount += 1
                    guesscount += 1
        for item_guess in n_str_list:
                cowcount += 1
                guesscount += 1
                print(('{} bull(s), {} cow(s). Try again: ').format(bullcount, cowcount))
    except:
        print('Please enter a number')

if guess == n:
    guesscount += 1
    print(('Congratulations. You guessed the correct number in {} tries.').format(guesscount))
