import numpy

"""
class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def volume(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

def

def overlaps(cube1, cube2):
    pass
"""

def in_range(coord):
    return -50 <= coord <= 50

cubes = numpy.zeros((101, 101, 101))

def print_cubes():
    total = 0
    for x_row in cubes:
        for y_col in x_row:
            for z_val in y_col:
                total += z_val

    print(total)

with open("input.txt") as on_offs:
    while (ranges:= on_offs.readline().rstrip()):
        on_off = ranges.split(' ')[0]
        coords = ranges.split(' ')[1].split(',')

        x1, x2 = sorted(int(x) for x in coords[0][2:].split('..'))
        y1, y2 = sorted(int(y) for y in coords[1][2:].split('..'))
        z1, z2 = sorted(int(z) for z in coords[2][2:].split('..'))

        print(f"{on_off} {x1=}-{x2=} {y1=}-{y2=} {z1=}-{z2=}")


        on_regions = {}
        if in_range(x1) and in_range(x2) and in_range(y1) and in_range(y2) and in_range(z1) and in_range(z2):
            print(f"{x2 - x1} {y2 - y1} {z2-z1} = {(x2 - x1)*(y2 - y1)*(z2-z1)}")
            for x in range(x1 + 50, x2 + 51):
                for y in range(y1 + 50, y2 + 51):
                    for z in range(z1 + 50, z2 + 51):
                        cubes[x][y][z] = 1 if on_off == "on" else 0

print_cubes()
