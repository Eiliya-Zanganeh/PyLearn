score_1 = float(input('Please Enter Score 1 : '))
score_2 = float(input('Please Enter Score 2 : '))
score_3 = float(input('Please Enter Score 3 : '))

avg = (score_1 + score_2 + score_3) / 3

if avg >= 17:
    print('Great')
elif (17 > avg) and (avg >= 12):
    print('Normal')
elif avg < 12:
    print('Fail')