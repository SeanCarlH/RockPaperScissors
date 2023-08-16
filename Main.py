import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Let's play Rock, Paper, Scissors!\n")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n\n"))
min = 0
max = 2
computer_choice = random.randint(min, max)

if player_choice == 0:
    print("\nPlayer's Choice:\n")
    print(rock + "\n")
    print("Computer's Choice:\n")
    if computer_choice == 0:
        print(rock)
        print("\n\nDraw")
    elif computer_choice == 1:
        print(paper)
        print("\n\nYou Lose :(")
    else:
        print(scissors)
        print("\n\nYou Win!")

if player_choice == 1:
    print("\nPlayer's Choice:\n")
    print(paper + "\n")
    print("Computer's Choice:\n")
    if computer_choice == 0:
        print(rock)
        print("\n\nYou Win!")
    elif computer_choice == 1:
        print(paper)
        print("\n\nDraw")
    else:
        print(scissors)
        print("\n\nYou Lose :(")

if player_choice == 2:
    print("\nPlayer's Choice:\n")
    print(scissors + "\n")
    print("Computer's Choice:\n")
    if computer_choice == 0:
        print(rock)
        print("\n\nYou Lose :(")
    elif computer_choice == 1:
        print(paper)
        print("\n\nYou Win!")
    else:
        print(scissors)
        print("\n\nDraw")