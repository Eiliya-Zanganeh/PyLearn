i = 0
sum_score = 0
while True:
    score = input(f'Please Enter Score Or Exit ({i + 1}): ').title()
    if score == 'Exit':
        break
    else:
        sum_score += float(score)
        i += 1

result = round(sum_score / i)
print(f'Score: {result}')
