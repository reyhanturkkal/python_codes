from art import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


def exponent(num1, num2):
    return num1**num2


def calc_decision(answer):
    """Asks to user to make decision about calculation ex. continue mevcut suregelen calculation, new calculation or exit the calculator"""
    user_decision = input(
        f"Type 'y' to continue calculting with {answer}, or type 'n' to start a new calculation \n(if none of them to exit type 'e'): "
    ).lower()
    return user_decision


math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "^": exponent
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    symbols = ''

    for symbol in math_operations:
        symbols += (symbol + ' ')

    print(symbols)

    continue_calc = True

    while continue_calc:

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in math_operations:
            print("Chosen operation symbol is not valid")
            continue

        num2 = float(input("What's the next number?: "))

        calculation_func = math_operations[operation_symbol]
        answer = calculation_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_calc_dec = calc_decision(answer)

        if user_calc_dec == 'n':
            continue_calc = False
            calculator()
        elif user_calc_dec == 'y':
            num1 = answer
        elif user_calc_dec == 'e':
            print("Goodbye!")
            return
        else:
            print("Invalid character")
            calc_decision(answer)


calculator()
