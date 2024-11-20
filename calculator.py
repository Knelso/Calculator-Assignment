import operator

# Define available operations
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow
}

def evaluate_expression(num1, op, num2):
    """Evaluate the user's input with error handling."""
    try:
        num1, num2 = float(num1), float(num2)  # Convert inputs to floats
        
        # Check if the operation is valid
        if op not in OPERATIONS:
            return f"Error: Unsupported operation '{op}'"
        
        # Perform the operation
        result = OPERATIONS[op](num1, num2)
        return f"{num1} {op} {num2} = {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please enter valid numbers."
    except Exception as e:
        return f"Unexpected error: {e}"

def calculator():
    """Advanced calculator program."""
    print("Welcome to the Calculator!")
    print("Supported operations: +, -, *, /, %, ^ (power)")
    print("Enter 'quit' to exit the program.\n")
    
    while True:
        # Input numbers and operation
        num1 = input("Enter the first number: ").strip()
        if num1.lower() == 'quit':
            print("Goodbye!")
            break
        
        op = input("Enter the operation (+, -, *, /, %, ^): ").strip()
        if op.lower() == 'quit':
            print("Goodbye!")
            break
        
        num2 = input("Enter the second number: ").strip()
        if num2.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Evaluate the expression and print the result
        result = evaluate_expression(num1, op, num2)
        print(result + "\n")

# Run the calculator program
if __name__ == "__main__":
    calculator()
