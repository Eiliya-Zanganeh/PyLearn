user_list = []
while True:
    result = input('Enter Number Or Exit: ').strip().title()
    if result == "Exit":
        break
    else:
        user_list.append(int(result))

# user_set = set(user_list)
# print(user_set)

for num in user_list:
    count = user_list.count(num)
    if count > 1:
        index = user_list.index(num)
        user_list.pop(index)

print(user_list)
