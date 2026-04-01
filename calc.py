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

print(compute(10, '+', 5))
print(compute(10, '-', 5))
print(compute(10, '*', 5))
print(compute(10, '/', 5))