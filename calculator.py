def calculator():
#firstly we define our operators with def and gave them names
    def add(n1,n2):
        return n1 + n2
    def subtract(n1,n2):
        return n1 - n2
    def multiply(n1,n2):
        return n1 * n2
    def divide(n1,n2):
        return n1 / n2
    def exponential_numbers(n1,n2):
        return n1 ** n2
#we define operations on dict. and we call them after.
    operations = {
        "+": add,
        "-": subtract,
        "*":  multiply,
        "/": divide,
        "**": exponential_numbers,
    }
    num1= float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    #we use while because we want  continue our process and do more mathematical operations
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2=float(input("What's the next number?: "))
        calculation_function= operations[operation_symbol]
        answer= calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':

            num1 = answer
            #We are use if here for stop our operations or continue
        else:
            should_continue = False


calculator()

