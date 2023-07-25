from advent import Advent, Runner, File_to_String
import numpy as np
import sys


class Day18(Advent):
    def __init__(self, input_text):
        self.name = "18"
        self.lines = input_text
        self.initial_state = []

    def parse(self):
        initial_state = []
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            line_arr = [ch for ch in tmp]
            self.initial_state.append(line_arr)

    def count_neighbors(self, arr, r, c):
        min_r, max_r = 0, arr.shape[0]
        min_c, max_c = 0, arr.shape[1]
        res = 0
        dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in dir:
            new_r = r + dy
            new_c = c + dx
            if min_r <= new_r < max_r and min_c <= new_c < max_c:
                # if new_r in range(arr.shape[0]) and new_c in range(arr.shape[1]):
                if arr[new_r, new_c] == '#':
                    res += 1
        return res

    def animate_step(self, board, output=False):
        new_board = np.full_like(board, '.')
        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                if output:
                    print(board[r, c], ' ', end='')
                neighbors = self.count_neighbors(board, r, c)
                if board[r, c] == '#':
                    if neighbors in [2, 3]:
                        new_board[r, c] = '#'
                elif board[r, c] == '.':
                    if neighbors == 3:
                        new_board[r, c] = '#'
            if output:
                print()
        return new_board

    def new_animate_step(self, board, output=False):
        new_board = np.full_like(board, '.')
        new_board[0, 0] = '#'
        new_board[0, board.shape[1]-1] = '#'
        new_board[board.shape[0]-1, 0] = '#'
        new_board[board.shape[0]-1, board.shape[1]-1] = '#'
        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                if output:
                    print(board[r, c], ' ', end='')
                neighbors = self.count_neighbors(board, r, c)
                if board[r, c] == '#':
                    if neighbors in [2, 3]:
                        new_board[r, c] = '#'
                elif board[r, c] == '.':
                    if neighbors == 3:
                        new_board[r, c] = '#'
            if output:
                print()
        return new_board

    def count_lights(self, board):
        cnt = 0
        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                if board[r, c] == '#':
                    cnt += 1
        return cnt

    def partA(self, limit=100, output=False):
        board = np.array(self.initial_state)
        for ctr in range(limit):
            board = self.animate_step(board, output=output)
            if output:
                print(
                    f"After {ctr+1} steps {self.count_lights(board)} lights are on")
        total = self.count_lights(board)
        print(f"After {limit} steps {total} lights are on")
        return total

    def partB(self, limit=100, output=False):
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

        return None


def main():
    aoc1 = Day18(File_to_String("day18-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
