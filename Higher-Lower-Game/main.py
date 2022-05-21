import random
from game_data import data
import art
from replit import clear

guess_A = {}
guess_B = {}
score = 0
should_continue = True

def choices():
  clear()
  global guess_A
  global guess_B
  if bool(guess_A):
    guess_A = guess_B
  else:  
    guess_A = random.choice(data)
  print(art.logo)
  if score > 0:
    print(f"You're right! Current score: {score}")
  print(f"Compare A: {guess_A['name']}, a {guess_A['description']}, from {guess_A['country']}.")
  print(art.vs)
  guess_B = random.choice(data)
  print(f"Against B: {guess_B['name']}, a {guess_B['description']}, from {guess_B['country']}.")
  if guess_A['follower_count'] > guess_B['follower_count']:
    return 'A'
  else:
    return 'B'

while should_continue:
  answer = choices()
  user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  if answer == user_guess:
    score += 1
  else:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong! Final score: {score}")
    should_continue = False
