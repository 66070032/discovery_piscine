def is_valid(rows):
    if len(rows) == 0:
        return False
    for row in rows:
        if len(row) != len(rows):
            return False
    king_count = 0
    for row in rows:
        king_count += row.count("K")
    return king_count == 1


def find_king(rows):
    for y in range(len(rows)):
        for x in range(len(rows)):
            if rows[y][x] == "K":
                return y, x
    return None


def first_piece(rows, y, x, dy, dx):
    size = len(rows)
    y += dy
    x += dx
    while 0 <= y < size and 0 <= x < size:
        if rows[y][x] in "PBRQ":
            return rows[y][x]
        y += dy
        x += dx
    return None


def attacked_by_pawn(rows, y, x):
    size = len(rows)
    below = y + 1
    if below >= size:
        return False
    if x - 1 >= 0 and rows[below][x - 1] == "P":
        return True
    if x + 1 < size and rows[below][x + 1] == "P":
        return True
    return False


def attacked_by_slider(rows, y, x):
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dy, dx in straight:
        if first_piece(rows, y, x, dy, dx) in ("R", "Q"):
            return True
    for dy, dx in diagonal:
        if first_piece(rows, y, x, dy, dx) in ("B", "Q"):
            return True
    return False


def checkmate(board):
    if not isinstance(board, str):
        print("Error")
        return
    rows = board.splitlines()
    if not is_valid(rows):
        print("Error")
        return
    y, x = find_king(rows)
    if attacked_by_pawn(rows, y, x) or attacked_by_slider(rows, y, x):
        print("Success")
    else:
        print("Fail")
