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


    rowList = [1,2,3,4,5,6,7,8,9]
    rowListLen = len(rowList)-1

    row=0
    rowIt=0
    column = 0
    while(column !=len(board)):
        while(rowIt !=len(board)):
            randomNum = random.choice(rowList)
            board[column][row] = randomNum
            rowList.remove(randomNum)
            row+=1


            if not rowList:
                rowList = [1,2,3,4,5,6,7,8,9]
                row=0
                rowIt += 1
                column+=1

    # for column in range(len(board)):
    #     row = 0
    #     if column==0 or column==1 or column==2:
    #         while(row != 9):
    #             randomNum = random.randint(1,9)
    #             if isUniqueRow(randomNum,board,column) and isUniqueCol(randomNum,board,column,row) :
    #                # and \
    #                # isUniqueBox(randomNum,board,column,row):
    #                 board[column][row] = randomNum
    #                 row +=1




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





def isUniqueRow(number,board,column):
    if number != board[column][0] and \
       number != board[column][1] and \
       number != board[column][2] and \
       number != board[column][3] and \
       number != board[column][4] and \
       number != board[column][5] and \
       number != board[column][6] and \
       number != board[column][7]:
        return True





def isUniqueCol(number,board,column,row):
    if column ==0:
        return True
    elif column==1:
        return number != (board[column-1][row])
    elif column==2:
        return \
            number!=(board[column-1][row]) and \
            number!=(board[column-2][row])






def isUniqueBox(number,board,column,row):
    box1 = [[0,1,2],[0,1,2]]
    box2 = [[0,1,2],[3,4,5]]
    box3 = [[0,1,2],[6,7,8]]

    return True




def main():
    board = populateBoard()
    printBoard(board)


main()
