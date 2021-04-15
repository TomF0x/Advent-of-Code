import math
seats=open('seat.txt','r').read().split('\n')[:-1]
print(seats)
hight=0
ids=[]
for seat in seats:
    lhalf = 0
    uhalf = 127
    for keyword in seat[0:6]:
        if 'F' in keyword:
            uhalf=uhalf-math.ceil((uhalf-lhalf)/2)
        if 'B' in keyword:
            lhalf=lhalf+math.ceil((uhalf-lhalf)/2)
    if seat[6] == 'F':
        row=lhalf
    else:
        row=uhalf
    lcolum=0
    ucolum=7
    for keyword in seat[-3:-1]:
        if 'R' in keyword:
            lcolum = lcolum + math.ceil((ucolum - lcolum) / 2)
        if 'L' in keyword:
            ucolum = ucolum - math.ceil((ucolum - lcolum) / 2)
    if seat[-1]=='R':
        colum=ucolum
    else:
        colum=lcolum
    id = row*8+colum
    ids.append(id)
    if id>hight:
        hight=id
    print(hight)
ids.sort()
print(ids)
for i in range(13,978):
    if i in ids and i+1 in ids:
        pass
    else:
        print(i)