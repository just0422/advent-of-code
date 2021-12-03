with open("input.txt") as depths:
    line_count = 0

    diagnostics = depths.read().splitlines()
    diagnostic_length = len(diagnostics[0])

    def find_diagnostic(diags, i, least):
        if i == diagnostic_length or len(diags) == 1:
            return diags[0]

        ones = []
        zeroes = []
        for diag in diags:
            if diag[i] == "1":
                ones.append(diag)
            else:
                zeroes.append(diag)

        ones_over_zeroes = len(ones) >= len(zeroes)
        if least:
            ones_over_zeroes = not ones_over_zeroes

        if ones_over_zeroes:
            return find_diagnostic(ones, i + 1, least)
        else:
            return find_diagnostic(zeroes, i + 1, least)

    o2 = find_diagnostic(diagnostics, 0, False)
    co2 = find_diagnostic(diagnostics, 0, True)

    print(o2, int(o2, 2))
    print(co2, int(co2, 2))

    print(int(o2,2) * int(co2, 2))
"""
    o2 = ""
    co2 = ""
    for i in range(len(diagnostics[0])):
        ones = 0
        zeroes = 0
        for diag in diagnostics:
            if diag[i] == "1":
                ones += diag
            else:
                zeroes += diag

        if ones >= zeroes:
            o2 += "1"
            co2 += "0"
        else:
            o2 += "0"
            co2 += "1"

"""
