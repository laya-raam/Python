###### Guess the number game ############
import replit
from art import logo
import random

replit.clear()
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)
print(f"The answer is {answer}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
  lives = 10
elif level == "hard":
  lives = 5
else:
  print("You have entered a wrong input!")

game_over = False

def guess():
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess < answer:
    print("Too Low.") 
    return False
  elif guess > answer:
    print("Too High.")
    return False
  elif guess == answer:
    print(f"You got it! The answer was {guess}")
    return True

while not game_over and lives > 0:
  game_over = guess()
  lives -= 1
  if not game_over and lives > 0:
    print("Guess again.")
  
if not game_over and lives < 1:
  print("You've run out of guesses. You lose!")
  
