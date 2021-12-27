import itertools

from scipy.spatial.transform import Rotation as R


def generate_variations(graph):
    """
    [x, y , z]
    [-x, y, z]
    [x,

    Rx
     1  0  0
     0  0 -1
     0  1  0

    Ry
     0  0  1
     0  1  0
    -1  0  0

    Rz
     0 -1  0
     1  0  0
     0  0  1
    """
    pass

v = [4,6,5]
points = []
for axis in 'xyz':
    for rot in [90, 180, 270]:
        r = R.from_euler(axis, rot, degrees=True)
        ax_v = [round(x) for x in r.apply(v)]
        points.append(ax_v)

        for subaxis in 'xyz':
            if subaxis == axis:
                continue
            for rot in [90, 180, 270]:
                r = R.from_euler(axis, rot, degrees=True)
                sax_v = [round(x) for x in r.apply(ax_v)]
                points.append(sax_v)

                for subsubaxis in 'xyz':
                    if subsubaxis in [subaxis, axis]:
                        continue
                    for rot in [90, 180, 270]:
                        r = R.from_euler(subsubaxis, rot, degrees=True)
                        points.append([round(x) for x in r.apply(sax_v)])

print(len(points))

unique_points = []
for point in points:
    if point not in unique_points:
        print(point)
        unique_points.append(point)
print(len(unique_points))
