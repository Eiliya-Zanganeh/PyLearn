from random import randint

i = 1
computer_number = randint(0, 100)

while True:
    user_number = int(input(f'Please Enter Number ({i}) : '))
    i += 1

    if user_number < computer_number:
        print('Go Up 👆')

    elif user_number > computer_number:
        print('Go Down 👇')

    elif user_number == computer_number:
        print('You Win 👏')