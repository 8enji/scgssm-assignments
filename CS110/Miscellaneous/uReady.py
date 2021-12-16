def valid_solution(board):
    print(board)
    output = True
    goal = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i in range(9):
        setx = set()
        sety = set()
        for j in range(9):
            setx.add(board[i][j])
            sety.add(board[j][i])
        if setx != goal or sety != goal:
            output = False
        # print(sumx, sumy)
    for x in [0, 3, 6]:
        setz = set()
        for i in range(3):
            for j in range(3):
                setz.add(board[i + x][j + x])
                setz.add(board[i + x][j + x])
        print(setz)
        if setz != goal:
            output = False

    return output
