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

#Write your code below this line 👇
# 0=rock, 1=paper, 2=scissors
choices = [rock, paper, scissors]

comp_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))

if user_choice <= 0 or user_choice > 3:
  print("You chose an invalid number")
else:
  print(f"Computer\'s choice:\n {choices[comp_choice]}")
  print(f"Your choice:\n {choices[user_choice]}")

  if comp_choice == user_choice:
    print("Computer also chose the same. It\'s a tie!")
  elif comp_choice==0 and user_choice==1:
    print("Computer chose Rock! You Win!")
  elif comp_choice==0 and user_choice==2:
    print("Computer chose Rock! You lose!")
  elif comp_choice==1 and user_choice==0:
    print("Computer chose Paper! You lose!")
  elif comp_choice==1 and user_choice==2:
    print("Computer chose Paper! You Win!")
  elif comp_choice==2 and user_choice==0:
    print("Computer chose Scissors! You Win!")
  elif comp_choice==2 and user_choice==1:
    print("Computer chose Scissors! You lose!")
