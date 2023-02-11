import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}:"))
        if guess > random_number:
            print('sorry, guess again. too high')
        elif guess < random_number:
            print('sorry, guess again. too low')
    print(f'congratulations, you have guessed the number {random_number} correctly')

guess(10)


