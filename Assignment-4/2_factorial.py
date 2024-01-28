num = int(input('Please Enter Number: '))
factorial = 1
i = 1
while factorial < num:
    i += 1
    factorial *= i
if factorial == num:
    print("yes")
else:
    print("no")
