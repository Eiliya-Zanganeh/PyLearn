# user_list = [1, 2, 3, 4, 5, 6]
# user_list.reverse()
# print(user_list)

user_list = []
while True:
    result = input('Enter Number Or Exit: ').strip().title()
    if result == "Exit":
        break
    else:
        user_list.append(int(result))
new_list = []
for num in range(len(user_list)):
    item = user_list.pop()
    new_list.append(item)

print(new_list)
