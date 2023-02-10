# letting computer guess the number
import random

def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            guess = random.randint(1,x)
        else:
            guess = low # high also since it is equal
        feedback = input(f"is {guess}  high(H), low(L) or correct(C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yes, the computer guessed your number {guess} correctly')


computer_guess(5)