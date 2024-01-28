w = float(input('Please Enter weight : '))
h = float(input('Please Enter height : '))

bmi = w / h

if bmi < 18.5:
    print('Underweight')
elif (bmi >= 18.5) and (bmi < 25):
    print('Normalweight')
elif (bmi >= 25) and (bmi < 30):
    print('Overweight')
elif (bmi >= 30) and (bmi < 35):
    print('Obesity')
elif (bmi >= 35) and (bmi < 40):
    print('Extreme Obesity')