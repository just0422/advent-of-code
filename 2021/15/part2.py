from collections import defaultdict

with open("input.txt") as risks:
    graph = []

    while (risk_line := risks.readline().rstrip()):
        graph.append([int(x) for x in list(risk_line)])

    based_graph_size = len(graph)
    new_graph = []
    for x in range(len(graph) * 5):
        new_graph.append([])
        for i in range(5):
            for y in graph[x % 10]:
                new_val = y + i + int(x/len(graph))
                if new_val >= 10:
                    new_val = new_val % 10 +1
                new_graph[x].append(new_val)


    # Dijkstra's
    visited = defaultdict(lambda: False)
    risk_sums = defaultdict(lambda: 20 * len(new_graph))
    risk_sums[(0,0)] = 0
    x = 0
    y = 0
    while True:
        if x == len(graph) or y == len(graph):
            continue
        if x == len(new_graph) - 1 and y == len(new_graph) - 1:
            break

        if not visited[(x+1,y)] and x < len(new_graph) - 1 and risk_sums[(x+1,y)] > risk_sums[(x, y)] + new_graph[x+1][y]:
            risk_sums[(x+1,y)] = risk_sums[(x, y)] + new_graph[x+1][y]
        if not visited[(x, y+1)] and y < len(new_graph) - 1 and risk_sums[(x,y+1)] > risk_sums[(x, y)] + new_graph[x][y+1]:
            risk_sums[(x,y+1)] = risk_sums[(x, y)] + new_graph[x][y+1]

        visited[(x,y)] = True
        del risk_sums[(x,y)]

        r_sums = min(risk_sums.values())
        res = [key for key in risk_sums if not visited[key] and risk_sums[key] == r_sums]

        x,y = res[0]

    print(len(new_graph) - 1, len(new_graph) - 1, risk_sums[(len(new_graph)-1, len(new_graph) - 1)])
