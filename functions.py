def Convert(lig, col):
    x = 40 * col
    y = 40 * lig
    return x, y


def miniConvert(lig, col):
    x = 10 * col
    y = 10 * lig
    return x, y


def resetLevel(level, dire, tunnel):
    for col in range(15):
        for lig in range(15):

            if level[lig][col] == 14:
                level[lig][col] = 13
            if tunnel:

                if level[lig][col] == 11:
                    level[lig][col] = 12
                elif level[lig][col] == 12:
                    level[lig][col] = 11

    for _ in range(dire):
        for col in range(15):
            for lig in range(15):
                if level[lig][col] == 9:
                    level[lig][col] = 6
                elif level[lig][col] == 8:
                    level[lig][col] = 7
                elif level[lig][col] == 6:
                    level[lig][col] = 8
                elif level[lig][col] == 7:
                    level[lig][col] = 9

    return level


def levelSetStart(level):
    for col in range(15):
        for lig in range(15):
            x, y = Convert(lig, col)
            if level[lig][col] == 2:
                return x, y
