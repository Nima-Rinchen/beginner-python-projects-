def add(a, b):
    result = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(result) )
def sub(a, b):
    result = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(result))
def multiply(a, b):
    result = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(result))
def divide(a, b):
    result = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(result))


while True:

    operation = input('Pick any operation:\na for addition, \ns for subtraction, \nd for division, \nm for multiplication: ').lower()


    if operation == 'a':
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        add(a, b)
    elif operation == 's':
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        sub(a, b)
    elif operation == 'd':
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        divide(a, b)
    elif operation == 'm':
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        multiply(a, b)
    elif operation == 'q':
        quit()
    else:
        print('Wrong input')

