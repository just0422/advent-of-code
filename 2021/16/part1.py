from collections import defaultdict

with open("input.txt") as hex_codes:
    hex_line = hex_codes.readline().rstrip()
    bin_line = bin(int(hex_line, 16))[2:].zfill(4*len(hex_line))

    print(bin_line)

    version_total = 0

    def literal(bin_line):
        literal = 0b0
        count = 0
        while True:
            count += 1
            literal <<= 4
            literal |= int(bin_line[1:5], 2)

            bit_0 = bin_line[0]
            bin_line = bin_line[5:]

            if int(bit_0) == 0:
                break

        #bin_length = count * 5
        #total_bin = int(int((bin_length + 3) / 4) * 4)
        #left_over = total_bin - bin_length

        print(f"{literal=}")
        if not bin_line:
            bin_line = ""
        #print(total_bin, bin_length, left_over)
        #bin_line = bin_line[left_over:]
        #print(count, bin_line)
        #bin_line = bin_line[count*5:]
        return literal, bin_line

    def packet(bin_line):
        global version_total
        if len(bin_line) == 0 or int(bin_line, 2) == 0:
            return 0, ""

        version = int(bin_line[:3], 2)
        version_total += version
        type_id = int(bin_line[3:6], 2)
        bin_line = bin_line[6:]

        print()
        print(f"{version=} - {version:03b}, {type_id=} - {type_id:03b}")
        print(bin_line)
        if type_id == 4:
            return literal(bin_line)
        else:
            length_type = bin_line[0]
            print(f"{length_type=}")
            if int(length_type) == 0:
                sub_packet_length = int(bin_line[1:16], 2)
                print(f"{sub_packet_length=}")
                bin_line = bin_line[16:]

                sub_packets = bin_line[:sub_packet_length]
                bin_line = bin_line[sub_packet_length:]

                while len(sub_packets) > 0:
                    _, sub_packets = packet(sub_packets)
            else:
                sub_packet_count = int(bin_line[1:12], 2)
                print(f"{sub_packet_count=}")
                bin_line = bin_line[12:]

                for i in range(sub_packet_count):
                    _, bin_line = packet(bin_line)

        if len(bin_line) > 0:
            return packet(bin_line)
        return -1, ""

    packet(bin_line)
    print(version_total)
