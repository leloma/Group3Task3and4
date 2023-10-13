# Function to perform the operation based on the operator
def apply_op(op, b, a):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

# Function to evaluate the expression using operator precedence parsing
def evaluate_expression(tokens):
    values = []
    ops = []

    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token in ['+', '-', '*', '/']:
            while len(ops) > 0 and precedence(ops[-1]) >= precedence(token):
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(apply_op(op, b, a))
            ops.append(token)

    while len(ops) > 0:
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(apply_op(op, b, a))

    return values[0]

# Function to get the precedence of operators
def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

# Input the expression
expression = input("Enter the expression: ")
tokens = expression.split()

# Evaluate the expression using operator precedence parsing
result = evaluate_expression(tokens)
print(f"Result: {result}")
