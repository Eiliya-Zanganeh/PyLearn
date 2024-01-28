i = 1
num_1 = 1
num_2 = 1
user_number = int(input('Please Enter Number: '))
print(num_2, end=', ')
while i < user_number:
    print(num_2, end=', ')
    res = num_2
    num_2 += num_1
    num_1 = res
    i += 1

