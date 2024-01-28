def multiplication_table(row: int, col: int) -> None:
    for r in range(row):
        print("|", end="")
        for c in range(col):
            print((r + 1) * (c + 1), end='|')
        print('')


multiplication_table(3, 3)
