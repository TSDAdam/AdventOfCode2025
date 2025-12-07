from copy import deepcopy
with open ('./07.in') as file:
    data = [line.strip() for line in file]

beams = set()
beams.add(data[0].index('S'))
splitters = {}
for x, row in enumerate(data):
    rowsplitters = []
    for i, c in enumerate(row):
        if c == '^':
            rowsplitters.append(i)
    if len(rowsplitters) > 0:
        splitters[x] = rowsplitters
print(splitters)

splits = 0

tempbeams = deepcopy(beams)
for x in range(len(data)):
    if x in splitters:
        print("\nRow: ", x)
        tempbeams = deepcopy(beams)
        for splitter in splitters[x]:

            if splitter in beams:
                splits += 1
                print("Split at: ", splitter)
                tempbeams.remove(splitter)
                if splitter > 0:
                    tempbeams.add(splitter - 1)
                if splitter < len(data[0]) -1:
                    tempbeams.add(splitter + 1)
    beams = deepcopy(tempbeams)

print("Part 1: ", splits)

# Part 2

start_col = data[0].index('S')

rows = len(data)
cols = len(data[0])

dp = [[0] * cols for _ in range(rows)]
dp[0][start_col] = 1

total_splits = 0

for row in range(rows -1):
    for col in range(cols):
        if dp[row][col] > 0:
            current_char = data[row][col]

            if current_char == '^':
                total_splits += dp[row][col]

                # left
                if col > 0:
                    dp[row + 1][col - 1] += dp[row][col]
                # right
                if col < cols - 1:
                    dp[row + 1][col + 1] += dp[row][col]
            else:
                dp[row + 1][col] += dp[row][col]

total_paths = sum(dp[rows - 1])
print("Part 2: ", total_paths)