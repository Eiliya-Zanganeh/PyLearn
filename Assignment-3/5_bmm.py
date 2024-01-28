def main():
    num_1 = int(input('Please Enter Number 1: '))
    num_2 = int(input('Please Enter Number 2: '))
    list_1 = get_divisor(num_1)
    list_2 = get_divisor(num_2)
    bmm = get_bmm(list_1, list_2)
    print(bmm)


def get_divisor(num):
    divisor = []
    for i in range(num):
        if num % (i + 1) == 0:
            divisor.append(i + 1)
    return divisor


def get_bmm(list_1, list_2):
    bmm = None
    for num in list_1:
        if num in list_2:
            bmm = num
    return bmm


if __name__ == '__main__':
    main()
