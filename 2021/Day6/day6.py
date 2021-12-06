def FirstStar(lst):
    for _ in range(5):
        for i in range(len(lst)):
            if int(lst[i]) > 0:
                lst[i] = str(int(lst[i])-1)
            else:
                lst[i] = "6"
                lst.append("8")
    print(len(lst))


FirstStar(open("data.txt", "r").read().split(","))


def SecondStar(lst):
    dic = {str(i): 0 for i in range(-1, 9)}
    temp = {str(i): 0 for i in range(-1, 9)}
    for number in lst:
        dic[number] += 1
    for _ in range(256):
        for i in range(8, -1, -1):
            temp[str(i-1)] = dic[str(i)]
        temp["8"] = temp["-1"]
        temp["6"] += temp["-1"]
        temp["-1"] = 0
        dic = temp.copy()
    print(sum(dic.values()))


SecondStar(open("data.txt", "r").read().split(","))
