from collections import defaultdict

with open("input.txt") as pol:
    template = pol.readline().rstrip()
    pol.readline()

    rules = {}
    while (insert := pol.readline().rstrip()):
        cond, eff = insert.split(' -> ')
        rules[cond] = eff

    total_char_count = defaultdict(int)
    for char in template:
        total_char_count[char] += 1

    depth_breakdown = {}

    depth = 40
    def string_boost(string, inserts):
        if inserts == 0:
            return {}


        if string in depth_breakdown and inserts in depth_breakdown[string]:
            return depth_breakdown[string][inserts]

        insert = rules[string]

        string1 = string[0] + insert
        char_count1 = string_boost(string1, inserts - 1)

        string2 = insert + string[1]
        char_count2 = string_boost(string2, inserts - 1)

        char_count = defaultdict(int)
        char_count[insert] = 1
        for cc in char_count1:
            char_count[cc] += char_count1[cc]
        for cc in char_count2:
            char_count[cc] += char_count2[cc]

        if string not in depth_breakdown:
            depth_breakdown[string] = {}

        if inserts not in depth_breakdown[string]:
            depth_breakdown[string][inserts] = {}

        depth_breakdown[string][inserts] = char_count.copy()

        return char_count

    for x in range(len(template) - 1):
        for cc, vv in string_boost(template[x: x + 2], depth).items():
            total_char_count[cc] += vv

    for k, v in total_char_count.items():
        continue
        print(f"{k} - {v}")

    print(max(total_char_count.values()) - min(total_char_count.values()))
