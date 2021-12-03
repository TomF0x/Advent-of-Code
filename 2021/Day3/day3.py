def FirstStar(lst):
    gamma = ""
    for i in range(12):
        zero, one = 0, 0
        for number in lst:
            if number[i] == "0":
                zero += 1
            elif number[i] == "1":
                one += 1
        if zero > one:
            gamma += "0"
        else:
            gamma += "1"
    epsilon = ""
    for number in gamma:
        if number == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    return int(gamma, 2)*int(epsilon, 2)


print(FirstStar(open("data.txt", "r").read().split("\n")))
