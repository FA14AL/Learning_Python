import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add, "-":sub, "*":multiply, "/": divide}

#print(operations['*'](4,8))

def calculator():
    print(art.logo)
    number_1 = float(input("What is the first number?:"))
    continue_working = True
    while continue_working :
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation:")
        number_2 = float(input("What is the next number?:"))
        result = (operations[op](number_1,number_2))
        print(f"{number_1} {op} {number_2} = {result}")
        ask = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if ask == "y":
            number_1 = result

        else:
            continue_working = False
            print("\n" * 100)
            calculator()

calculator()