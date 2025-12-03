with open('./02.in') as file:
    data = [line.strip() for line in file]

ids = data[0].split(",")
invalidids = []
t1 = 0
t2 = 0

# Part 1
for row in ids:
    idrange = row.split('-')
    lo = int(idrange[0])
    hi = int(idrange[1])
    for x in range(lo, hi + 1):
        if len(str(x)) % 2 != 0: # odd length IDs can never match
            continue
        else:    
            mid = int(len(str(x)) / 2)
            if str(x)[:mid] == str(x)[mid:]:
                invalidids.append(x)

for id in invalidids:
    t1 += id
print("Part 1: ", t1)

# Part 2
pt2invalidids = []
for row in ids:
    idrange = row.split('-')
    lo = int(idrange[0])
    hi = int(idrange[1])
    for x in range(lo, hi + 1):
        mid = int(len(str(x)) / 2)
        substrings = [] # List of potential substrings to check through
        for y in range(mid):
            substrings.append(str(x)[:y + 1]) 
        for sub in substrings:
            invalid = True
            for i in range(len(sub), int(len(str(x))), len(sub)): # loop through remainder of string, stepping by length of substring
                if str(x)[i:i + len(sub)] != sub:
                    invalid = False
                    break
            if invalid:
                pt2invalidids.append(int(x)) # if it didn't fail to match the substring all the way to the end, it's invalid
                break # add this to the list and don't check it again

for p in pt2invalidids:
    t2 += p
print("Part 2: ", t2)