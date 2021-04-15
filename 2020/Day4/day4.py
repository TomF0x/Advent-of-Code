passport=open('passport.txt','r').read().split('\n\n')
valid=0

color=['amb','blu','brn','gry','grn','hzl','oth']
for pp in passport:
    check=0
    if 'byr' in pp and 1920<=int([a for a in pp.replace('\n',' ').split(' ') if 'byr' in a][0][4:])<=2002:
        check+=1
    if 'iyr' in pp and 2010<=int([a for a in pp.replace('\n',' ').split(' ') if 'iyr' in a][0][4:])<=2020:
        check+=1
    if 'eyr' in pp and 2020<=int([a for a in pp.replace('\n',' ').split(' ') if 'eyr' in a][0][4:])<=2030:
        check+=1
    if 'hgt' in pp:
        if 'cm' in [a for a in pp.replace('\n',' ').split(' ') if 'hgt' in a][0] and 150<=int([a for a in pp.replace('\n',' ').split(' ') if 'hgt' in a][0][4:-2])<=193:
            check+=1
        elif 'in' in [a for a in pp.replace('\n',' ').split(' ') if 'hgt' in a][0] and 59<=int([a for a in pp.replace('\n',' ').split(' ') if 'hgt' in a][0][4:-2])<=76:
            check += 1
    if 'hcl' in pp and len([a for a in pp.replace('\n',' ').split(' ') if 'hcl' in a][0])==11:
        if [a for a in pp.replace('\n',' ').split(' ') if 'hcl' in a][0][5]!='#':
            check+=1
    if 'ecl' in pp and [a for a in pp.replace('\n',' ').split(' ') if 'ecl' in a][0][4:] in color:
        check+=1
    if 'pid' in pp and len([a for a in pp.replace('\n',' ').split(' ') if 'pid' in a][0])==13:
        check+=1
    if check==7:
        valid+=1
print(valid)