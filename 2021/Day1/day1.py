def FirstStar(lst):
    return sum([1 if int(lst[i]) < int(lst[i+1]) else 0 for i in range(len(lst)-1)])


print(FirstStar(open("data.txt", "r").read().split("\n")))


def SecondStar(lst):
    return sum([1 if int(lst[i])+int(lst[i+1])+int(lst[i+2]) < int(lst[i + 1])+int(lst[i + 2]) + int(lst[i+3]) else 0 for i in range(len(lst) - 3)])


print(SecondStar(open("data.txt", "r").read().split("\n")))
