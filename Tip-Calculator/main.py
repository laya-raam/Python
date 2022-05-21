# The below code is for calculating a Restaurant tip
print("Welcome to the tip calculator")
bill_amt = input("What was the total bill? $")
people = input("How many people to split out the bill? ")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")


tip = (int(tip_percent) / 100) * float(bill_amt)
total = float(bill_amt) + tip

pp_bill = total / int(people)
# print(f"Each person should pay: ${round(pp_bill,2)}")
final = "{:.2f}".format(pp_bill)
print(f"Each person should pay: ${final}")
