numbers = []

while True:
    num = input('Please Enter Number or Exit: ').title()
    if num == 'Exit':
        break
    else:
        try:
            num = int(num)
            numbers.append(num)
        except:
            print('You did not enter correctly...')
            continue

print(numbers)
is_sort = True
point = 0
for number in numbers:
    index = numbers.index(number)
    if index == len(numbers) - 1:
        break
    elif numbers[index] <= numbers[index + 1]:
        continue
    else:
        is_sort = False
        break

if is_sort:
    print("List Is Sort...")
else:
    print("List Is Not Sort...")