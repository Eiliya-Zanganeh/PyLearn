from random import randint

numbers = []
end_point = 100
while True:
    user_input = int(input('Please Enter Number: '))
    if user_input > end_point:
        print(f'Please Enter a smaller number of {end_point}...')
    elif user_input < 0:
        print('mese adam vared kon 😐')
    else:
        break

while len(numbers) != user_input:
    # sample(range(100), user_input)
    random_number = randint(0, end_point)
    if random_number not in numbers:
        numbers.append(random_number)

print(numbers)
