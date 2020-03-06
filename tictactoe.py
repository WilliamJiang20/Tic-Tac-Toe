# Python Tic-Tac-Toe

import math
import time

# counts how many winning moves there are
def winning_moves(grid, player):
    row1, row2, row3 = row_maker(grid)

    column1, column2, column3 = column_maker(grid)

    cross1, cross2 = cross_maker(grid)

    total_lists = [row1, row2, row3, column1, column2, column3, cross1, cross2]
    counter = 0
    for i in range(len(total_lists)):
        result = win_next_turn(total_lists[i], player)
        if result:
            counter += 1
        else:
            continue
    return counter

# inserts letter into board
def insert_letter(letter, pos, grid):
    grid[pos] = letter
    return grid

# checks if board is full
def full_board(grid):
    return grid.count("_") == 0

# produces a list of empty spots in the board
def empty_spots(grid):
    lst_of_empty = []
    for i in range(len(grid)):
        if grid[i] == "_":
            lst_of_empty.append(i)
        else:
            continue
    return lst_of_empty

# produces clean version of board
def print_board(grid):
    print("-------------")
    print("| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print("-------------")
    print("| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print("-------------")
    print("| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print("-------------")

# splits the board into 3 rows
def row_maker(grid):
    row1 = [grid[0], grid[1], grid[2]]
    row2 = [grid[3], grid[4], grid[5]]
    row3 = [grid[6], grid[7], grid[8]]
    return row1, row2, row3

# splits the board into 3 columns
def column_maker(grid):
    column1 = [grid[0], grid[3], grid[6]]
    column2 = [grid[1], grid[4], grid[7]]
    column3 = [grid[2], grid[5], grid[8]]
    return column1, column2, column3

# splits the board into 2 crosses
def cross_maker(grid):
    cross1 = [grid[0], grid[4], grid[8]]
    cross2 = [grid[2], grid[4], grid[6]]
    return cross1, cross2

# checks if there is a winner in the board
def winner_check(grid):
    row1, row2, row3 = row_maker(grid)

    column1, column2, column3 = column_maker(grid)

    cross1, cross2 = cross_maker(grid)

    total_lists = [row1, row2, row3, column1, column2, column3, cross1, cross2]

    for i in range(len(total_lists)):
        result = winning_list(total_lists[i])
        if result == 1:
            return True
        else:
            continue
    return False

# checks if a list of 3 elements is a winning list
def winning_list(lst):
    for i in range(len(lst)):
        if lst[i] == "_":
            return False
        else:
            continue
    result = len(set(lst))
    return result

# checks if a list of 3 elements can win in one move
def win_next_turn(lst, player):
    result = len(set(lst))
    if (result == 2) and (lst.count("_") == 1):
        if (lst[0] == lst[1] == player) or (lst[1] == lst[2] == player) or (lst[0] == lst[2] == player):
            return True
        else:
            return False
    else:
        return False


# helper function for first step
def win_next_turn_loop(grid, player):
    row1, row2, row3 = row_maker(grid)

    column1, column2, column3 = column_maker(grid)

    cross1, cross2 = cross_maker(grid)

    total_lists = [row1, row2, row3, column1, column2, column3, cross1, cross2]

    for i in range(len(total_lists)):
        result = win_next_turn(total_lists[i], player)
        if result:
            return True
        else:
            continue
    return False


# Step 1
# checks if one move can win the game and produces the move
def win_in_one_round(grid, player):
    winner = win_next_turn_loop(grid, player)
    if winner:
        moves = empty_spots(grid)
        for i in range(len(moves)):
            new_grid = insert_letter(player, moves[i], grid)
            winner_exists = winner_check(new_grid)
            new_grid = insert_letter("_", moves[i], grid)
            if winner_exists:
                return moves[i] + 1
            else:
                continue
    else:
        return False

# Step 2
# checks if the human has a winning move
def opp_win_one_round(grid, player):
    if not (win_in_one_round(grid, player)):
        return False
    else:
        move = win_in_one_round(grid, player)
        return move

# Step 3
# produces a move that produces a fork
def check_fork(grid, ai):
    moves = empty_spots(grid)
    for i in range(len(moves)):
        new_grid = insert_letter(ai, moves[i], grid)
        counter = winning_moves(new_grid, ai)
        new_grid = insert_letter("_", moves[i], grid)
        if counter >= 2:
            return moves[i] + 1
        else:
            continue
    return False


# Step 4 - blocks fork
# produces a move that produces the human's move that would make a fork
def opp_fork(grid, player):
    moves = empty_spots(grid)
    for i in range(len(moves)):
        new_grid = insert_letter(player, moves[i], grid)
        counter = winning_moves(new_grid, player)
        new_grid = insert_letter("_", moves[i], grid)
        if counter >= 2:
            return moves[i] + 1
        else:
            continue
    return False

# makes two in a row
def make_two(grid, ai):
    moves = empty_spots(grid)
    for i in range(len(moves)):
        new_grid = insert_letter(ai, moves[i], grid)
        result = win_next_turn_loop(new_grid, ai)
        new_grid = insert_letter("_", moves[i], grid)
        if result:
            return True, moves[i]
        else:
            continue
    return False, None

# STEP 4
# block all forks that also allow ai to create 2 in a row, or ai creates 2 in a row as long as it doesn't create a fork
def move_make_two(grid, ai, player):
    result, move = make_two(grid, ai)
    block_fork = opp_fork(grid, player)
    if block_fork:
        move = opp_fork(grid, player)
        return move
    if block_fork and result:
        if block_fork == move:
            return move + 1
        else:
            return block_fork
    else:
        return False

# Step 4.1
# make two in a row if doesn't make a fork
def make_two_in_row(grid, ai):
    result, move = make_two(grid, ai)
    if grid.count("_") < 7:
        if result:
            return move + 1
        else:
            return False
    else:
        return False

# Step 5
# checks if center is open
def move_center(grid):
    if grid[4] == "_":
        return 4
    else:
        return False

# Step 6
# if a corner is occupied, place in opposite corner
def opposite_corner(grid, player):
    if (grid[0] == player) and (grid[8] == "_"):
        return 9
    elif (grid[2] == player) and (grid[6] == "_"):
        return 7
    elif (grid[6] == player) and (grid[2] == "_"):
        return 3
    elif (grid[8] == player) and (grid[0] == "_"):
        return 1
    else:
        return False

# Step 7
def empty_corner(grid):
    list_of_corners = [0, 2, 6, 8]
    for i in range(len(list_of_corners)):
        if grid[list_of_corners[i]] == "_":
            return list_of_corners[i] + 1
        else:
            continue
    else:
        return False

# Step 8
# plays empty side
def empty_side(grid):
    list_of_sides = [1, 3, 5, 7]
    for i in range(len(list_of_sides)):
        if grid[list_of_sides[i]] == "_":
            return list_of_sides[i]
        else:
            continue

# algorithm employed to get ai's move
def get_move(grid, ai):
    if ai == "O":
        opp = "X"
    if ai == "X":
        opp = "O"
    if win_in_one_round(grid, ai):
        move = win_in_one_round(grid, ai)
        return move - 1
    elif opp_win_one_round(grid, opp):
        move = opp_win_one_round(grid, opp)
        return move - 1
    elif check_fork(grid, ai):
        move = check_fork(grid, ai)
        return move - 1
    elif move_make_two(grid, ai, opp):
        move = move_make_two(grid, ai, opp)
        return move - 1
    elif make_two_in_row(grid, ai):
        move = make_two_in_row(grid, ai)
        return move - 1
    elif move_center(grid):
        move = move_center(grid)
        return move
    elif opposite_corner(grid, opp):
        move = opposite_corner(grid, opp)
        return move - 1
    elif empty_corner(grid):
        move = empty_corner(grid)
        return move - 1
    else:
        move = empty_side(grid)
        return move

def main():
    board = ["_" for x in range(0, 9)]
    answer = input("Would you like to play? \"Y/N\"")
    if answer == "Y":
        answer = input("Would you like to play a two player game (1) or face the computer (2)? \"1/2\"")
        if answer == "1":
            player1 = "X"
            player2 = "O"
            turn = player1
            while True:
                if full_board(board) or winner_check(board):
                    break

                elif turn == player1:
                    print_board(board)
                    try:
                        move = int(input("What's your move? (1 - 9)"))
                        if board[move - 1] == "_":
                            board = insert_letter(player1, move - 1, board)
                            turn = player2
                        else:
                            print("Invalid move! Position is occupied!")
                    except:
                        print("You must input an integer between 1 and 9!")

                elif turn == player2:
                    print_board(board)
                    try:
                        move = int(input("What's your move? (1 - 9)"))
                        if board[move - 1] == "_":
                            board = insert_letter(player2, move - 1, board)
                            turn = player1
                        else:
                            print("Invalid move! Position is occupied!")
                    except:
                        print("You must input an integer between 1 and 9!")

            if winner_check(board):
                if turn == player2:
                    print_board(board)
                    print("Player 1 has won!")
                    print_board(board)
                elif turn == player1:
                    print_board(board)
                    print("Player 2 has won!")
            elif full_board(board):
                print_board(board)
                print("Tie!")

        elif answer == "2":
            answer = input("Would you like to be player one or player two? \"1/2\"")

            if answer == "1":
                human = "X"
                ai = "O"
                turn = human
                while True:
                    if full_board(board) or winner_check(board):
                        break

                    elif turn == human:
                        print_board(board)
                        try:
                            move = int(input("What's your move? (1 - 9)"))
                            if board[move - 1] == "_":
                                board = insert_letter(human, move - 1, board)
                                turn = ai
                            else:
                                print("Invalid move! Position is occupied!")
                        except:
                            print("You must input an integer between 1 and 9!")

                    elif turn == ai:
                        move = get_move(board, ai)
                        board = insert_letter(ai, move, board)
                        turn = human

                if winner_check(board):
                    if turn == ai:
                        print_board(board)
                        print("You have won!")
                        print_board(board)
                    elif turn == human:
                        print_board(board)
                        print("CPU has won!")
                elif full_board(board):
                    print_board(board)
                    print("Tie!")

            elif answer == "2":
                human = "O"
                ai = "X"
                turn = ai
                while True:
                    if full_board(board) or winner_check(board):
                        break

                    elif turn == ai:
                        move = get_move(board, ai)
                        board = insert_letter(ai, move, board)
                        turn = human

                    elif turn == human:
                        print_board(board)

                        try:
                            move = int(input("What's your move? (1 - 9)"))
                            if board[move - 1] == "_":
                                board = insert_letter(human, move - 1, board)
                                turn = ai

                            else:
                                print("Invalid move! Position is occupied!")
                        except:
                            print("You must input an integer between 1 and 9!")

                if winner_check(board):
                    if turn == ai:
                        print_board(board)
                        print("You have won!")
                    elif turn == human:
                        print_board(board)
                        print("CPU has won!")
                elif full_board(board):
                    print("Tie!")
    print("Goodbye!")
    time.sleep(3)


main()
