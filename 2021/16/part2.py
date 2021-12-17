from collections import defaultdict

with open("input.txt") as hex_codes:
    hex_line = hex_codes.readline().rstrip()
    bin_line = bin(int(hex_line, 16))[2:].zfill(4*len(hex_line))

    print(bin_line)

    version_total = 0

    def calculate_value(values, type_id):
        final_value = 0
        print(f"\n\n{values=}")
        if type_id == 0:
            print(f"{sum(values)=}")
            final_value = sum(values)
        if type_id == 1:
            f_val = 1
            for value in values:
                f_val *= value
            final_value = f_val
            print(f"product(values)={f_val}")
        if type_id == 2:
            final_value = min(values)
            print(f"{min(values)=}")
        if type_id == 3:
            final_value = max(values)
            print(f"{max(values)=}")
        if type_id == 5:
            final_value = 1 if values[0] > values[1] else 0
            print(f"gt - {values[0]} > {values[1]} = {final_value}")
        if type_id == 6:
            final_value = 1 if values[0] < values[1] else 0
            print(f"lt - {values[0]} < {values[1]} = {final_value}")
        if type_id == 7:
            final_value = 1 if values[0] == values[1] else 0
            print(f"eq - {values[0]} == {values[1]} = {final_value}")

        return final_value


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

        print(f"{literal=}")
        if not bin_line:
            bin_line = ""
        return literal, bin_line

    def packet(bin_line):
        global version_total
        if len(bin_line) < 8:
            return None, None

        version = int(bin_line[:3], 2)
        version_total += version
        type_id = int(bin_line[3:6], 2)
        bin_line = bin_line[6:]

        print()
        print(f"{version=} - {version:03b}, {type_id=} - {type_id:03b}")
        values = []
        if type_id == 4:
            return literal(bin_line)
        else:
            sub_values = []
            length_type = bin_line[0]
            print(f"{length_type=}")
            if int(length_type) == 0:
                sub_packet_length = int(bin_line[1:16], 2)
                print(f"{sub_packet_length=}")
                bin_line = bin_line[16:]

                sub_packets = bin_line[:sub_packet_length]
                bin_line = bin_line[sub_packet_length:]

                while len(sub_packets) > 0:
                    val, sub_packets = packet(sub_packets)
                    values.append(val)
            else:
                sub_packet_count = int(bin_line[1:12], 2)
                print(f"{sub_packet_count=}")
                bin_line = bin_line[12:]

                for _ in range(sub_packet_count):
                    val, bin_line = packet(bin_line)
                    values.append(val)

            return calculate_value(values, type_id), bin_line
    print(packet(bin_line)[0])
