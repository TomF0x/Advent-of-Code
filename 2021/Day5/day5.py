def FirstStar(lst):
    points, rep = [], 0
    for data in lst:
        point_a, point_b = data.split(" -> ")
        if point_a.split(",")[0] == point_b.split(",")[0]:
            if int(point_a.split(",")[1]) < int(point_b.split(",")[1]):
                for i in range(int(point_a.split(",")[1]), int(point_b.split(",")[1]) + 1):
                    points.append(f"{point_a.split(',')[0]},{i}")
            else:
                for i in range(int(point_b.split(",")[1]), int(point_a.split(",")[1]) + 1):
                    points.append(f"{point_a.split(',')[0]},{i}")
        if point_a.split(",")[1] == point_b.split(",")[1]:
            if int(point_a.split(",")[0]) < int(point_b.split(",")[0]):
                for i in range(int(point_a.split(",")[0]), int(point_b.split(",")[0]) + 1):
                    points.append(f"{i},{point_a.split(',')[1]}")
            else:
                for i in range(int(point_b.split(",")[0]), int(point_a.split(",")[0]) + 1):
                    points.append(f"{i},{point_a.split(',')[1]}")

    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for point in points:
        matrix[int(point.split(",")[1])][int(point.split(",")[0])] += 1

    for row in matrix:
        for number in row:
            if 2 <= number:
                rep += 1

    print(rep)


FirstStar(open("data.txt", "r").read().split("\n"))


def SecondStar(lst):
    points, rep = [], 0
    for data in lst:
        point_a, point_b = data.split(" -> ")
        if ((int(point_b.split(",")[0]) - int(point_a.split(",")[0])) ** 2) ** 0.5 == ((int(point_b.split(",")[1]) - int(point_a.split(",")[1])) ** 2) ** 0.5:
            if int(point_a.split(",")[0]) < int(point_b.split(",")[0]) and int(point_a.split(",")[1]) < int(point_b.split(",")[1]):
                for i in range(int(((int(point_b.split(",")[0]) - int(point_a.split(",")[0])) ** 2) ** 0.5)+1):
                    points.append(f"{int(point_a.split(',')[0])+i},{int(point_a.split(',')[1])+i}")
            elif int(point_a.split(",")[0]) > int(point_b.split(",")[0]) and int(point_a.split(",")[1]) > int(point_b.split(",")[1]):
                for i in range(int(((int(point_b.split(",")[0]) - int(point_a.split(",")[0])) ** 2) ** 0.5)+1):
                    points.append(f"{int(point_a.split(',')[0]) - i},{int(point_a.split(',')[1]) - i}")
            elif int(point_a.split(",")[0]) < int(point_b.split(",")[0]) and int(point_a.split(",")[1]) > int(point_b.split(",")[1]):
                for i in range(int(((int(point_b.split(",")[0]) - int(point_a.split(",")[0])) ** 2) ** 0.5)+1):
                    points.append(f"{int(point_a.split(',')[0]) + i},{int(point_a.split(',')[1]) - i}")
            elif int(point_a.split(",")[0]) > int(point_b.split(",")[0]) and int(point_a.split(",")[1]) < int(point_b.split(",")[1]):
                for i in range(int(((int(point_b.split(",")[0]) - int(point_a.split(",")[0])) ** 2) ** 0.5)+1):
                    points.append(f"{int(point_a.split(',')[0]) - i},{int(point_a.split(',')[1]) + i}")
        if point_a.split(",")[0] == point_b.split(",")[0]:
            if int(point_a.split(",")[1]) < int(point_b.split(",")[1]):
                for i in range(int(point_a.split(",")[1]), int(point_b.split(",")[1]) + 1):
                    points.append(f"{point_a.split(',')[0]},{i}")
            else:
                for i in range(int(point_b.split(",")[1]), int(point_a.split(",")[1]) + 1):
                    points.append(f"{point_a.split(',')[0]},{i}")
        if point_a.split(",")[1] == point_b.split(",")[1]:
            if int(point_a.split(",")[0]) < int(point_b.split(",")[0]):
                for i in range(int(point_a.split(",")[0]), int(point_b.split(",")[0]) + 1):
                    points.append(f"{i},{point_a.split(',')[1]}")
            else:
                for i in range(int(point_b.split(",")[0]), int(point_a.split(",")[0]) + 1):
                    points.append(f"{i},{point_a.split(',')[1]}")

    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for point in points:
        matrix[int(point.split(",")[1])][int(point.split(",")[0])] += 1

    for row in matrix:
        for number in row:
            if 2 <= number:
                rep += 1

    print(rep)


SecondStar(open("data.txt", "r").read().split("\n"))
