from art import logo 

def add(a, b):
  return a+b
def subtract(a, b):
  return a-b
def multiply(a, b):
  return a*b
def divide(a, b):
  return a/b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  should_continue = True
  while should_continue:  
    for operator in operations:
      print(operator)
    op = input("Pick an operation: ")  
    num2 = float(input("What's the next number?: "))
    function = operations[op]
    answer = function(num1, num2)
    print(f"{num1} {op} {num2} = {answer}")
    cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ").lower() 
    if cont == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
