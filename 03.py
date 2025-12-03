with open('./03.in') as file:
    data = [line.strip() for line in file]
allbatteries = []

for row in data:
    maxbatt = 0
    for i, b in enumerate(row):
        for nextb in range(i + 1, len(row)):
            combostring = b + row[nextb]
            if int(combostring) > maxbatt:
                maxbatt = int(combostring)
    allbatteries.append(maxbatt)

p1 = 0
for b in allbatteries:
    p1 += b
print("Part 1: ", p1)

# Part 2
p2batteries = []

for row in data:
    batteries = []
    for b in row:
        batteries.append(int(b))
    newbatt = []
    i = 0 # index for position in battery row
    while len(newbatt) < 12:
        j = len(row) - 12 + len(newbatt) + 1 # end of window to look for next value, always leaving room to get to 12 total
        maxval = max(batteries[i:j]) # find biggest in next window
        newbatt.append(maxval)
        i = batteries[i:j].index(maxval) + i + 1 # move the index pointer to just after the one we just added
    p2batteries.append(newbatt)

p2 = 0
for battery in p2batteries:
    p2 += int("".join(str(b) for b in battery))
print("Part 2: ", p2)


