num=open('num.txt','r').read().split('\n')[:-1]
print(num)
for a in num:
    for b in num:
        for c in num:
            if int(a)+int(b)+int(c)==2020:
                print(a,b,c)