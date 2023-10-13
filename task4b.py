# Function to perform the operation based on the operator
def apply_operator(operator, b, a):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

# Function to evaluate the expression using operator precedence parsing
def evaluate_expression(tokens):
    values = []
    operators = []

    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token in ['+', '-', '*', '/']:
            while len(operators) > 0 and precedence(operators[-1]) >= precedence(token):
                b = values.pop()
                a = values.pop()
                operator = operators.pop()
                values.append(apply_operator(operator, b, a))
            operators.append(token)

    while len(operators) > 0:
        b = values.pop()
        a = values.pop()
        operator = operators.pop()
        values.append(apply_operator(operator, b, a))

    return values[0]

# Function to get the precedence of operator
def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    return 0

# Input the expression
expression = input("Enter the expression: ")
tokens = expression.split()

# Evaluate the expression using operator precedence parsing
result = evaluate_expression(tokens)
print(f"Result: {result}")
