from art import logo, vs
from random import choice
from game_data import data as celebrities
from os import system


def play_game(current_celebrities, current_score):

    def select_celebrities(comp_celebrities):
        """selects celebrities from the data and assign them to a list. switches A ve B too"""
        celebrity_A = celebrity_B = comp_celebrities[1]

        while celebrity_A == celebrity_B:
            celebrity_B = choice(celebrities)

        return [celebrity_A, celebrity_B]

    def print_celebrity(celebrity):
        """prints the celebrity description"""
        first_let_desc = celebrity['description'][0].lower()
        a_or_an = ''

        if first_let_desc in ('a', 'e', 'i', 'o', 'u'):
            a_or_an = 'an'
        else:
            a_or_an = 'a'

        print(
            f"{celebrity['name']}, {a_or_an} {celebrity['description']}, from {celebrity['country']}."
        )

    def compare_celebrities(celebrities):
        """compares the celebrities and prints the winner"""
        cel_A_followers = celebrities[0]['follower_count']
        cel_B_followers = celebrities[1]['follower_count']
        if cel_A_followers > cel_B_followers:
            return 'A'
        elif cel_A_followers < cel_B_followers:
            return 'B'
        else:
            return 'B'

    current_celebrities = select_celebrities(current_celebrities)
    user_guess = ''

    print_celebrity(current_celebrities[0])
    print(vs, '\n')
    print_celebrity(current_celebrities[1])

    while user_guess != 'A' and user_guess != 'B':
        user_guess = input(
            "Who has more followers? Please type 'A' or 'B': ").upper()

    if user_guess == compare_celebrities(current_celebrities):
        system('clear')
        print(logo)
        current_score += 1
        print(f"You're right! Current score: {current_score}.")
        play_game(current_celebrities, current_score)
    else:
        system('clear')
        print(f"Sorry, that's wrong. Final score: {current_score}")
        exit()


comparing_celebrities = [choice(celebrities), choice(celebrities)]
score = 0

print(logo)

play_game(comparing_celebrities, score)
