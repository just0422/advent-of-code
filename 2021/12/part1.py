from collections import defaultdict

with open("input.txt") as caves:
    graph = defaultdict(list)
    while (path := caves.readline().rstrip()):
        endpoints = path.split('-')
        graph[endpoints[0]].append(endpoints[1])
        graph[endpoints[1]].append(endpoints[0])

    print(graph)

    def traverse(cave, current_path):
        if cave == "end":
            print(current_path)
            return 1

        result = 0
        for next_cave in graph[cave]:
            if next_cave.isupper() or (next_cave.islower() and next_cave not in current_path):
                result += traverse(next_cave, current_path + [next_cave])
        return result

    print(traverse("start", ["start"]))
