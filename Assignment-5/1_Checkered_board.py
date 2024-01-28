def checkered_board(row: int, col: int) -> None:
    for r in range(row):
        for c in range(col):
            if r % 2 == 0:
                char = "#"
            else:
                char = "*"
            if c % 2 == 0:
                print(char, end='')
            else:
                if char == "#":
                    print("*", end='')
                else:
                    print("#", end='')
        print("")


checkered_board(2, 2)
