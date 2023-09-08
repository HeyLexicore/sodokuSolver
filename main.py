import numpy as np

board = np.array([
    [0, 4, 0, 0, 0, 2, 8, 0, 0],
    [2, 0, 8, 0, 0, 0, 3, 5, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 6],
    [0, 0, 5, 7, 0, 4, 2, 0, 9],
    [7, 0, 4, 0, 0, 6, 0, 0, 5],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 6, 4, 7, 0, 0, 0],
    [0, 0, 0, 2, 0, 9, 6, 0, 0],
    [0, 6, 0, 8, 5, 0, 0, 9, 0],
], dtype=object)


def print_board(board, full):
    for j in range(9):
        for k in range(9):
            if full:
                print(board[j, k], end="|")
            else:
                if type(board[j, k]) != int:
                    print(" ", end="|")
                else:
                    print(board[j, k], end="|")
        print()

def prep(sodoku):
    sodoku = sodoku.copy()

    for j in range(9):
        for k in range(9):
            if sodoku[j, k] == 0:
                sodoku[j, k] = np.arange(9) + 1
    print_board(sodoku, False)
    return sodoku

def run(sodoku: np.ndarray):

    for j in range(9):
        for k in range(9):
            if type(sodoku[j, k]) == np.ndarray:
                hori = sodoku[j]
                hori = [x for x in hori if type(x) == int]

                verti = sodoku[:, k]
                verti = [x for x in verti if type(x) == int]

                sqare = sodoku[int(np.floor(j / 3) * 3):int((np.floor(j / 3) + 1) * 3),
                        int(np.floor(k / 3) * 3):int((np.floor(k / 3) + 1) * 3)].flatten()
                sqare = [x for x in sqare if type(x) == int]

                hori.extend(verti)
                hori.extend(sqare)

                lets = np.array(list(set(list(hori))))

                rem = np.array([x for x in sodoku[j, k] if x not in lets])

                sodoku[j, k] = rem

    result = np.empty_like(sodoku, dtype=object)

    for i in range(9):
        for j in range(9):
            element = sodoku[i, j]

            if isinstance(element, np.ndarray) and element.size == 1:
                result[i, j] = int(element[0])
            else:
                result[i, j] = element
    print()
    print_board(result, False)
    sodoku = result
    sum = 0
    for j in range(9):
        for k in range(9):

            if type(result[j, k]) == int:
                sum += result[j, k]
    print(sum)
    if sum == 405:
        pass
    else:
        run(sodoku)

run(prep(board))
