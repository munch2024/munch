# Ryan Parker
# Task 2.2 Code Snippet

"""
Rock, Paper, Scissors Game

- This script allows the user to play a game of Rock, Paper, Scissors against the computer.
- The user selects their weapon (Rock, Paper, or Scissors) through the terminal, and the computer randomly selects its weapon.
- The winner is determined based on the standard Rock, Paper, Scissors rules.
- After each round, the user is prompted if they want to play again.

How to Use:
1. Run the script in a Python environment.
2. Follow the prompts in the terminal to select your weapon (R for Rock, P for Paper, S for Scissors).
3. The computer will randomly select its weapon.
4. The winner will be announced, and you will be prompted if you wish to play again.

"""

import random

def check_play_status():
    """
    Check if the user wants to play again.

    Returns:
    bool: True if the user wants to play again, False otherwise.
    """
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)


def play_rps():
    """
    Play a game of Rock, Paper, Scissors.
    """
    play = True
    while play:
        print('\nRock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon [R]ock], [P]aper, or [S]cissors: ').upper()

        if user_choice not in ['R', 'P', 'S']:
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        print(f'You chose: {user_choice}')

        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print(f'I chose: {opp_choice}')

        if opp_choice == user_choice:
            print('Tie!')
            play = check_play_status()
        elif (opp_choice == 'R' and user_choice == 'S') or \
            (opp_choice == 'S' and user_choice == 'P') or \
            (opp_choice == 'P' and user_choice == 'R'):
            print(f'{opp_choice} beats {user_choice}, I win!')
            play = check_play_status()
        else:
            print('You win!')
            play = check_play_status()

if __name__ == '__main__':
    play_rps()