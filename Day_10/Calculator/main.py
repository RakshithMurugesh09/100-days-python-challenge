from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1,n2):
    return n1*n2

# print(logo)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def main():
    first_number = float(input("What's the first number?: "))
    while True:
        for symbols in operations:
            print(symbols)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        final_answer = (operations[operation](first_number, second_number))
        print(f"{first_number} {operation} {second_number} = {final_answer}")
        new_start = input(f"Type 'y' to continue calculating with {final_answer}, or type 'n' to start a new calculation: ").lower()
        if new_start == 'y':
            first_number = final_answer
        else:
            break
main()
