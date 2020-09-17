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

#######################
# Calculator Function #
#######################


def calculate():
    while True:
        print()
        print('You have the option of: ')
        print('A. - Addition')
        print('B. - Subtraction')
        print('C. - Multiplication')
        print('D. - Division')
        print('E. - Exponentiation')
        print()
        user_selection = input('Please enter a selection (A, S, M, D, E): ')

        choice = user_selection.upper()

        if choice in ('A', 'S', 'M', 'D', 'E'):
            num_1 = float(input('Please input first number: '))
            num_2 = float(input('Please input second number: '))
            print()

            if choice == 'A':
                result = add(num_1, num_2)
                print('The result is: ' + str(result))

            elif choice == 'S':
                result = sub(num_1, num_2)
                print('The result is: ' + str(result))

            elif choice == 'M':
                result = mult(num_1, num_2)
                print('The result is: ' + str(result))

            elif choice == 'D':
                result = div(num_1, num_2)
                print('The result is: ' + str(result))

            elif choice == 'E':
                result = expo(num_1, num_2)
                print('The result is: ' + str(result))

        else:
            print()
            print('Invalid Input')


calculate()
