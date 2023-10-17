from art import logo
import random


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)

    attempts = 0
    user_guessed = False

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while difficulty != 'hard' and difficulty != 'easy':
        difficulty = input("Please type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while not user_guessed and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("What's your guess?"))
        if guess_number == random_number:
            print(f"You guessed it! The number was {random_number}.")
            user_guessed = True
        elif guess_number > random_number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        if attempts > 0 and user_guessed == False:
            print("Guess again.")

    if not user_guessed:
        print(
            f"Sorry, you ran out of guesses. The number was {random_number}.")

    play_again = input(
        "Would you like to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")


play_game()