from copy import deepcopy
with open('./04.in') as file:
    rawdata = [line.strip() for line in file]

data = []
for row in rawdata:
    thisrow = []
    for c in row:
        thisrow.append(c)
    data.append(thisrow)

t2 = 0

def removepaper(data):
    returndata = deepcopy(data) # Create a copy of the original data to modify and return
    MAX = 3
    t1 = 0
    dirs = [-1,0,1]
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '@':
                c = 0
                for yy in dirs: # Check all neighbouring spaces for @ and increment the counter if found
                    for xx in dirs:
                        if 0 <= y + yy <= len(row) - 1:
                            if 0 <= x + xx <= len(data) -1:
                                if not (xx == 0 and yy == 0):
                                    if data[y + yy][x + xx] == '@':
                                        c += 1
                if c <= MAX: # if there are fewer than 4 neighbouring
                    t1 += 1
                    returndata[y][x] = '.' # remove the roll from the data to be returned
    return (t1, returndata) # return the total number removed and the new data

t1, ret = removepaper(data)
print("Part 1: ", t1)
removedpaper = True
thisdata = deepcopy(data)
while removedpaper:
    t, thisdata = removepaper(thisdata)
    if t > 0:
        t2 += t
    else:
        removedpaper = False
print("Part 2: ", t2)