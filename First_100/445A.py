# 445A - DZY loves chessboard
n, m = map(int, input().split())
board = [list(input()) for i in range(n)]
color = ['W', 'B']
for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            board[i][j] = color[(i+j) % 2]
for row in board:
    print(''.join(row))