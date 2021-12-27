import math

import numpy


def in_range(coord):
    return -50 <= coord <= 50

def count_cubes(cubes):
    total = 0
    print(cubes)
    for x_row in cubes:
        for y_col in x_row:
            for z_val in y_col:
                total += z_val

    return total

boxes = []

current_largest = 0
with open("test_input2.txt") as on_offs:
    while (ranges:= on_offs.readline().rstrip()):
        on_off = ranges.split(' ')[0]
        coords = ranges.split(' ')[1].split(',')

        x1, x2 = sorted(int(x) for x in coords[0][2:].split('..'))
        y1, y2 = sorted(int(y) for y in coords[1][2:].split('..'))
        z1, z2 = sorted(int(z) for z in coords[2][2:].split('..'))

        boxes.append([x1, x2, y1, y2, z1, z2, on_off])

cubes = [0] * 3125

for index, box in enumerate(boxes):
    x1 = box[0] + 50016
    x2 = box[1] + 50016 + 1
    y1 = box[2] + 50016
    y2 = box[3] + 50016 + 1
    z1 = box[4] + 50016
    z2 = box[5] + 50016 + 1
    on_off = box[6]

    print(f"{on_off} {x1=}-{x2=} {y1=}-{y2=} {z1=}-{z2=}")
    big_index = 0
    for jindex in range(len(cubes)):
        str_num = list(format(cubes[jindex],'#032b'))[2:]
        for bit in range(len(str_num)):
            grid_size = 100032 * 100032
            z = big_index % 10032
            y = math.floor((big_index - (z * grid_size)) / 100032)
            x = math.floor((big_index - (z * grid_size)) % 100032)

            big_index += 1

            print(big_index, x, y,z)
            if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                if on_off == "on" :
                    str_num[bit] = "1"
                else:
                    str_num[bit] = "0"

        cubes[jindex] = int("".join(str_num), 2)

running_total = 0
for jindex in range(len(cubes)):
    str_num = list(format(cubes[jindex],'#032b'))[2:]
    running_total += sum([int(x) for x in str_num])
print(running_total)
