from random import randint

while True:
    # computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    number = randint(1, 3)
    if number == 1:
        computer_choice = 'Rock'
    elif number == 2:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'

    user_choice = input('Choice Rock Or Paper Or Scissors Or Other For Exit: ').strip().title()
    print(f'Computer Choice: {computer_choice}')

    if user_choice == 'Rock' and computer_choice == 'Rock': print('Equal...')
    elif user_choice == 'Rock' and computer_choice == 'Paper': print('You Lose')
    elif user_choice == 'Rock' and computer_choice == 'Scissors': print('You Win')

    elif user_choice == 'Paper' and computer_choice == 'Rock': print('You Win')
    elif user_choice == 'Paper' and computer_choice == 'Paper': print('Equal...')
    elif user_choice == 'Paper' and computer_choice == 'Scissors': print('You Lose')

    elif user_choice == 'Scissors' and computer_choice == 'Rock': print('You Lose')
    elif user_choice == 'Scissors' and computer_choice == 'Paper': print('You Win')
    elif user_choice == 'Scissors' and computer_choice == 'Scissors': print('Equal...')

    else:
        print('Good By')
        break




