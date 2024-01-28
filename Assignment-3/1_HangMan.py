from random import randint

words = ['computer', 'django', 'python', 'neural network', 'nodejs', 'vuejs', 'laravel', 'react']

# word = choice(words)
index = randint(0, len(words) - 1)
word = words[index]
i = 1

true_char = []
false_char = []

while i < 7:
    win = True
    for char in word:
        if char == ' ':
            print(' / ', end='')
        elif char in true_char:
            print(f'{char} ', end='')
        else:
            print('_ ', end='')
            win = False
    if win:
        print('You Win ...👏')
        break
    user_char = input(f'Please Enter Char ({i}): ').lower()

    if len(user_char) != 1:
        print('mese adam vared kon 😐')
    elif user_char in word:
        true_char.append(user_char)
    else:
        false_char.append(user_char)
        i += 1

if i >= 7:
    print('You Lose ...😎')
