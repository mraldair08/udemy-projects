import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = True
    print(art.logo)
    value1 = float(input("Enter the first number:\n"))

    while should_continue:
        
        for symbol in operations:
            print(symbol)
            
        operator = input("Enter the type of operation:\n")
        value2 = float(input("Enter the second number:\n"))
        total = operations[operator](value1, value2)
        
        print(f"{value1} {operator} {value2} = {total}")

        next_operation = input(f"Would you like to make another operation with the result {total}? Type 'Yes' or 'No': ").lower()
        
        if next_operation == "yes":
            valor1 = total
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
            
calculator()