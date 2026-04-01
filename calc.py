<<<<<<< HEAD
#  Calculator - FIT3047 Team 123

=======
print('Hello from Dakshesh!')
print('hello Zihao')
>>>>>>> 7f9dcaaadcdec050c86925cc0f12615ca2113d21
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

<<<<<<< HEAD
print(power(2, 3))
=======
print(compute(10, '+', 5))
print(compute(10, '-', 5))
print(compute(10, '*', 5))
print(compute(10, '/', 5))
>>>>>>> 7f9dcaaadcdec050c86925cc0f12615ca2113d21
