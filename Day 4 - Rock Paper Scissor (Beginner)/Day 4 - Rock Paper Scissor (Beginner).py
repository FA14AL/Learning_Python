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

options = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors."))
print(f"the user choice is:{user_choice}")
print(options[user_choice])
computer_choice = random.randint(0,2)
print(f"the computer choice is {computer_choice}:")
print(options[computer_choice])

if user_choice >= 3 or user_choice<0:
    print("the user choice is invalid")
elif user_choice == 0 and computer_choice==2:
    print("You Win")
elif user_choice == 2 and computer_choice==0:
    print("You take a big L")
elif user_choice>computer_choice:
    print("You Win")
elif computer_choice > user_choice:
    print("You take a big L")
elif user_choice==computer_choice:
    print("It is a draw")
