groups = open('groups.txt', 'r').read().split('\n\n')
#print(groups)
globalyes = 0
#for group in groups:
    #if 'a' in group:
    #    globalyes += 1
    #if 'b' in group:
    #    globalyes += 1
    #if 'c' in group:
    #    globalyes += 1
    #if 'd' in group:
    #    globalyes += 1
    #if 'e' in group:
    #    globalyes += 1
    #if 'f' in group:
    #    globalyes += 1
    #if 'g' in group:
    #    globalyes += 1
    #if 'h' in group:
    #    globalyes += 1
    #if 'i' in group:
    #    globalyes += 1
    #if 'j' in group:
    #    globalyes += 1
    #if 'k' in group:
    #    globalyes += 1
    #if 'l' in group:
    #    globalyes += 1
    #if 'm' in group:
    #    globalyes += 1
    #if 'n' in group:
    #    globalyes += 1
    #if 'o' in group:
    #    globalyes += 1
    #if 'p' in group:
    #    globalyes += 1
    #if 'q' in group:
    #    globalyes += 1
    #if 'r' in group:
    #    globalyes += 1
    #if 's' in group:
    #    globalyes += 1
    #if 't' in group:
    #    globalyes += 1
    #if 'u' in group:
    #    globalyes+=1
    #if 'v' in group:
    #    globalyes+=1
    #if 'w' in group:
    #    globalyes+=1
    #if 'x' in group:
    #    globalyes+=1
    #if 'y' in group:
    #    globalyes+=1
    #if 'z' in group:
    #    globalyes+=1
#print(globalyes)
for group in groups:
    if group.count('a')==len(group.split('\n')):
        globalyes += 1
    if group.count('b')==len(group.split('\n')):
        globalyes += 1
    if group.count('c')==len(group.split('\n')):
        globalyes += 1
    if group.count('d')==len(group.split('\n')):
        globalyes += 1
    if group.count('e')==len(group.split('\n')):
        globalyes += 1
    if group.count('f')==len(group.split('\n')):
        globalyes += 1
    if group.count('g')==len(group.split('\n')):
        globalyes += 1
    if group.count('h')==len(group.split('\n')):
        globalyes += 1
    if group.count('i')==len(group.split('\n')):
        globalyes += 1
    if group.count('j')==len(group.split('\n')):
        globalyes += 1
    if group.count('k')==len(group.split('\n')):
        globalyes += 1
    if group.count('l')==len(group.split('\n')):
        globalyes += 1
    if group.count('m')==len(group.split('\n')):
        globalyes += 1
    if group.count('n')==len(group.split('\n')):
        globalyes += 1
    if group.count('o')==len(group.split('\n')):
        globalyes += 1
    if group.count('p')==len(group.split('\n')):
        globalyes += 1
    if group.count('q')==len(group.split('\n')):
        globalyes += 1
    if group.count('r')==len(group.split('\n')):
        globalyes += 1
    if group.count('s')==len(group.split('\n')):
        globalyes += 1
    if group.count('t')==len(group.split('\n')):
        globalyes += 1
    if group.count('u')==len(group.split('\n')):
        globalyes += 1
    if group.count('v')==len(group.split('\n')):
        globalyes += 1
    if group.count('w')==len(group.split('\n')):
        globalyes += 1
    if group.count('x')==len(group.split('\n')):
        globalyes += 1
    if group.count('y')==len(group.split('\n')):
        globalyes += 1
    if group.count('z')==len(group.split('\n')):
        globalyes += 1
print(globalyes)