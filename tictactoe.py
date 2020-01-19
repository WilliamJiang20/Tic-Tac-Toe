# Python Tic-Tac-Toe
# Started: 01/07/2020
# Last Worked On: 01/08/2020



import math
import time


board = ["_" for x in range(0, 9)]

human = "O"
ai = "X"



# checks if a list of 3 elements is a winning list
def winninglist(lst):
    for i in range(len(lst)):
        if (lst[i] == "_"):
            return False
        else:
            continue
    result = len(set(lst))
    return result

          
# makes the board into 3 rows
def rowmaker(grid):
    row1 = [grid[0], grid[1], grid[2]]
    row2 = [grid[3], grid[4], grid[5]]
    row3 = [grid[6], grid[7], grid[8]]
    return row1, row2, row3

# makes the board into 3 columns
def columnmaker(grid):
    column1 = [grid[0], grid[3], grid[6]]
    column2 = [grid[1], grid[4], grid[7]]
    column3 = [grid[2], grid[5], grid[8]]
    return column1, column2, column3

# makes the board into 2 crosses
def crossmaker(grid):
    cross1 = [grid[0], grid[4], grid[8]]
    cross2 = [grid[2], grid[4], grid[6]]
    return cross1, cross2

    
        
def winnercheck(grid):
    row1, row2, row3 = (rowmaker(grid))
    
    column1, column2, column3 = (columnmaker(grid))
    
    cross1, cross2 = (crossmaker(grid))
    
    totalLists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    
    for i in range(len(totalLists)):
        result = winninglist(totalLists[i])
        whoWon = totalLists[i][0]
        if (result == 1):
            return True, whoWon
        else:
            continue
    return False, 0



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

def endState(grid):
    boolResult, winningList = (winnercheck(grid))
    if (boolResult == True):
        return True

    elif (fullBoard(grid) == True):
        return True
    
    else:
        return False


    
# produces a list of empty spots in the board
def emptySpots(grid):
    lstOfEmpty = []
    for i in range(len(grid)):
        if (grid[i] == "_"):
            lstOfEmpty.append(i)
        else:
            continue
    return lstOfEmpty

# checks who wins
def whoWon(grid):
    boolResult, winningList = (winnercheck(grid))
    if (boolResult == True):
        if (winningList == "X"):
            return 10
        if (winningList == "O"):
            return -10

    if (boolResult == False) and (fullBoard(grid) == True):
        return 0




