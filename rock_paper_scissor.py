import random

def play():
    user = input('enter any, r for rock, p for paper, s for scissor: ')
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "its a tie"
    elif user not in ('p', 'r', 's'):
        return "wrong input"
    if win_user(user, computer):
        return "You win"

    return " you lose"

def win_user(you, opponent):
    if (you == 'r' and opponent == 's') or (you =='s' and opponent == 'p') or (you == 'p' and opponent == 'r'):
        return True

print(play())