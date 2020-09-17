###################################
#_SIMPLE PYTHON CALCULATOR PROGRAM_#
###################################

#################
#Basic Functions#
#################

# ADDITION

def add(x, y):
    return x + y

# SUBTRACTION


def sub(x, y):
    return x - y

# MULTIPLICATION


def mult(x, y):
    return x * y

# DIVISION


def div(x, y):
    return x / y

# EXPONENT


def expo(x, y):
    return x ** y


print('Hi there, welcome to your calcaulator')
print()
print('You have the option of: ')
print('A. - Addition')
print('B. - Subtraction')
print('C. - Multiplication')
print('D. - Division')
print('E. - Exponentiation')
print()

# Loop forever until break
while True:
    user_selection = input('Please enter a selection (A, S, M, D, E): ')

    choice = user_selection.upper()

    if choice in ('A', 'S', 'M', 'D', 'E'):
        num_1 = float(input('Please input first number: '))
        num_2 = float(input('Please input second number: '))

        if choice == 'A':
            result = add(num_1, num_2)
            print('The result is: ' + str(result))

        elif choice == 'S':
            result = sub(num1_num_2)
            print('The result is: ' + str(result))

        elif choice == 'M':
            result = mult(num1_num_2)
            print('The result is: ' + str(result))

        elif choice == 'D':
            result = div(num1_num_2)
            print('The result is: ' + str(result))

        elif choice == 'E':
            result = expo(num1_num_2)
            print('The result is: ' + str(result))
        break

    else:
        print('Invalid Input')
