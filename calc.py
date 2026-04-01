#  Calculator - FIT3047 Team 123

def compute(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('unknown operator!')
        return None
# Power function
def power(num1, num2):
    return num1 ** num2

print(power(2, 3))