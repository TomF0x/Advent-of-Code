input = open('example.txt', 'r').read().split('\n')


#Star 1

def cleaner(lst):
    newlst = []
    toremove = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ' bag', '.', ' bags']
    for contain in lst:
        for a in toremove:
            contain = contain.replace(a, '')
        newlst.append(contain[1:])
    return newlst


bags = {a.split(' bags ')[0]: cleaner(a.split(' contain ')[1].split(', ')) for a in input}


def explore(bagtoexplore):
    try:
        bags[bagtoexplore]
    except KeyError:
        bagtoexplore = bagtoexplore[:-1]
    if 'o others' in bags[bagtoexplore]:
        return False
    if 'shiny gold' in bags[bagtoexplore] or 'shiny golds' in bags[bagtoexplore]:
        return True
    if len(bags[bagtoexplore])==4:
        return explore(bags[bagtoexplore][0]) or explore(bags[bagtoexplore][1]) or explore(bags[bagtoexplore][2]) or explore(bags[bagtoexplore][3])
    elif len(bags[bagtoexplore])==3:
        return explore(bags[bagtoexplore][0]) or explore(bags[bagtoexplore][1]) or explore(bags[bagtoexplore][2])
    elif len(bags[bagtoexplore])==2:
        return explore(bags[bagtoexplore][0]) or explore(bags[bagtoexplore][1])
    else:
        return explore(bags[bagtoexplore][0])


print([explore(a) for a in list(bags)].count(True))

