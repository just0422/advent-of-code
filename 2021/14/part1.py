from collections import defaultdict

with open("input.txt") as pol:
    template = pol.readline().rstrip()
    pol.readline()

    rules = {}
    while (insert := pol.readline().rstrip()):
        cond, eff = insert.split(' -> ')
        rules[cond] = eff

    char_count = defaultdict(int)
    for char in template:
        char_count[char] += 1
    for _ in range(10):
        for x in range(len(template) - 1, 0, -1):
            sub_str = template[x-1:x+1]

            insert = rules[sub_str]
            char_count[insert] += 1


            template = template[:x] + insert + template[x:]

    for k, v in char_count.items():
        print(f"{k} - {v}")

    print(max(char_count.values()) - min(char_count.values()))
