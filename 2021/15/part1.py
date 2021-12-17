from collections import defaultdict

with open("input.txt") as risks:
    graph = []

    while (risk_line := risks.readline().rstrip()):
        graph.append([int(x) for x in list(risk_line)])

    visited = defaultdict(lambda: False)
    unvisited = []
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            unvisited.append((x,y))
    risk_sums = defaultdict(lambda: 20 * len(graph))
    risk_sums[(0,0)] = 0
    x = 0
    y = 0
    while True:
        print(len(visited))
        if x == len(graph) - 1 and y == len(graph) - 1:
            break

        if not visited[(x+1,y)] and x < len(graph) - 1 and risk_sums[(x+1,y)] > risk_sums[(x, y)] + graph[x+1][y]:
            risk_sums[(x+1,y)] = risk_sums[(x, y)] + graph[x+1][y]
        if not visited[(x, y+1)] and y < len(graph) - 1 and risk_sums[(x,y+1)] > risk_sums[(x, y)] + graph[x][y+1]:
            risk_sums[(x,y+1)] = risk_sums[(x, y)] + graph[x][y+1]

        #print(x,y, risk_sums[(x,y)])
        visited[(x,y)] = True
        #unvisited.remove((x,y))
        del risk_sums[(x,y)]

        r_sums = min(risk_sums.values())
        res = [key for key in risk_sums if not visited[key] and risk_sums[key] == r_sums]

        #print(risk_sums)

        #print(visited)
        #print(risk_sums)
        #print(res)
        x,y = res[0]

    print(len(graph) - 1, len(graph) - 1, risk_sums[(len(graph)-1, len(graph) - 1)])
"""
    risk_sums = defaultdict(lambda: 20 * len(graph))
    current_minimum = 20 * len(graph)
    def distance_to_end(x, y, running_sum):
        x_dist = len(graph) - x
        y_dist = len(graph) - y

        return running_sum + x_dist + y_dist

    def shortest_path(x, y, running_sum):
        global current_minimum
        if current_minimum < distance_to_end(x, y, running_sum):
            return 20 * len(graph)
        if x == len(graph) or y == len(graph[x]):
            return 20 * len(graph)
        if x == len(graph) - 1 and y == len(graph[x]) - 1:
            if running_sum < current_minimum:
                current_minimum = running_sum
            return running_sum

        #print(x, y, current_minimum, running_sum)

        # print(risk_sums[(x,y)], graph[x][y], min(risk_sums[(x,y)], graph[x][y]))
        if risk_sums[(x,y)] <= running_sum + graph[x][y]:
            return 20 * len(graph)

        subtotal = running_sum + graph[x][y]
        risk_sums[(x,y)] = subtotal
        #print(risk_sums[(x,y)])

        # print("--", x,y, current_total)j

        sp1 = shortest_path(x + 1, y, subtotal)
        sp2 = shortest_path(x, y + 1, subtotal)

        #if sp1 < sp2 and sp1 != 2000:
        #    print(x, y, graph[x][y], sp1)
        #elif sp2 != 2000:
        #    print(x, y, graph[x][y], sp2)

        # print(x + 1, y, sp1)
        # print(x, y + 1, sp2)
        return min(sp1, sp2)

    risk_sums[(0, 0)] = 0
    current_minimum = 20 * len(graph)
    print(shortest_path(0, 1, 0))
    current_minimum = 20 * len(graph)
    print(shortest_path(1, 0, 0))
"""
