def FirstStar(lst):
    for _ in range(80):
        for i in range(len(lst)):
            if int(lst[i]) > 0:
                lst[i] = str(int(lst[i])-1)
            else:
                lst[i] = "6"
                lst.append("8")
    print(len(lst))


FirstStar(open("data.txt", "r").read().split(","))
