def FirstStar(lst):
    return sum([1 if int(lst[i]) < int(lst[i+1]) else 0 for i in range(len(lst)-1)])


print(FirstStar(open("data.txt", "r").read().split("\n")))
