""" Solution for Day 18 """

import numpy as np
from advent import Advent, Runner, file_to_string


class Day18(Advent):
    """ class for Day 18 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "18"
        self.lines = input_text
        self.initial_state = []

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            line_arr = [ch for ch in tmp]
            self.initial_state.append(line_arr)

    def count_neighbors(self, arr, row, col):
        """ count neighbors """
        min_r, max_r = 0, arr.shape[0]
        min_c, max_c = 0, arr.shape[1]
        res = 0
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        for d_x, d_y in dirs:
            new_r = row + d_y
            new_c = col + d_x
            if min_r <= new_r < max_r and min_c <= new_c < max_c:
                # if new_r in range(arr.shape[0]) and new_c in range(arr.shape[1]):
                if arr[new_r, new_c] == '#':
                    res += 1
        return res

    def animate_step(self, board, output=False):
        """ animate one step """
        new_board = np.full_like(board, '.')
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if output:
                    print(board[row, col], ' ', end='')
                neighbors = self.count_neighbors(board, row, col)
                if board[row, col] == '#':
                    if neighbors in [2, 3]:
                        new_board[row, col] = '#'
                elif board[row, col] == '.':
                    if neighbors == 3:
                        new_board[row, col] = '#'
            if output:
                print()
        return new_board

    def new_animate_step(self, board, output=False):
        """ animate a time step the new way """
        new_board = np.full_like(board, '.')
        new_board[0, 0] = '#'
        new_board[0, board.shape[1]-1] = '#'
        new_board[board.shape[0]-1, 0] = '#'
        new_board[board.shape[0]-1, board.shape[1]-1] = '#'
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if output:
                    print(board[row, col], ' ', end='')
                neighbors = self.count_neighbors(board, row, col)
                if board[row, col] == '#':
                    if neighbors in [2, 3]:
                        new_board[row, col] = '#'
                elif board[row, col] == '.':
                    if neighbors == 3:
                        new_board[row, col] = '#'
            if output:
                print()
        return new_board

    def count_lights(self, board):
        """ count the number of lit lights on the board """
        cnt = 0
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                if board[row, col] == '#':
                    cnt += 1
        return cnt

    def part_one(self, limit=100, output=False):
        board = np.array(self.initial_state)
        for ctr in range(limit):
            board = self.animate_step(board, output=output)
            if output:
                print(
                    f"After {ctr+1} steps {self.count_lights(board)} lights are on")
        total = self.count_lights(board)
        print(f"After {limit} steps {total} lights are on")
        return total

    def part_two(self, limit=100, output=False):
        board = np.array(self.initial_state)
        board[0, 0] = '#'
        board[0, board.shape[1]-1] = '#'
        board[board.shape[0]-1, 0] = '#'
        board[board.shape[0]-1, board.shape[1]-1] = '#'
        for ctr in range(limit):
            board = self.new_animate_step(board, output=output)
            if output:
                print(
                    f"After {ctr+1} steps {self.count_lights(board)} lights are on")
        total = self.count_lights(board)
        print(f"After {limit} steps {total} lights are on")
        return total


def main():
    """ stub for main() """
    aoc1 = Day18(file_to_string("day18-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
