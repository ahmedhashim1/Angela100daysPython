from art import logo


# Calculator
# Addition
def add(n1, n2):
    return n1 + n2


# subtract
def sub(n1, n2):
    return n1 - n2


# multiply
def mul(n1, n2):
    return n1 * n2


# divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)
    num1 = float(input("Please enter 1st number: "))
    for op in operations:
        print(op)

    should_continue = True
    while should_continue:
        op_sympbol = input("Which operation you want to perform from above:")
        num2 = float(input("Please enter 2nd number: "))
        calc_function = operations[op_sympbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {op_sympbol} {num2} = {answer}")

        user_resp = input(f"Type 'y' to continue calcuation with {answer}, or type 'n' to start fresh calculation")

        if user_resp.casefold() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
