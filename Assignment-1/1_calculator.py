from math import *

print('Welcome to Calculator...')
num_1 = float(input('Please Enter First Number: '))
print('''
    + : sum 
    - : minus
    * : mul
    / : div
    √ : sqrt
    sin, cos, tan, cot
    factorial : fact 
''')
opp = input('Please Select Operator: ')
if opp == 'sqrt':
    print(sqrt(num_1))
elif opp == 'sin':
    print(sin(radians(num_1)))
elif opp == 'cos':
    print(cos(radians(num_1)))
elif opp == 'tan':
    print(tan(radians(num_1)))
elif opp == 'cot':
    print(1 / (tan(radians(num_1))))
elif opp == 'fact':
    print(factorial(int(num_1)))
else:
    num_2 = float(input('Please Enter Second Number: '))
    if opp == 'sum':
        print(num_1 + num_2)
    elif opp == 'minus':
        print(num_1 - num_2)
    elif opp == 'mul':
        print(num_1 * num_2)
    elif opp == 'div':
        if num_2 == 0:
            print('In Division The second number cannot be zero')
        else:
            print(num_1 / num_2)
    else:
        print('The operator is not correct')
