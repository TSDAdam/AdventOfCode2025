with open ('./05.in') as file:
    data = [line.strip() for line in file]

validranges = []
values = []

# Parse input
i = 0
for row in data:
    if len(row) > 0:
        i += 1
        minv, maxv = row.split('-')
        validranges.append([int(minv), int(maxv)])
    else:
        i += 1
        break

for row in data[i:]:
    values.append(int(row))
# End parsing

# Sort the ranges, then find overlapping or adjacent ranges and merge them
ranges = sorted(validranges, key=lambda x: x[0])
mergedranges = [ranges[0]]
for start, end in ranges[1:]:
    prev_start, prev_end = mergedranges[-1]
    if start <= prev_end + 1:
        mergedranges[-1] = [prev_start, max(prev_end, end)]
    else:
        mergedranges.append([start, end])

p1 = 0
for val in values: # Binary tree search to search for valid ID
    left, right = 0, len(mergedranges) - 1
    while left <= right:
        mid = (left + right) // 2
        start, end = mergedranges[mid]
        if start <= val <= end:
            p1 += 1
            break
        elif val < start:
            right = mid - 1
        else:
            left = mid + 1

print('Part 1: ', p1)

# Part 2 simple with merged ranges.
p2 = 0
for lo, hi in mergedranges:
    p2 += (hi - lo) + 1
print('Part 2: ', p2)