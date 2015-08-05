size = int(input())
square_map = []
to_be_x = []
for i in range(0,size):
    line = list(input())
    line = [int(x) for x in line]
    square_map.append(line)

for j in range(1,size-1):
    for k in range(1, size-1):
        if square_map[j][k] > square_map[j-1][k] and square_map[j][k] > square_map[j][k-1] and square_map[j][k] > square_map[j+1][k] and square_map[j][k] > square_map[j][k+1]:
            to_be_x.append([j, k])

for values in to_be_x:
    square_map[values[0]][values[1]] = "X"

for line in square_map:
    new_line = [ str(x) for x in line ]
    print(''.join(new_line))
