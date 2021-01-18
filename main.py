import random


def populateBoard():
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    row=0

    rowArry = []
    colArray = []

    while(row != 9):
        randomNum = random.randint(1,9)

        if randomNum in rowArry:
            randomNum = random.randint(1,9)
        else:
            board[0][row] = randomNum
            rowArry.append(randomNum)
            row+=1




    return board


def printBoard(board):
    drawLine = (3,6)
    print('')
    for i in range(len(board)):
        if i in drawLine:
            print('---------------------')

        for j in range(len(board[0])):
            if j in drawLine:
                print('|', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

    print('')






def main():
    board = populateBoard()
    printBoard(board)



main()
