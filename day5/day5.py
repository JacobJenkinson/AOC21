import numpy as np

input_file = open("input.txt", "r").read().splitlines()

position_mappings = []
for line in input_file:
    a, b = line.split('->')
    ax, ay = map(int, a.split(','))
    bx, by = map(int, b.split(','))
    position_mappings.append((ax, ay, bx, by))

mapped_points = np.zeros((1000, 1000))
points = []
for positions in position_mappings:
    if positions[0] == positions[2]:
        upper = max(positions[1], positions[3])
        lower = min(positions[1], positions[3])
        for i in range(lower, upper + 1):
            mapped_points[i][positions[0]] += 1

    elif positions[1] == positions[3]:
        upper = max(positions[0], positions[2])
        lower = min(positions[0], positions[2])
        for i in range(lower, upper + 1):
            mapped_points[positions[1]][i] += 1
    else:
        upper_x = max(positions[0], positions[2])
        lower_x = min(positions[0], positions[2])
        upper_y = max(positions[1], positions[3])
        lower_y = min(positions[1], positions[3])

        m = (positions[3] - positions[1]) / (positions[2] - positions[0])
        if m > 0:
            for index, i in enumerate(range(lower_x, upper_x + 1)):
                mapped_points[lower_y + index][i] += 1
        else:
            for index, i in enumerate(range(lower_y, upper_y + 1)):
                mapped_points[i][upper_x - index] += 1

# print(mapped_points)
total = (mapped_points > 1).sum()
print(total)
