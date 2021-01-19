import random


def fillBoard(board):

    emptyBox = findEmpty(board)

    if not emptyBox:
        return True
    else:
        row,column = emptyBox

    possibleNumbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(possibleNumbers)

    for i in possibleNumbers:
        if isUnique(board, i,( row, column)):
            board[row][column] = i

            if fillBoard(board):
                return True

            board[row][column] = 0

    return False






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










def isUnique(board,number,position):

    # Check Row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] !=i:
            return False


    # Check Column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False


    # Check Box
    xBox = position[1] // 3
    yBox = position[0] // 3

    for i in range(yBox*3, yBox*3+3):
        for j in range(xBox*3, xBox*3+3):
            if board[i][j] == number and (i,j) !=position:
                return False


    return True








def findEmpty(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return (row,column)

    return None


def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    fillBoard(board)
    printBoard(board)


main()