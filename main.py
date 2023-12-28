import os
from art import logo

#Addition
def add(n1, n2):
  return n1 + n2

#Substraction
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Division
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract, 
  "*": multiply,
  "/": divide,
}
def calculator():
  os.system("clear")
  print(logo)
  num1 = int(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What is the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculating. ") == 'y':
      num1 = answer
    else:
      calculator()

calculator()