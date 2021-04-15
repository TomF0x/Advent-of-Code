password=open('passwords.txt','r').read().split('\n')[:-1]
nb=0

#Star 1
for passw in password:
    passw=passw.replace(':','').split(' ')
    print(passw)
    if int(passw[0].split('-')[0]) <= int(passw[2].count(passw[1])) <= int(passw[0].split('-')[1]):
        nb+=1
print(nb)

#Star 2
for passw in password:
    passw=passw.replace(':','').split(' ')
    print(passw)
    print(passw[2][int(passw[0].split('-')[0]) - 1] == passw[1])
    print(passw[2][int(passw[0].split('-')[1])-1]==passw[1])
    if passw[2][int(passw[0].split('-')[0])-1]==passw[1] and (passw[2][int(passw[0].split('-')[1])-1]==passw[1])==False or (passw[2][int(passw[0].split('-')[0])-1]==passw[1])==False and passw[2][int(passw[0].split('-')[1])-1]==passw[1]:
        print('oui')
        nb+=1
print(nb)