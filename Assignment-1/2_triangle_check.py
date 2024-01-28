def main():
    side_1 = float(input('Please Enter Side 1: '))
    side_2 = float(input('Please Enter Side 2: '))
    side_3 = float(input('Please Enter Side 3: '))

    if (
            check_side(side_1, side_2, side_3) and
            check_side(side_2, side_1, side_3) and
            check_side(side_3, side_1, side_2)
    ):
        print('True')
    else:
        print('False')


def check_side(side, other_side_1, other_side_2):
    result = other_side_1 + other_side_2
    if side < result:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
