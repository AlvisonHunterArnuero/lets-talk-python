from basic_operations import sum, substract, multiply, division
from box import boxed_menu
import os

operations_lst = ["Add","Substract", "Multiply","Divide", "Exit"]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def clear_screen():
    input('Press any key to continue...')
    clear()
    boxed_menu(operations_lst, "Python Calculator")

def error_handler(text, error=''):
    print(f'{text}\n{error}')
    clear_screen()

boxed_menu(operations_lst, "Python Calculator")
while True:
    try:
        user_input = int(input('-> '))

        # User select exit option
        if (user_input == 5):
            print('You decided to leave, Good bye for now!')
            break

        if (user_input > 5 or user_input < 1):
            print('Sorry, you selected an invalid option...')
            clear_screen()
            continue

        number1 = int(input('Please type first number: \n-> '))
        number2 = int(input('Please type second number: \n-> '))

        match user_input:
            case 1:
                print(f'Result: {sum(number1, number2)}')
                clear_screen()
            case 2:
                print(f'Result: {substract(number1, number2)}')
                clear_screen()
            case 3:
                print(f'Result: {multiply(number1, number2)}')
                clear_screen()
            case 4:
                print(f'Result: {division(number1, number2)}')
                clear_screen()
            case _:
                print("Sorry, you selected an invalid option...")

    except ValueError as error:
        error_handler('Sorry, you selected an invalid option', error)
        continue
    except KeyboardInterrupt:
        error_handler('This command is not allowed')
        continue
