# Python Tic-Tac-Toe
# Started: 01/07/2020
# Last Worked On: 01/08/2020



import math
import time




board = ["_" for x in range(0, 9)]

human = "O"
ai = "X"



#counts how many winning moves there are
def winningMoves(grid, player):
    row1, row2, row3 = (rowmaker(grid))
    
    column1, column2, column3 = (columnmaker(grid))
    
    cross1, cross2 = (crossmaker(grid))
    
    totalLists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    counter = 0
    for i in range(len(totalLists)):
        result = winNextTurn(totalLists[i], player)
        if (result):
            counter += 1
        else:
            continue

    return counter

            
    

# inserts letter into board    
def insertLetter(letter, pos, grid):
    grid[pos] = letter
    return grid

    
       

# checks if board is full
def fullBoard(grid):    
    if (grid.count("_") >= 1):
        return False
    else:
        return True


    
# produces a list of empty spots in the board
def emptySpots(grid):
    lstOfEmpty = []
    for i in range(len(grid)):
        if (grid[i] == "_"):
            lstOfEmpty.append(i)
        else:
            continue
    return lstOfEmpty





# produces clean version of board
def printBoard(grid):
    print ("-------------")
    print ("| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print ("-------------")
    print ("| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print ("-------------")
    print ("| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print ("-------------")



# splits the board into 3 rows
def rowmaker(grid):
    row1 = [grid[0], grid[1], grid[2]]
    row2 = [grid[3], grid[4], grid[5]]
    row3 = [grid[6], grid[7], grid[8]]
    return row1, row2, row3



# splits the board into 3 columns
def columnmaker(grid):
    column1 = [grid[0], grid[3], grid[6]]
    column2 = [grid[1], grid[4], grid[7]]
    column3 = [grid[2], grid[5], grid[8]]
    return column1, column2, column3



# splits the board into 2 crosses
def crossmaker(grid):
    cross1 = [grid[0], grid[4], grid[8]]
    cross2 = [grid[2], grid[4], grid[6]]
    return cross1, cross2


    
#checks if there is a winner in the board
def winnercheck(grid):
    row1, row2, row3 = (rowmaker(grid))
    
    column1, column2, column3 = (columnmaker(grid))
    
    cross1, cross2 = (crossmaker(grid))
    
    totalLists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    
    for i in range(len(totalLists)):
        result = winninglist(totalLists[i])
        if (result == 1):
            return True
        else:
            continue
    return False



# checks if a list of 3 elements is a winning list
def winninglist(lst):
    for i in range(len(lst)):
        if (lst[i] == "_"):
            return False
        else:
            continue
    result = len(set(lst))
    return result




# checks if a list of 3 elements can win in one move
def winNextTurn(lst, player):
    result = len(set(lst))
    if (result == 2) and (lst.count("_") == 1):
        if (lst[0] == lst[1] == player) or (lst[1] == lst[2] == player) or (lst[0] == lst[2] == player):
            return True
        else:
            return False
    else:
        return False



# helper function for first step    
def winNextTurnLoop(grid, player):
    row1, row2, row3 = (rowmaker(grid))
    
    column1, column2, column3 = (columnmaker(grid))
    
    cross1, cross2 = (crossmaker(grid))
    
    totalLists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    
    for i in range(len(totalLists)):
        result = winNextTurn(totalLists[i], player)
        if (result):
            return True
        else:
            continue
    return False


# FIRST STEP
#checks if one move can win the game and produces the move
def winInOneRound(grid, player):
    winner = winNextTurnLoop(grid, player)
    if (winner):
        moves = emptySpots(grid)
        for i in range(len(moves)):
            newGrid = insertLetter(player, moves[i], grid)
            winnerExists = winnercheck(newGrid)
            newGrid = insertLetter("_", moves[i], grid)
            if (winnerExists):
                return moves[i] + 1
            else:
                continue
    else:
        return False




#Step 2
#checks if the human has a winning move
def oppWinOneRound(grid):
    if (not (winInOneRound(grid, human))):
        return False
    else:
        move = winInOneRound(grid, human)
        return move

#Step 3
# produces a move that produces a fork
def checkFork(grid):
    moves = emptySpots(grid)
    for i in range (len(moves)):
        newGrid = insertLetter(ai, moves[i], grid)
        counter = winningMoves(newGrid, ai)
        newGrid = insertLetter("_", moves[i], grid)
        if (counter >= 2):
            return moves[i] + 1
        else:
            continue
    return False

        
#Step 4 - blocks fork
# produces a move that produces the human's move that would make a fork
def oppFork(grid):
    moves = emptySpots(grid)
    for i in range (len(moves)):
        newGrid = insertLetter(human, moves[i], grid)
        counter = winningMoves(newGrid, human)
        newGrid = insertLetter("_", moves[i], grid)
        if (counter >= 2):
            return moves[i] + 1
        else:
            continue
    return False



#makes two in a row
def makeTwo(grid):
    moves = emptySpots(grid)
    for i in range(len(moves)):
        newGrid = insertLetter(ai, moves[i], grid)
        result = winNextTurnLoop(newGrid, ai)
        newGrid = insertLetter("_", moves[i], grid)
        if (result):
            return True, moves[i]
        else:
            continue
    return False, None


# STEP 4
# block all forks that also allow ai to create 2 in a row, or ai creates 2 in a row as long as it doesn't create a fork
def moveMakeTwo(grid):
    moves = emptySpots(grid)
    result, move = makeTwo(grid)
    blockFork = oppFork(grid)
    if (blockFork!= False):
        move = oppFork(grid)
        return move
    if (blockFork != False) and (result == True):
        if (blockFork == move):
            return move + 1
        else:
            return blockFork
    else:
        return False


# Step 4.1
# make two in a row if doesn't make a fork
def makeTwoInRow(grid):
    moves = emptySpots(grid)
    result, move = makeTwo(grid)
    if (grid.count("_") < 7):   
        if (result):
            return move + 1
        else:
            return False
    else:
        return False


    
#STEP 5
# checks if center is open
def moveCenter(grid):
    if (grid[4] == "_"):
        return 4
    else:
        return False



# Step 6
# if a corner is occupied, place in opposite corner
def oppositeCorner(grid):
    if (grid[0] == human) and (grid[8] == "_"):
        return 9
    elif (grid[2] == human) and (grid[6] == "_"):
        return 7
    elif (grid[6] == human) and (grid[2] == "_"):
        return 3
    elif (grid[8] == human) and (grid[0] == "_"):
        return 1
    else:
        return False


# Step 7
def emptyCorner(grid):
    listOfCorners = [0, 2, 6, 8]
    for i in range(len(listOfCorners)):
        if (grid[listOfCorners[i]] == "_"):
            return listOfCorners[i] + 1
        else:
            continue
    else:
        return False



#Step 8
#plays empty side

def emptySide(grid):
    listOfSides = [1, 3, 5, 7]
    for i in range(len(listOfSides)):
        if (grid[listOfSides[i]] == "_"):
            return listOfSides[i]
        else:
            continue




#algorithm employed to get ai's move
def getMove(grid):
    if (winInOneRound(grid, ai) != False):
        move = winInOneRound(grid, ai)
        return move - 1
    elif (oppWinOneRound(grid) != False):
        move = oppWinOneRound(grid)
        return move - 1
    elif (checkFork(grid) != False):
        move = checkFork(grid)
        return move - 1
    elif (moveMakeTwo(grid) != False):
        move = moveMakeTwo(grid)
        return move - 1
    elif (makeTwoInRow(grid) != False):
        move = makeTwoInRow(grid)
        return move - 1
    elif (moveCenter(grid) != False):
        move = moveCenter(grid)
        return move
    elif (oppositeCorner(grid) != False):
        move = oppositeCorner(grid)
        return move - 1
    elif (emptyCorner(grid) != False):
        move = emptyCorner(grid)
        return move - 1
    else:
        move = emptySide(grid)
        return move
    
    



def allowedMove(grid, move):
    try:
        insertLetter(human, move - 1, grid)
        return True
    except:
        print("That move is not a valid move!")
        return False
        



def main(grid):
    answer = input("Would you like to play tic tac toe? (Y/N)")
    if (answer == "Y"):
        
        print("")
        printBoard(grid)


        while (fullBoard(grid) == False):


            move = getMove(grid)
            newGrid = insertLetter(ai, move, grid)
            result = (winnercheck(grid))
    
        

            if (fullBoard(grid) == True):
                if (winnercheck(grid) == True):
                    printBoard(grid)
                    print("Winner!")
                    break
                else:
                    printBoard(grid)
                    print("Tie!")
                    break
                     
            if (result == False):
                print ("")
                printBoard(grid)
                print ("No winner yet!")
                print ("")
                print ("")
                move = int(input("What's your move? (1 - 9)"))
                grid = insertLetter(human, move - 1, grid)
                                    
            else:
                print("")
                printBoard(grid)
                print("Winner!")
                break

    else:
        print("Okay, goodbye!")


main(board)

# some test boards
##board2 = ["X", "_", "X", "X", "_", "O", "_", "O", "O"]
##board5 = ["O", "X", "O", "X", "B", "X", "O", "_", "O"]
##board1 = ["X", "_", "_", "_", "O", "_", "_", "_", "_"]
##board7 = ['X', 'X', 'O', '_', '_', '_', '_', '_', '_']
##board8 = ["_", "_", "_", "O", "X", "_", "_", "_", "_"]
##board9 = ["O", "X", "O", "_", "X", "_", "_", "O", "X"]


        
            


        
    

    
            
            
        







           





