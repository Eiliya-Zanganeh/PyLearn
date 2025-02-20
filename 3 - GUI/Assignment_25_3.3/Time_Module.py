class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour, self.minute, self.second = hour, minute, second

    def update(self):
        self.second += 1
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    def minus(self):
        self.second -= 1
        if self.second <= -1:
            self.second = 59
            self.minute -= 1
        if self.minute <= -1:
            self.minute = 59
            self.hour -= 1

    def __str__(self):
        return f"{self.hour:02}", f"{self.minute:02}", f"{self.second:02}"

    def reset(self):
        self.hour, self.minute, self.second = 0, 0, 0