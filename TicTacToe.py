from random import randrange

def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  " ,board[0][1],"  |  " ,board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  " , board[1][0] , "  |  " , board[1][1] , "  |  " , board[1][2] , "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  " , board[2][0] , "  |  " , board[2][1] , "  |  " , board[2][2] , "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
    while True:
        move=-1
        DrawMove(board)
        print("Computer's movement")
        DisplayBoard(board)
        if VictoryFor(board, "X")==True:
            return
        freeSquares=MakeListOfFreeFields(board)
        while move not in freeSquares:
            move=int(input("Enter you movement: "))
            if move==11:
                return
            if move not in freeSquares:
                print("Your movement is incorrect!!!")
        for row in range(3):
            for column in range(3):
                if move==board[row][column]:
                    board[row][column]="O"
                    print("Your movement")
                    DisplayBoard(board)
                    if VictoryFor(board,"O")==True:
                        return

def MakeListOfFreeFields(board):
    freeSquare=[]
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X","O"]:
                freeSquare.append(board[row][column])
    return freeSquare

def VictoryFor(board, sign):
    countDiagonal1 = 0
    countDiagonal2 = 0
    for row in range(3):
        countRows=0
        countColumns = 0
        for column in range(3):
            if (row==column and board[row][column]==sign):
                countDiagonal2+=1
            if (row+column==2 and board[column][row]==sign):
                countDiagonal1+=1
            if board[row][column]==sign:
                countRows+=1
            if board[column][row] == sign:
                countColumns += 1
            if countColumns == 3 or countRows==3 or countDiagonal1==3 or countDiagonal2==3:
                if sign == "O":
                    print("You Win!!!")
                    return True
                else:
                    print("Computer's Win!!!")
                    return True

    freeSquares=MakeListOfFreeFields(board)
    if len(freeSquares)<1:
        print("Tieeeee !!!")
        return True

def DrawMove(board):
    #First computer movement
    computerMovement=5
    freeSquares=MakeListOfFreeFields(board)
    while computerMovement not in freeSquares:
        computerMovement=randrange(1,10)
    for row in range(3):
        for column in range(3):
            if computerMovement == board[row][column]:
                board[row][column] = "X"


board = [[0 for row in range(3)] for column in range(3)]
i = 1
for row in range(3):
    for column in range(3):
        board[row][column] = i
        i += 1

MakeListOfFreeFields(board)
EnterMove(board)