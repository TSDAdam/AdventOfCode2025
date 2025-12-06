with open('./06.in') as file:
    data = [line.strip() for line in file]

rows = []
operators = []
for row in data[:-1]:
    rows.append([int(x) for x in row.split(" ") if x != ''])

for x in data[-1].split(' '):
    if x != '':
        operators.append(x)

# Part 1
totals = []
for i, op in enumerate(operators):
    t = rows[0][i]
    for x in range(1, len(rows)):
        if op == '+':
            t += rows[x][i]
        else:
            t *= rows[x][i]
    totals.append(t)

print("Part 1: ", sum(totals))

# Part 2
# Need to reparse without stripping spaces out...
rawdata = []
with open('./06.in') as file:
    for line in file:
        s = ''
        for c in line:
            if not c == '\n':
                s += c
            else:
                break
        rawdata.append(s)

numbers = []
newnumbers = []
for y in range(len(rawdata[0]) -1,-1,-1):
    num = ''
    for x in range(len(rawdata) - 1):
        if rawdata[x][y] != ' ':
            num = num + rawdata[x][y]
    if len(num) > 0:
        numbers.append(int(num))
    else:
        newnumbers.insert(0, numbers)
        numbers = []
newnumbers.insert(0, numbers)


p2totals = []
for i in range(len(newnumbers) - 1, -1, -1):
    t = newnumbers[i][0]
    op = operators[i]
    for n in newnumbers[i][1:]:
        if op == '+':
            t += n
        elif op == '*':
            t *= n
    p2totals.append(t)

print("Part 2: ",sum(p2totals))
