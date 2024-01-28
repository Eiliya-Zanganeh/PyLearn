def main():
    num_1 = int(input('Please Enter Number 1: '))
    num_2 = int(input('Please Enter Number 2: '))
    if num_1 > num_2:
        get_kmm(num_2, num_1)
    else:
        get_kmm(num_1, num_2)


def get_kmm(num_1, num_2):
    multiple_1 = ['']
    multiple_2 = ['']
    i = 2
    while True:
        multiple_1.append(num_1 * i)
        multiple_2.append(num_2 * i)
        if multiple_1[-1] in multiple_2:
            print(multiple_1[-1])
            break
        i += 1


if __name__ == '__main__':
    main()