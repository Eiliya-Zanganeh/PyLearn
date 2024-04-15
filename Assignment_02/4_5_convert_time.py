user_time = input('Please Enter Hour To Second Or Second To Hour: ')
hour, minute, second = 0, 0, 0
try:
    # User Time Is Second
    user_time = int(user_time)
    if user_time > 59:
        minute = user_time // 60
        second = user_time % 60
        if minute > 59:
            hour = minute // 60
            minute = minute % 60
            print(f'{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}')
        else:
            print(f'00:{str(minute).zfill(2)}:{str(second).zfill(2)}')
    else:
        print(f'00:00:{str(user_time).zfill(2)}')
except ValueError:
    user_time = user_time.split(':')
    if len(user_time) == 2:
        minute = user_time[0]
        second = user_time[1]
    elif len(user_time) == 3:
        hour = int(user_time[0])
        minute = int(user_time[1])
        second = int(user_time[2])

    minute += hour * 60
    second += minute * 60

    print(f'Second: {second}')