# produces clean version of board
def printBoard(grid):
    print ("-------------")
    print ("| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print ("-------------")
    print ("| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print ("-------------")
    print ("| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print ("-------------")
        

##def getAiMove(oldGrid):
##    val, move = minimax(oldGrid, True)
##    return move
##
##
##def minimax(grid, aiTurn):
##    moves = emptySpots(grid)
##
##    if (aiTurn == False):
##        nextTurn = True
##    else:
##        nextTurn = False
##
##    if (endState(grid) == True):
##        value = whoWon(grid)
##        return value, value
##
##    if (fullBoard(grid) == True):
##        return 0, -1
##
##    
##
##    result = []
##        
##    for i in range (len(moves)):
##        grid = insertLetter(ai, moves[i], grid)
##        value = minimax(grid, True)
##        result.append(value)
##        grid = insertLetter("_", moves[i], grid)
##
##
##
##    if (not(aiTurn):
##        value = max(result)
##        return value, moves[result.index(value)]
##
##    else:
##        value = min(result)
##        return value, moves[result.index(value)]

    



    


##def getAiTurn(grid):
##    maxScore = -math.inf
##    moves = emptySpots(grid)
##    for i in range (len(moves)):
##        grid = insertLetter(ai, moves[i], grid)
##        newScore = minimax(grid, 0, False)
##        grid = insertLetter("_", moves[i], grid) 
##        if (newScore > maxScore):
##            maxScore = newScore
##            bestMove = i
##            return bestMove




def test(grid):
    moves = emptySpots(grid)
    for i in range (len(moves)):
        newGrid = insertLetter(ai, moves[i], grid)
        printBoard(newGrid)
        newGrid = insertLetter("_", moves[i], grid)

##
##def minimax(grid, depth, aiTurn):
##
##    if (endState(grid) == True):
##        value = whoWon(grid)
##        return value
##
##    if (aiTurn == True):
##        maxScore = -math.inf
##        moves = emptySpots(grid)
##        for i in range(len(moves)):
##            grid = insertLetter(ai, moves[i], grid)
##            newScore = minimax(grid, depth + 1, False)
##            grid = insertLetter("_", moves[i], grid)
##            maxScore = max(newScore, maxScore)
##
##        return maxScore
##
##    else:
##        minScore = math.inf
##        moves = emptySpots(grid)
##        for i in range(len(moves)):
##            grid = insertLetter(human, moves[i], grid)
##            newScore = minimax(grid, depth + 1, True)
##            grid = insertLetter("_", moves[i], grid)
##            minScore = min(newScore, minScore)
##
##        return minScore




def minimax(grid, aiTurn):
    if (endState(grid) == True):
        value = whoWon(grid)
        return value

    if (aiTurn):
        nextTurn = False

    else:
        nextTurn = True
        
    scores = []

    moves = emptySpots(grid)
    for i in range(len(moves)):
        grid = insertLetter(ai, moves[i], grid)
        score = minimax(grid, nextTurn)
        grid = insertLetter("_", moves[i], grid)
        scores.append(score)
    
    if (aiTurn):
        maxScore = max(scores)
        scoresIndex = moves[scores.index(maxScore)]
        return scoresIndex

    else:
        minScore = min(scores)
        scoresIndex = moves[scores.index(minScore)]
        return scoresIndex


def getMove(grid):
    bestScore = -math.inf
    moves = emptySpots(grid)
    for i in range(len(moves)):
            grid = insertLetter(ai, moves[i], grid)
            score = minimax2(grid, False)
            grid = insertLetter("_", moves[i], grid)
            if (score > bestScore):
                bestScore = score
                move = i
    grid = insertLetter(ai, move, grid)

def minimax2(grid, maximizingPlayer):
    if (endState(grid) == True):
        value = whoWon(grid)
        return value


    counter = 0
    
    if (maximizingPlayer):
        bestScore = -math.inf
        moves = emptySpots(grid)
        for i in range(len(moves)):
            grid = insertLetter(ai, moves[i], grid)
            counter = counter + 1
            score = minimax2(grid, False)
            grid = insertLetter("_", moves[i], grid)
            bestScore = max(bestScore, score)
        return bestScore

    else:
        bestScore = math.inf
        moves = emptySpots(grid)
        for i in range(len(moves)):
            grid = insertLetter(ai, moves[i], grid)
            counter = counter + 1
            score = minimax2(grid, True)
            grid = insertLetter("_", moves[i], grid)
            bestScore = min(bestScore, score)
        return bestScore
        
            


        
    

    
            
            
        


def main(grid):
    print("")
    printBoard(grid)


    while (fullBoard(grid) == False):


        move = minimax2(grid, True)
        grid = insertLetter(ai, move, grid)
        print(grid)
        boolResult, winningList = (winnercheck(grid))
        


        if (fullBoard(grid) == True):
            printBoard(grid)
            print("Tie!")
            break
                     
        if (boolResult == False):
            print ("")
            printBoard(grid)
            print ("No winner yet!")
            print ("")
            print ("")
            move = int(input("What's your move?"))
            grid = insertLetter(human, move - 1, grid)

                
        else:
            print("")
            printBoard(grid)
            print("Winner!")
            break

    

        

    
    
        
#main(board)

board2 = ["X", "_", "X", "X", "_", "O", "_", "O", "O"]
board5 = ["O", "X", "O", "X", "B", "X", "O", "O", "O"]
board1 = ["X", "_", "_", "_", "O", "_", "_", "_", "_"]
board7 = ['X', 'X', 'X', '_', '_', '_', '_', '_', '_']
board8 = ["X", "_", "_", "_", "X", "_", "O", "_", "O"]




           





