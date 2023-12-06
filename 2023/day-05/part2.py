import sys
import math

directory = sys.argv[1]
files = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

seeds = [1848591090, 462385043, 2611025720, 154883670, 1508373603, 11536371, 3692308424, 16905163, 1203540561, 280364121, 3755585679, 337861951, 93589727, 738327409, 3421539474, 257441906, 3119409201, 243224070, 50985980, 7961058]
# seeds = [79, 14, 55, 13]
seed = 13

class AlmanacMapping:
    def __init__(self, line):
        self.min = int(line[1])
        self.max = self.min + int(line[2]) - 1

        self.offset = int(line[0]) - self.min

    def get_dest(self, src):
        return src + self.offset

    def difference(self, x):
        return self.max - x

    def __contains__(self, x):
        return self.min <= x <= self.max

    def __str__(self):
        return f"{self.min}-{self.max} {self.offset}"

    def __repr__(self):
        return f"{self.min}-{self.max} {self.offset}"

maps = {f"{files[x]}-to-{files[x+1]}": [] for x in range(len(files) - 1)}
for x in range(len(files) - 1):
    stage = f"{files[x]}-to-{files[x+1]}"
    with open(f"{directory}/{stage}.txt", "r") as almanac_file:
        while (line := almanac_file.readline().rstrip()):
            mapping = AlmanacMapping(line.split(" "))

            maps[stage].append(mapping)

final = -1
seed_to_loc = {}
for y in range(0, len(seeds) - 1, 2):
    seed = seeds[y]
    while seed < seeds[y] + seeds[y + 1]:
        value = seed
        smallest_diff = seeds[y + 1]
        for x in range(len(files) - 1):
            stage = f"{files[x]}-to-{files[x+1]}"
            for mapping in maps[stage]:
                if value in mapping:
                    smallest_diff = min(mapping.difference(value), smallest_diff)
                    value = mapping.get_dest(value)
                    break

        seed += smallest_diff + 1
        seed_to_loc[seed] = value

min_key = min(seed_to_loc, key=seed_to_loc.get)
print(seed_to_loc[min_key])
