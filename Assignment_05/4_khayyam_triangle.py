def khayyam_triangle(num: int) -> list:
    all_rows = []
    for i in range(num):
        row = []
        i += 1
        for j in range(i):
            if j == 0:
                print("|1|", end='')
                row.append(1)
                continue
            try:
                number = all_rows[i - 2][j] + all_rows[i - 2][j - 1]
            except IndexError:
                number = 1
            row.append(number)
            print(f"|{number}|", end='')
        all_rows.append(row)
        print("")
    return all_rows


all_rows = khayyam_triangle(7)
print('---------------------------------')
print(all_rows)
