# Basic Calculator - FIT3047 Team 123

print('Welcome to Team 123 Calculator!')
print('Hello from Dakshesh!')
print('Hello from Zihao!')

num1 = float(input('Enter first number: '))
operator = input('Enter operator (+, -, *, /): ')
num2 = float(input('Enter second number: '))

def compute(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'Error: Cannot divide by zero!'
        return num1 / num2
    else:
        return 'Unknown operator!'

result = compute(num1, operator, num2)
print(f'Result: {num1} {operator} {num2} = {result}')