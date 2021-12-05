from typing import List
import numpy as np


def check_if_won(board: List) -> bool:
    for row in board:
        if sum(row) == -5:
            return True
    for column in np.transpose(board):
        i = sum(column)
        if i == -5:
            return True
    return False


def update_board(board: List, bingo_number: int) -> List:
    updated_board = board
    for row_idx, row in enumerate(board):
        for col_idx, number in enumerate(row):
            if number == bingo_number:
                updated_board[row_idx][col_idx] = -1
    return updated_board


def board_score(board: List, bingo_number: int) -> int:
    total = 0
    for row in board:
        for number in row:
            if number != -1:
                total += number

    return total * bingo_number


if __name__ == "__main__":
    numbers = open("input.txt", "r").read().splitlines()
    bingo_numbers = list(map(int, numbers[0].split(',')))

    bingo_boards = []
    new_bingo_board = []
    for line in numbers[2:]:
        if line == "":
            bingo_boards.append(new_bingo_board)
            new_bingo_board = []
        else:
            row_numbers = list(map(int, line.split()))
            new_bingo_board.append(row_numbers)

    winning_board = []
    board_has_won = []
    for number in bingo_numbers:
        for bingo_index, board in enumerate(bingo_boards):
            updated_board = update_board(board, number)
            is_winner = check_if_won(updated_board)
            if is_winner:
                winning_board = updated_board
                print(winning_board)
                print(number)
                board_score(winning_board, number)
            bingo_boards[bingo_index] = updated_board

    print(winning_board)
