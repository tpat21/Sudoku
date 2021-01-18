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



    # for i in range(len(board)):
    #     row=0
    #     rowArry = []
    #     colArray = []
    #     if i==0:
    #         while(row != 9):
    #             randomNum = random.randint(1,9)
    #
    #             if randomNum in rowArry:
    #                 randomNum = random.randint(1,9)
    #             else:
    #                 board[i][row] = randomNum
    #                 rowArry.append(randomNum)
    #                 row+=1


    for i in range(len(board)):
        row = 0
        while(row != 9):

            randomNum = random.randint(1,9)
            if isUniqueRow(randomNum,board):
                board[0][row] = randomNum
                row +=1






        #
        # for j in range(len(board)):
        #     # if isUniqueRow(randomNum,board) and isUniqueCol(randomNum,board) and isUniqueBox(randomNum,board):
        #         board[i][j] = randomNum
        #     else:
        #         randomNum = random.randint(1,9)











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





def isUniqueRow(number,board):
    if number ==3:
        return False
    else:
        return True

def isUniqueCol(number,board):
    return True

def isUniqueBox(number,board):
    return True




def main():
    board = populateBoard()
    printBoard(board)



main()
