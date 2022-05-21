from replit import clear
clear()
import art
print(art.logo)

bid_dict= {}
end_of_bidding = False
while not end_of_bidding:
  name = input("What is your name?: ")
  bid_value = int(input("What\'s your bid?: $"))
  more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'\n").lower()
  bid_dict[name] = bid_value
  if more_bidders == "yes":
    clear()
    end_of_bidding = False
  else:
    clear()
    end_of_bidding = True

def highest_bidder(bid_dict):
  winning_bid = 0
  winner = ""
  for person in bid_dict:
    if bid_dict[person] > winning_bid:
      winning_bid = bid_dict[person]
      winner = person
  print(f"The winner is {winner} with a bid of {winning_bid}")
  
highest_bidder(bid_dict)

