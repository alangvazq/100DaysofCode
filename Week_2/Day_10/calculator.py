from art import logo

# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Substract
def substract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}


def calculation():
  print(logo)
  
  num1 = float(input("What's the fist number? "))
  for operation in operations:
    print(operation)
  again = True
  
  while again == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    answer = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    next_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

    if next_operation == "y":
      num1 = answer
    elif next_operation == "n":
      again = False
      calculation()

calculation()