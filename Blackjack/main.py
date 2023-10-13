from os import system
from art import logo
import random

start_game = True

if (input("Do you want to play game? (y/n) ").lower() == "n"):
    start_game = False
    print("Maybe another day...")

system('clear')

while start_game:

    print(logo)
    print("Welcome to Blackjack!")

    def deal_card():
        """Deal a single card from the deck"""
        card = random.choice(cards)
        return card

    def calculate_score(deck):
        """Sum of the numbers on cards from the deck"""
        score = 0
        for card in deck:
            score += card
        return score

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    comp_deck = [deal_card(), deal_card()]
    player_deck = [deal_card(), deal_card()]
    comp_score = 0
    player_score = 0
    winner = 'Player'

    player_score = calculate_score(player_deck)
    comp_score = calculate_score(comp_deck)

    if player_score != 21 and start_game:
        print(f"Your cards: {player_deck}, current score: {player_score}")
        print(f"Computer's first card: {comp_deck[0]}")

        hit_or_stay = input("Type 'h' to hit, or 's' to stay: ").lower()

        while hit_or_stay != 'h' and hit_or_stay != 's':
            hit_or_stay = input("Please type 'h' or 's' : ")

        if hit_or_stay == 'h':
            while hit_or_stay == 'h':
                player_deck.append(deal_card())
                player_score = calculate_score(player_deck)
                if player_score > 21:
                    winner = 'Computer'
                    break
                else:
                    if player_score != 21:
                        print(
                            f"Your cards: {player_deck}, current score: {player_score}"
                        )
                        print(f"Computer's first card: {comp_deck[0]}")
                        hit_or_stay = input(
                            "Type 'h' to hit, or 's' to stay: ").lower()
                        while hit_or_stay != 'h' and hit_or_stay != 's':
                            hit_or_stay = input("Please type 'h' or 's' : ")
                    else:
                        break
        if hit_or_stay == 's':
            comp_score = calculate_score(comp_deck)
            if comp_score == 21:
                winner = 'Computer'
            else:
                while comp_score < 17:
                    comp_deck.append(deal_card())
                    comp_score = calculate_score(comp_deck)

                if comp_score > 21:
                    winner = 'Player'
                else:
                    if comp_score == player_score:
                        winner = 'Draw'
                    elif comp_score > player_score:
                        winner = 'Computer'

    print(f"\nYour final hand: {player_deck}, final score: {player_score}")
    print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
    if winner == 'Player':
        print("""You won! 😃""")

    if winner == 'Draw':
        print("""It's a draw! 🙃""")

    if winner == 'Computer':
        if player_score > 21:
            print("""You went over. You lose 😭""")
        elif comp_score == 21:
            print("""Lose, opponent has Blackjack 😱""")
        else:
            print("You lost!")
    play_again = input("Do you want to play again? Type 'y' or 'n':")
    while play_again != 'y' and play_again != 'n':
        play_again = input("Please type 'y' or 'n' : ")
    if play_again == 'n':
        start_game = False
    system('clear')
