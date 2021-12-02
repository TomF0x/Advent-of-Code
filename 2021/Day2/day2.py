def FirstStar(lst):
    horizontal, depth = 0, 0
    for order in lst:
        if "forward" in order:
            horizontal += int(order[8:])
        elif "down" in order:
            depth += int(order[5:])
        elif "up" in order:
            depth -= int(order[3:])
    return depth*horizontal


print(FirstStar(open("data.txt","r").read().split("\n")))


def SecondStar(lst):
    horizontal, depth, aim = 0, 0, 0
    for order in lst:
        if "forward" in order:
            horizontal += int(order[8:])
            depth += aim*int(order[8:])
        elif "down" in order:
            aim += int(order[5:])
        elif "up" in order:
            aim -= int(order[3:])
    return depth * horizontal


print(SecondStar(open("data.txt","r").read().split("\n")))
