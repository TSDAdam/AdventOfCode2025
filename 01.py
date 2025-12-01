with open('./01.in') as file:
    data = [line.strip() for line in file]

t1 = 0
t2 = 0

dial = 50 # Starting position for dial

for line in data:
    lastdial = dial # Remember where the dial was for pt 2
    dir = line[0]
    turn = int(line[1:])
    fullrotations, partrotation = divmod(turn, 100) # Anything over 100 is at least 1 zero for pt 2
    t2 += fullrotations
    if dir == 'L':
        dial -= partrotation # we can ignore full rotations, just move the dial the remainder
    elif dir == 'R':
        dial += partrotation
    if (dial < 0 or dial > 100) and lastdial != 0: # if it's gone past 0 and didn't start at 0
        t2 +=1
    print(dial)

    dial = dial % 100
    print(dial)
    if dial == 0:
        t1 += 1

print("part 1: ", t1)
print("part 2: ", t1 + t2)