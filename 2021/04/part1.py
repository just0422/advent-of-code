def play_bingo():
    with open("input.txt") as bingo_details:
        moves = bingo_details.readline().rstrip().split(',')

        board_no = -1
        row_count = 0
        col_count = 0
        boards = {}
        boards_row_col = {}
        while (line:= bingo_details.readline()):
            if len(line) == 1:
                row_count = 0
                board_no += 1
                boards[board_no] = {}
                continue

            line = line.rstrip()

            col_count = 0
            for cell in line.split():
                boards[board_no][cell] = (row_count, col_count)
                col_count += 1

            row_count += 1

        board_count = board_no + 1
        for board in range(board_count):
            boards_row_col[board] = {}
            boards_row_col[board]['rows'] = [0] * row_count
            boards_row_col[board]['cols'] = [0] * col_count

        finished = False
        for move in moves:
            for board in range(board_count):
                if move not in boards[board]:
                    continue
                move_row, move_col = boards[board].pop(move, None)

                boards_row_col[board]['rows'][move_row] += 1
                boards_row_col[board]['cols'][move_col] += 1

                unmarked = []
                if boards_row_col[board]['rows'][move_row] == col_count:
                    unmarked = [int(x) for x in boards[board]]
                    finished = True
                elif boards_row_col[board]['cols'][move_col] == row_count:
                    unmarked = [int(x) for x in boards[board]]
                    finished = True

                if finished:
                    print(board, unmarked)
                    print(int(move), sum(unmarked))
                    print(int(move) * sum(unmarked))
                    return


play_bingo()
