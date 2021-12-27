import sys
import numpy as np


def count_neighbors(arr, r, c):
    res = 0
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in dir:
        new_r = r + dy
        new_c = c + dx
        if new_r in range(arr.shape[0]) and new_c in range(arr.shape[1]):
            if arr[new_r, new_c] == '#':
                res += 1
    return res


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    initial_state = []
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            line_arr = [ch for ch in tmp]
            initial_state.append(line_arr)

    board = np.array(initial_state)
    print(f"{board}")
    step = 0

    for ctr in range(100):
        board = animate_step(board)
        step += 1
        print(f"After {step} steps {count_lights(board)} lights are on")


def animate_step(board):
    new_board = np.full_like(board, '.')
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            # print(board[r, c], ' ', end='')
            neighbors = count_neighbors(board, r, c)
            if board[r, c] == '#':
                if neighbors in [2, 3]:
                    new_board[r, c] = '#'
            elif board[r, c] == '.':
                if neighbors == 3:
                    new_board[r, c] = '#'
    return new_board


def count_lights(board):
    cnt = 0
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if board[r, c] == '#':
                cnt += 1
    return cnt


if __name__ == '__main__':
    main()