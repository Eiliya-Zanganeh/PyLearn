def diamond_draw(num: int) -> None:
    x = num + num - 1
    for i in range(num):
        i += 1
        count_star = i + i - 1
        count_space = (x - count_star) // 2
        print(' ' * count_space, end='')
        print('*' * count_star, end='')
        print('')

    for i in range(num):
        i += 1
        count_star = x - (i * 2)
        count_space = (x - count_star) // 2
        print(' ' * count_space, end='')
        print('*' * count_star, end='')
        print('')


diamond_draw(10)
