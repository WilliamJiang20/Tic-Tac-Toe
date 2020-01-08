# Python Tic-Tac-Toe
# Started: 01/07/2020
# Last Worked On: 01/08/2020

board = ["_" for x in range(0, 10)]




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
    cross2 = [grid[2], grid[4], grid[7]]
    return cross1, cross2

    
        
def winnercheck(grid):
    row1, row2, row3 = (rowmaker(grid))
    column1, column2, column3 = (columnmaker(grid))
    cross1, cross2 = (crossmaker(grid))
    totallists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    for i in range(len(totallists)):
        result = winninglist(totallists[i])
        if (result == 1):
            return True
        else:
            continue
    return False



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


    
##def mainTicTacToe(grid):
##    
## #   if ((not (winnercheck(grid)) == True)):
##  #      while (not (fullBoard(grid))) and ((not (winnercheck(grid)) == True)):
##    while (winnercheck(grid) == False):
##        if (fullBoard(grid) == True):
##            print("")
##            print(grid)
##            print("")
##            print("Tie!")
##
##        else:
##            print ("")
##            print ("No winner yet!")
##            print ("")
##            print(grid)
##            print ("")
##            move = int(input("What's your move?"))
##            mainTicTacToe(insertLetter("X", move))
##
##        
##    
##    if  (winnercheck(grid) == True):
##        print ("")
##        print(grid)
##        print ("")
##        print("Winner!")




def main(grid):
    print("")


    while (fullBoard(grid) == False):

        if (winnercheck(grid) == False):
            print ("")
            print ("No winner yet!")
            print ("")
            print(grid)
            print ("")
            move = int(input("What's your move?"))
            grid = insertLetter("X", move, grid)

        else:
            print("")
            print(grid)
            print("")
            print ("Winner!")
            break

    if (fullBoard(grid) == True):
        print("Tie!")

    

            



#main(board)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, "_"]

main(lst2)





