from collections import defaultdict

with open("input.txt") as lines:
    graph = defaultdict(int)
    graph_inv = defaultdict(list)

    while (line := lines.readline().rstrip()):
        line_coords = line.split(' -> ')
        start = line_coords[0].split(',')
        end = line_coords[1].split(',')

        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))

        if start[0] != end[0] and start[1] != end[1]:
            continue

        xy = 0 if start[1] == end[1] else 1

        i_start = start[xy]
        i_end = end[xy]

        if start[xy] > end[xy]:
            i_start = end[xy]
            i_end = start[xy]

        if xy == 0:
            for i in range(i_start, i_end + 1):
                graph[(i, start[1])] += 1
        else:
            for i in range(i_start, i_end + 1):
                graph[(start[0], i)] += 1

    for k,v in graph.items():
        graph_inv[v].append(k)

    for k,v in graph_inv.items():
        print(f"Nodes with {k} lines: {len(v)}")

    total = sum([len(v) for k,v in graph_inv.items() if k > 1])
    print(f"Nodes with more than 1 line: {total}")
