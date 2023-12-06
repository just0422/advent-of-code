import sys
import math

directory = sys.argv[1]
files = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

# seeds = [1848591090, 462385043, 2611025720, 154883670, 1508373603, 11536371, 3692308424, 16905163, 1203540561, 280364121, 3755585679, 337861951, 93589727, 738327409, 3421539474, 257441906, 3119409201, 243224070, 50985980, 7961058]
seeds = [79, 14, 55, 13]
seed = 13

class AlmanacMapping:
    def __init__(self, line):
        self.min = int(line[1])
        self.max = self.min + int(line[2]) - 1

        self.offset = int(line[0]) - self.min

    def get_dest(self, src):
        return src + self.offset

    def __contains__(self, x):
        return self.min <= x <= self.max

    def __str__(self):
        return f"{self.min}-{self.max} {self.offset}"

    def __repr__(self):
        return f"{self.min}-{self.max} {self.offset}"

final = -1
seed_to_loc = {}
for seed in seeds:
    value = seed
    maps = {f"{files[x]}-to-{files[x+1]}": [] for x in range(len(files) - 1)}
    for x in range(len(files) - 1):
        stage = f"{files[x]}-to-{files[x+1]}"
        with open(f"{directory}/{stage}.txt", "r") as almanac_file:
            while (line := almanac_file.readline().rstrip()):
                mapping = AlmanacMapping(line.split(" "))

                maps[stage].append(mapping)

        for mapping in maps[stage]:
            if value in mapping:
                value = mapping.get_dest(value)
                break

        # print(files[x+1], value)

    seed_to_loc[seed] = value


sorted_dict = dict(sorted(seed_to_loc.items(), key=lambda item: item[1]))
for key, value in sorted_dict.items():
    print(f"{key} - {value}")
