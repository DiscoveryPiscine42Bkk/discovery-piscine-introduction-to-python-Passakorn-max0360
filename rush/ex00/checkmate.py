#!/usr/bin/env python3

#Step 1: Determine the baord parameters
def checkmate(board_received): 
    board_rows = board_received.strip().split('\n') # From the input string, split it into rows based on "\n" characters.(When see it, split a new line)
    n = len(board_rows)                             # now count number of rows in the board
    board = [list(row) for row in board_rows]       # Convert each row into a list of characters for easier manipulation

#Step 2: Find the position of the king
    for i in range(n):
        for j in range(n):          # Two loops for checking each cell in the board (i=row, j=column)
            if board[i][j] == 'K':
                ki, kj = i, j       #If King is found, store its position in ki and kj
                break
        else:
            continue                # If King not found in this row, continue to next row
        break                       # If King found, break the outer loop

#Step 3: Check for attackers
    for i in range(n):
        for j in range(n):          # Again, two loops to check each cell in the board
            piece = board[i][j]     # Get the piece at the current position
            if piece == '.':
                continue            # If the cell is empty, skip to the next cell
            if piece == 'P' and pawn_attacks(i, j, ki, kj):
                print("Success")
                return              #If a pawn is found & check with its function & can kill , print "Success" and exit the function
            if piece == 'B' and bishop_attacks(i, j, ki, kj, board):
                print("Success")
                return              # If a bishop is found & check with its function & can kill , print "Success" and exit the function
            if piece == 'R' and rook_attacks(i, j, ki, kj, board):
                print("Success")
                return              # If a rook is found & check with its function & can kill , print "Success" and exit the function 
            if piece == 'Q' and queen_attacks(i, j, ki, kj, board):
                print("Success")
                return              # If a queen is found & check with its function & can kill , print "Success" and exit the function    

    print("Fail")                   # If no attackers can kill, print "Fail" and exit the function

# Step 4: Define the attack functions for each piece (i=row, j=column, ki=king_row, kj=king_column)
def pawn_attacks(i, j, ki, kj):                                             #Pawn attack logic
    return (i + 1 == ki and j - 1 == kj) or (i + 1 == ki and j + 1 == kj)   # Pawn = i+1 (moves one step up), j-1 (left) or j+1 (right) to attack the king

def bishop_attacks(i, j, ki, kj, board): # Bishop attack logic
    if abs(i - ki) != abs(j - kj):       # Bishop attack is diagonal, so absolute Row distance MUST equal absolute Column distance
        return False                     # If not, return False means bishop cannot attack the king

    row_dir = 1 if ki > i else -1        # Determine the direction of row movement (+1 if king is above Bishop, -1 if below)
    col_dir = 1 if kj > j else -1        # Determine the direction of column movement (+1 if king is right of Bishop, -1 if left)

    curr_i, curr_j = i + row_dir, j + col_dir # Now check Obstacles in the path of the bishop. Start with first square after the bishop
    while curr_i != ki and curr_j != kj:      # Continue this loop until we reach the king's position
        if board[curr_i][curr_j] != '.':      # If there is any piece in the path of the bishop, it cannot attack the king
            return False
        curr_i += row_dir                     # Continue moving in the determined direction
        curr_j += col_dir
    
    return True                               # If we reach King, it means the bishop can attack it, so return True

def rook_attacks(i, j, ki, kj, board):      # Rook attack logic
    if i != ki and j != kj:                 # Rook can only attack if it is in the same row or column as the king
        return False
    
    if i == ki:                                         #Case when rook and king are in the same row
        for col in range(min(j, kj) + 1, max(j, kj)):   # Continue until we reach the king's column
            if board[i][col] != '.':                    # Check if there is any piece in the path of the rook
                return False                            # If there is, return False

    if j == kj:                                         # Case when rook and king are in the same column    
        for row in range(min(i, ki) + 1, max(i, ki)):   # Continue until we reach the king's row
            if board[row][j] != '.':                    # Check if there is any piece in the path of the rook           
                return False                            # If there is, return False

    return True                                         # If we reach King, it means the rook can attack it, so return True

def queen_attacks(i, j, ki, kj, board):                 # Queen is the combination of rook and bishop
    return rook_attacks(i, j, ki, kj, board) or bishop_attacks(i, j, ki, kj, board)

