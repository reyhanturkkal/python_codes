import random

rock_paper_scissors = [
    ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''],
    ['''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''],
    ['''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

comp_choice = random.randint(0, 2)

print(f"{rock_paper_scissors[user_choice][0]}\n")
print(f"Computer chose:\n {rock_paper_scissors[comp_choice][0]}\n")

if user_choice == comp_choice:
    print("It's a draw")
else:
    if user_choice == 0:
        if comp_choice == 1:
            print("You lose")
        elif comp_choice == 2:
            print("You win!")
    elif user_choice == 1:
        if comp_choice == 0:
            print("You win!")
        elif comp_choice == 2:
            print("You lose")
    elif user_choice == 2:
        if comp_choice == 0:
            print("You lose")
    elif comp_choice == 1:
        print("You win!")
    else:
        print("Please enter a valid number (0,1,2)")
