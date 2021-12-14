from collections import defaultdict

with open("input.txt") as points:
    x_coords = defaultdict(list)
    y_coords = defaultdict(list)
    while (point := points.readline().rstrip()):
        pt = point.split(',')
        x = int(pt[0])
        y = int(pt[1])

        x_coords[x].append(y)
        y_coords[y].append(x)

    print()
    while (folds := points.readline().rstrip()):
        print(folds)
        fold_along = folds.split('=')
        coords = x_coords if 'x' in fold_along[0] else y_coords
        other_coords = x_coords if 'y' in fold_along[0] else y_coords

        fold_pt = int(fold_along[1])

        for point in list(coords.keys()):
            if point > fold_pt:
                coords[fold_pt*2 - point] += coords[point]
                coords[fold_pt*2 - point] = list(set(coords[fold_pt*2 - point] ))

                for pts in coords[point]:
                    other_coords[pts].remove(point)
                    other_coords[pts].append(fold_pt*2 - point)
                    other_coords[pts] = list(set(other_coords[pts]))

                del coords[point]

        visible = sum([len(v) for k, v in coords.items()])
        print(f"{visible=}")

        print()

    for y in range(max(y_coords.keys()) + 1):
        for x in range(max(x_coords.keys()) + 1):
            if x in y_coords[y]:
                print("#", end="")
            else:
                print(".", end="")
        print()
