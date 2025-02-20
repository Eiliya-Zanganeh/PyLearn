class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __add__(self, other):
        hour, minute, second = 0, 0, 0
        second += self.second + other.second
        if second > 59:
            minute += second // 60
            second -= 60 * (second // 60)
        minute += self.minute + other.minute
        if minute > 59:
            hour += minute // 60
            minute -= 60 * (minute // 60)
        hour += self.hour + other.hour
        return Time(hour, minute, second)

    def __sub__(self, other):
        hour, minute, second = self.hour, self.minute, self.second
        if (second - other.second >= 0):
            second -= other.second
        else:
            minute -= 1
            second += 60
            second -= other.second
        if (minute - other.minute >= 0):
            minute -= other.minute
        else:
            hour -= 1
            minute += 60
            minute -= other.minute
        hour -= other.hour
        return Time(hour, minute, second)
        
    def convert_time_to_second(self):
        second = 0
        second += self.second
        second += self.minute * 60
        second += self.hour * 60 * 60
        return second

    def convert_second_to_time(self):
        time = Time(0, 0, 0)
        return self + time
    
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

time_1 = Time(5, 30, 30)
time_2 = Time(5, 29, 30)
print(time_1)
print(time_2)

sum_time = time_1 + time_2
sub_time = time_1 - time_2
print(sum_time)
print(sub_time)

second_1 = time_1.convert_time_to_second()
second_2 = time_2.convert_time_to_second()
print(second_1)
print(second_2)

time_3 = Time(0, 0, 600)
convert_second_to_time = time_3.convert_second_to_time()
print(convert_second_to_time)