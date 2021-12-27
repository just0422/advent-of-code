from copy import deepcopy

cucumber_map = []

with open("input.txt") as cucumbers:
    while(row:= cucumbers.readline().rstrip()):
        cucumber_map.append(list(row))

    for c in cucumber_map:
        print(''.join(c))

    steps = 0
    travelers = -1

    while travelers != 0:
        cucumber_map2 = deepcopy(cucumber_map)
        travelers = 0
        for x in range(len(cucumber_map)):
            for y in range(len(cucumber_map[x])):
                if cucumber_map[x][y] == '>':
                    next_y = y + 1
                    if y == len(cucumber_map[x]) - 1:
                        next_y = 0

                    if cucumber_map[x][next_y] == '.':
                        cucumber_map2[x][next_y] = '>'
                        cucumber_map2[x][y] = '.'
                        travelers += 1

        cucumber_map = deepcopy(cucumber_map2)

        for x in range(len(cucumber_map)):
            for y in range(len(cucumber_map[x])):
                if cucumber_map[x][y] == 'v':
                    next_x = x + 1
                    if x == len(cucumber_map) - 1:
                        next_x = 0
                    #print(x,y)
                    #print(next_x, y)
                    #print(cucumber_map[x])
                    #print(cucumber_map[next_x])

                    if cucumber_map[next_x][y] == '.':
                        # print("YES")
                        cucumber_map2[next_x][y] = 'v'
                        cucumber_map2[x][y] = '.'
                        travelers += 1
                        #print(cucumber_map[x])
                        #print(cucumber_map[next_x])
                    #print()
        cucumber_map = deepcopy(cucumber_map2)
        steps += 1

    print()
    for c in cucumber_map:
        print(''.join(c))
    print(steps)
