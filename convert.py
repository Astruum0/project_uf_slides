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
            if tunnel:
                if level[lig][col] == 14:
                    level[lig][col] = 13

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


def convertTime(time):
    time = str(time)
    if "." in time:
        s, ms = time.split(".")
        m = str(int(s) // 60)
        h = str(int(m) // 60)
        m = str(int(m) % 60)
        s = str(int(s) % 60)
        if ms == "0":
            ms = "000"
    else:
        s = time
        ms = "000"
        m = str(int(s) // 60)
        h = str(int(m) // 60)
        m = str(int(m) % 60)
        s = str(int(s) % 60)

    return h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2) + "," + ms.zfill(3)


def convertShortTime(time):
    time = str(time)
    if "." in time:
        s, ms = time.split(".")
        m = str(int(s) // 60)
        h = str(int(m) // 60)
        m = str(int(m) % 60)
        s = str(int(s) % 60)
        if ms == "0":
            ms = "000"
    else:
        s = time
        ms = "000"
        m = str(int(s) // 60)
        h = str(int(m) // 60)
        m = str(int(m) % 60)
        s = str(int(s) % 60)

    return m.zfill(2) + ":" + s.zfill(2) + "," + ms.zfill(3)

