def test(arr):
    mid = len(arr) // 2
    return arr[:mid] == arr[-1:-mid - 1:-1]


print(test([1, 4, 3, 4, 1]))
print(test([1, 2, 3]))
