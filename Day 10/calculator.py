from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation_dictionary = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide
}

def calculator():
    is_accumulating = True
    n1 = float(input("What's the first number?: "))
    while is_accumulating:
        for symbol in calculation_dictionary:
            print(symbol)
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = calculation_dictionary[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        calculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if calculate_again == "y":
            n1 = result
        else:
            is_accumulating = False
            print("\n" * 20)
            calculator()

calculator()
