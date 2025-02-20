import random


def test(list_1, list_2):
    count = len(list_1) if len(list_1) < len(list_2) else len(list_2)
    random.shuffle(list_1)
    random.shuffle(list_2)
    result = []
    for i in range(count):
        result.append((list_1[i], list_2[i]))
    return result


boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

print(test(boys, girls))
