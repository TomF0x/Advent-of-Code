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


def SecondStar(lst):
    oxygen = ""
    bits = lst.copy()
    for i in range(12):
        zero, one = 0, 0
        for number in bits:
            if number[i] == "0":
                zero += 1
            elif number[i] == "1":
                one += 1
        if zero < one or zero == one:
            key = "1"
        else:
            key = "0"
        if len(bits) == 1:
            break
        temp = bits.copy()
        for number in temp:
            if number[i] != key:
                bits.remove(str(number))
    oxygen = bits[0]
    bits = lst.copy()
    for i in range(12):
        zero, one = 0, 0
        for number in bits:
            if number[i] == "0":
                zero += 1
            elif number[i] == "1":
                one += 1
        if zero < one or zero == one:
            key = "0"
        else:
            key = "1"
        temp = bits.copy()
        if len(bits) == 1:
            break
        for number in temp:
            if number[i] != key:
                bits.remove(str(number))
    return int(oxygen, 2)*int(bits[0], 2)

print(SecondStar((open("data.txt", "r").read().split("\n"))))
