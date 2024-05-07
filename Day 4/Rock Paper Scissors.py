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

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

choice = int(input())

hands = [rock, paper, scissors]

choice_index = hands[choice]

print("You Chose:")

print(choice_index)

print("Computer chose:")

computer_random = random.randint(0, 2)

computer_choice = hands[computer_random]

print(computer_choice)

if choice == computer_choice:
    print("Draw!")
elif choice == 0 and computer_random == 2:
    print("You Win!")
elif choice == 0 and computer_random == 1:
    print("You Lose!")
elif choice == 1 and computer_random == 0:
    print("You Win!")
elif choice == 1 and computer_random == 2:
    print("You Lose!")
elif choice == 2 and computer_random == 0:
    print("You Lose!")
elif choice == 2 and computer_random == 1:
    print("You Win!")
else: print("womp womp")

print(choice)
print(computer_random)