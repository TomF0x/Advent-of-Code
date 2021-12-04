def FirstStar(data):
    numbers = data[0].split(",")
    boards = [[row.replace("  ", " ").split(" ") if row[0] != " " else row[1:].replace("  ", " ").split(" ") for row in board.split('\n')] for board in data[1:]]
    testnumber = []
    for nb in numbers:
        testnumber.append(nb)
        for i in range(len(boards)):
            for row in boards[i]:
                if not False in [True if number in testnumber else False for number in row]:
                    print(f"Board {i + 1} win")
                    rep = 0
                    for lst in boards[i]:
                        for number in lst:
                            if number not in testnumber:
                                rep += int(number)
                    print(rep*int(testnumber.pop()))
                    return None
            for index in range(5):
                if not False in [True if number in testnumber else False for number in [col[index] for col in [row for row in boards[i]]]]:
                    print(f"Board {i + 1} win")
                    rep = 0
                    for lst in boards[i]:
                        for number in lst:
                            if number not in testnumber:
                                rep += int(number)
                    print(rep * int(testnumber.pop()))
                    return None


FirstStar(open("data.txt", "r").read().split("\n\n"))


def SecondStar(data):
    numbers = data[0].split(",")
    boards = [[row.replace("  ", " ").split(" ") if row[0] != " " else row[1:].replace("  ", " ").split(" ") for row in board.split('\n')] for board in data[1:]]
    testnumber = []
    boardswin = []
    for nb in numbers:
        testnumber.append(nb)
        for i in range(len(boards)):
            for row in boards[i]:
                if (not False in [True if number in testnumber else False for number in row]) and i not in boardswin:
                    print(f"Board {i + 1} win row")
                    rep = 0
                    for lst in boards[i]:
                        for number in lst:
                            if number not in testnumber:
                                rep += int(number)
                    print(rep * int(testnumber[-1]))
                    boardswin.append(i)
            for index in range(5):
                if (not False in [True if number in testnumber else False for number in [col[index] for col in [row for row in boards[i]]]]) and i not in boardswin:
                    print(f"Board {i + 1} win colums")
                    rep = 0
                    for lst in boards[i]:
                        for number in lst:
                            if number not in testnumber:
                                rep += int(number)
                    print(rep * int(testnumber[-1]))
                    boardswin.append(i)


SecondStar(open("data.txt", "r").read().split("\n\n"))
