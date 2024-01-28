from random import randint
end = False
while not end:
    i = 1
    while True:
        check_exit = input(f'Click Enter To Roll The Dice Or Exit... ({i})').title()
        if check_exit == 'Exit':
            end = True
        dice_number = randint(1, 6)
        print(f'Number is {dice_number}')
        if dice_number != 6:
            break
        else:
            print('You won a prize...')
            i += 1
