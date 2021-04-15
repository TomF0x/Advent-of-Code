map=open('tree.txt','r').read().split('\n')
print(map)

#Star 1
x=0
y=0
tree=0
while True:
    try:
        x+=3
        y+=1
        if map[y][x]=='#':
            tree+=1
    except:
        break
print(tree)

#Star 2
x=0
y=0
tree=0
rep=1
while True:
    try:
        x+=1
        y+=2
        if map[y][x]=='#':
            tree+=1
    except:
        break
print(tree)