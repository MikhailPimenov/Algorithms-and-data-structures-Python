from others.loopover.point.point import Point


def replace_2_board_cells(board: list, start: Point, finish: Point):
    temp = board[start.row][start.column]
    board[start.row][start.column] = board[finish.row][finish.column]
    board[finish.row][finish.column] = temp


def update_search_board(board: list, search_board: dict, start: Point, finish: Point):
    search_board[board[start.row][start.column]] = finish
    search_board[board[finish.row][finish.column]] = start


def swap2(
        board: list,
        start: Point,
        finish: Point,
        to_beginning: str,
        to_end: str,
        length: int,
        moves: list,
        search_board: dict,
):
    update_search_board(board, search_board, start, finish)
    replace_2_board_cells(board, start, finish)

    if to_beginning == 'L':
        base_direction = 'D'
        position_along = start.column
        position_perpendicular = start.row
    else:
        base_direction = 'R'
        position_along = start.row
        position_perpendicular = start.column

    for i in range(length):
        moves.append(f'{base_direction}{position_along}')
        moves.append(f'{to_beginning if i % 2 else to_end}{position_perpendicular}')

    moves.append(f'{base_direction}{position_along}')
