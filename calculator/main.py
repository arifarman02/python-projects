# Simple calculator

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))

operand = input('Enter your operand: ')

if operand == '+':
    result = num1 + num2
    print(result)

if operand == '-':
    result = num1 - num2
    print(result)

if operand == '*':
    result = num1 * num2
    print(result)

if operand == '/':
    result = num1 / num2
    print(result)