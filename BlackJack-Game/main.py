############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

####################################################################
import random
from replit import clear
from art import logo



def blackjack_game():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_card_list = []
  comp_card_list = []
  player_score = 0
  comp_score = 0
  another_card = 'n'

  def hit(list):
    choice = random.choice(cards)
    list.append(choice)
    return int(sum(list))

  def show_cards():
    print(f"Your cards: {player_card_list}, current score: {player_score}")
    print(f"Computer's first card: {comp_card_list[0]}")
  
  def final_print():
    print(f"Your cards: {player_card_list}, current score: {player_score}")
    print(f"Computer's first card: {comp_card_list[0]}")
    print(f"Your final hand: {player_card_list}, final score: {player_score}")
    print(f"Computer's final hand: {comp_card_list}, final score: {comp_score}")
  
  for i in range(2):
    player_score = hit(player_card_list)
    comp_score = hit(comp_card_list)
  continue_game = True

  while continue_game:
    if sum(comp_card_list) == 21 and len(comp_card_list) == 2:
      print("The computer has got the Blackjack! You lose!")
      continue_game = False
    elif sum(player_card_list) == 21 and len(player_card_list) == 2:
      print("You have got the Blackjack! You Win!")
      continue_game = False
    else:
      if player_score > 21:
        if 11 in player_card_list:
          player_card_list.remove(11)
          player_card_list.append(1)
          player_score -= 10
          if player_score > 21:
            final_print()
            print("You went over. You lose. 😭")            
            continue_game = False
          else:
            show_cards()
            another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
        else:
          continue_game = False
      else:
        show_cards()
        another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
        if another_card == 'y':
          player_score = hit(player_card_list)
        else:
          continue_game = False

  while comp_score < 17:
    comp_score = hit(comp_card_list)
    
  if player_score > 21:
    final_print()
    print("You went over. You lose. 😭")
  elif comp_score > 21:
    final_print()
    print("You Win!")
  elif player_score > comp_score:
    final_print()
    print("You are more than the Computer! You Win!")
  elif player_score < comp_score:
    final_print()
    print("You are less than the Computer! You Lose!")
  elif player_score == comp_score:
    final_print()
    print("You draw!")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  blackjack_game()
