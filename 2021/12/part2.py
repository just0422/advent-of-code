
from collections import defaultdict

with open("input.txt") as caves:
    graph = defaultdict(list)
    while (path := caves.readline().rstrip()):
        endpoints = path.split('-')
        graph[endpoints[0]].append(endpoints[1])
        graph[endpoints[1]].append(endpoints[0])

    def check_lower_caves(next_cave, current_path):
        if next_cave == "start":
            return False

        if current_path.count(next_cave) == 0:
            return True

        for cave in graph:
            if cave.islower() and current_path.count(cave) >= 2:
                return False

        return True

    def traverse(cave, current_path):
        if cave == "end":
            return 1

        result = 0
        for next_cave in graph[cave]:
            if next_cave.isupper() or check_lower_caves(next_cave, current_path):
                result += traverse(next_cave, current_path + [next_cave])
        return result

    print(traverse("start", ["start"]))
