# imports
# Your imports go here
import sys
import stdio
import stddraw

# global variables
# Your global variables go here
row_max = 10
col_max = 10
pieces = ["s", "l", "d", "x"]
piece_sizes = ["1", "2", "a", "b", "c", "d"]
directions = ["u", "d", "l", "r", "b"]

def cmd_line_parameters(stop=True):
    global row_max, col_max, gui_mode 
    try:
        row_max = int(sys.argv[1])
        col_max = int(sys.argv[2])
        gui_mode = int(sys.argv[3])
    except IndexError:
        print_errors("ERROR: Illegal argument", stop)
        return False
    if len(sys.argv) > 4:
        print_errors("ERROR: Too many arguments", stop)
        return False
    elif len(sys.argv) < 4:
        print_errors("ERROR: Too few arguments", stop)
        return False
    elif sys.argv[3] not in ("0", "1"):
        print_errors("ERROR: Illegal argument", stop)
        return False
    elif row_max < 8 or col_max < 8:
        print_errors("ERROR: Illegal argument", stop)
        return False
    elif row_max > 10 or col_max > 10:
        print_errors("ERROR: Illegal argument", stop)
        return False

def check_sink_range(row_max, col_max, r, c, stop=True):
    """
    Function to check whether a sink is in the correct position.

    Args:
        row_max (int): The number of rows in the board
        col_max (int): The number of columns in the board
        row (int): The row of the sink
        col (int): The column of the sink

    Returns:
        bool: True if the sink is in the correct range, False otherwise.
    """
    if ((c > 2) and (c < col_max - 3) and (r > 2) and (r < row_max - 3)):
        print_errors("ERROR: Sink in the wrong position", stop)
        return False
    elif (r > 9) or (c > 9) or (r < 0) or (c < 0):
        print_errors("ERROR: Field " + str(r) + " " + str(c) + " not on board", stop)
        return False
    elif (r == row_max) or (c == col_max):
        print_errors("ERROR: Field " + str(r) + " " + str(c) + " not on board", stop)
        return False
    elif (r not in range(0, row_max) or c not in range(0, col_max)):
         print_errors("ERROR: Sink in the wrong position", stop)
         return False
    else:
        return True


def check_piece_range(row_max, col_max, r, c, stop=True):
    """
    Function to check whether a piece is in the correct position.

    Args:
        row_max (int): The number of rows in the board
        col_max (int): The number of columns in the board
        row (int): The row of the piece
        col (int): The column of the piece

    Returns:
        bool: True if the piece is in the correct range, False otherwise.
    """
    if r not in range(row_max) or c not in range(col_max):
        print_errors("ERROR: Field " + str(r) + " " + str(c) + " not on board", stop)
        return False
    elif not ((c > 2) and (c < col_max - 3) and (r > 2) and (r < row_max - 3)):
        print_errors("ERROR: Piece in the wrong position", stop)
        return False
    else:
        return True


def check_piece_upright(r, c, board):
    """
    Function to check whether a piece is upright, or whether it is lying on it's
    side.

    Args:
        row (int): The row of the piece
        col (int): The column of the piece
        board (2D array of str): The game board

    Returns:
        bool: True if the piece is upright, False otherwise.
    """
    piece_list = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
    int_value = (len(board) * r) + c
    row_max = len(board) - 1
            
    if (r >= 0 and r < row_max):
        if board[r][c] in piece_list:
            if not (board[r][c + 1] == str(int_value) or 
            board[r + 1][c] == str(int_value) or board[r][c - 1] == str(int_value) or
            board[r - 1][c] == str(int_value)):
                return True
            else:
                return False
                
    elif r == 9:
        if board[r][c] in piece_list:
            return True
    pass


def get_piece_fields(r, c, board):
    """
    Get all the coordinates belonging to the piece at coordinate (row, col).

    Args:
        row (int): The row of the piece
        col (int): The column of the piece
        board (2D array of str): The game board

    Returns:
        array of coordinates: The fields that the piece occupies
    """
    # This is a helper function that you may find useful. If you do, you may
    # implement it and use it. You are also welcome to leave this blank or
    # remove it if you do not use it.
    pass

'''def check_overlapping_pieces(r, c, twoD_array, piece_type):
    #row_max, col_max = len(), len(board[0])
    # Check if out of bounds
    if r < 0 or r >= row_max or c < 0 or c >= col_max:
        return twoD_array[r][c] != "  "
    else:
        return twoD_array[r][c] == piece_type'''
def check_old_moves(piece, r, c, old_2darray, stop=True):
    if old_2darray == None:
        return False
    else: 
        if piece == old_2darray[r][c]:
            print_errors("ERROR: Piece cannot be returned to starting position")
            return False
        else: 
            return False

def print_errors(message, stop=False):
    if stop:
        stdio.writeln(f"{message}")
        sys.exit()
    else:
        return False


def validate_move(r, c, direction, player, twoD_array, old_2darray, stop=True):
    try:
        rs = len(twoD_array)
        cs = len(twoD_array[0])
        # Extract piece number values
        index = str(r * cs + c)

        if twoD_array[r][c].islower() and player == 1:
            print_errors("ERROR: Piece does not belong to the correct player", stop)
            return True
        elif twoD_array[r][c].isupper() and player == 0:
            stdio.writeln("ERROR: Piece does not belong to the correct player")
            sys.exit()
        elif twoD_array[r][c] == "  ":
            print_errors("ERROR: No piece on field " + str(r) + " " + str(c), stop)
            return False
        elif direction not in directions:
            stdio.writeln("ERROR: Invalid direction " + direction)
            sys.exit()

        elif twoD_array[r][c] in ("a", "A"):
            if direction == "r":
                if c < cs - 1:
                    
                    if (twoD_array[r][c + 1] == "  " or twoD_array[r][c + 1] == "s" or twoD_array[r][c + 1] != "x"):
                        if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                            return True
                        else:
                            return False
                else:
                    print_errors("ERROR: Cannot move beyond the board", stop)
                    return False
            elif direction == "l":
                if c > 0:
                    if (twoD_array[r][c - 1] == "  " or twoD_array[r][c - 1] == "s" or twoD_array[r][c - 1] != "x"):
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop): #DO THIS FOR THE REST
                            return True
                        else:
                            return False
                else:
                    print_errors("ERROR: Cannot move beyond the board", stop)
                    return False
            elif direction == "u":
                if (twoD_array[r + 1][c] == "  " or twoD_array[r + 1][c] == "s" or twoD_array[r + 1][c] != "x"):
                    if not check_old_moves(twoD_array[r][c], r + 1, c, old_2darray, stop):
                        return True
                    else:
                        return False
            elif direction == "d":
                if (twoD_array[r - 1][c] == "  " or twoD_array[r - 1][c] == "s" or twoD_array[r - 1][c] != "x"):
                    if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                        return True
                    else:
                        return False
            
    # Rules for Upright Type B (1x1)
        elif twoD_array[r][c] in ("b", "B") and check_piece_upright(r, c, twoD_array):
            # B piece moving UP
            # If it is purely empty?
            if direction == "u":
                
                if r < rs - 2 and (twoD_array[r + 1][c] == "  " and twoD_array[r + 2][c] == "  " or (twoD_array[r + 1][c] != "x" and twoD_array[r + 2][c] != "x")):
                    if not check_old_moves(twoD_array[r][c], r + 2, c, old_2darray, stop):
                        return True
                    else: 
                        return False
                # If it is purely a sink?
                elif r < rs - 2 and (twoD_array[r + 1][c] == "s" and twoD_array[r + 2][c] == "s"):
                    if not check_old_moves(twoD_array[r][c], r + 2, c, old_2darray, stop):
                        return True
                    else:
                        return False
                
            elif direction == "d":
                if r - 2 >= 0 and (twoD_array[r - 1][c] == "  " and twoD_array[r - 2][c] == "  " or (twoD_array[r - 1][c] != "x" and twoD_array[r - 2][c] != "x")):
                    if not check_old_moves(twoD_array[r][c], r - 2, c, old_2darray, stop):
                        return True
                    else: 
                        return False
                # If it is purely a sink?
                elif r - 2 >= 0 and (twoD_array[r - 1][c] == "s" and twoD_array[r - 2][c] == "s"):
                    if not check_old_moves(twoD_array[r][c], r - 2, c, old_2darray, stop):
                        return True
                    else:
                        return False
                    
            elif direction == "r":
                if c < cs - 2 and (twoD_array[r][c + 1] == "  " and twoD_array[r][c + 2] == "  " or (twoD_array[r][c + 1] != "x" and twoD_array[r][c + 2] != "x")):
                    if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                        return True
                    else: 
                        return False
                # If it is purely a sink?
                elif c < cs - 2 and (twoD_array[r][c + 1] == "s" and twoD_array[r][c + 2] == "s"):
                    if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                        return True
                    else:
                        return False
                # if + less than max and if - >= 0   
            elif direction == "l":
                if r < cs - 2 and (twoD_array[r][c - 1] in "  *" and twoD_array[r][c - 2] in "  *" or (twoD_array[r][c - 1] != "x" and twoD_array[r][c - 2] != "x")):
                    if not check_old_moves(twoD_array[r][c], r, c - 2, old_2darray, stop):
                        return True
                    else: 
                        return False
                # If it is purely a sink?
                elif r < rs - 2 and (twoD_array[r][c - 1] == "s" and twoD_array[r][c - 2] == "s"):
                    if not check_old_moves(twoD_array[r][c], r, c - 2, old_2darray, stop):
                        return True
                    else:
                        return False
                    
        elif twoD_array[r][c] in ("b", "B") and not check_piece_upright(r, c, twoD_array):
            
            # Laying Type B in Vertical Orientation (2x1)
            if r < rs - 2 and twoD_array[r + 1][c] == index:
                if direction == "u":
                    # If it is purely empty?
                    if twoD_array[r + 2][c] == "  " or twoD_array[r + 2][c] != "x":
                        if not check_old_moves(twoD_array[r][c], r + 2, c, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r + 2][c] == "s":
                        if not check_old_moves(twoD_array[r][c], r + 2, c, old_2darray, stop):
                            return True
                        else:
                            return False

                elif direction == "d":
                    if twoD_array[r - 1][c] == "  " or twoD_array[r - 1][c] != "x":
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r - 1][c] == "s":
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "r":
                    if twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  " or (twoD_array[r][c + 1] != "x" or twoD_array[r + 1][c + 1] != "x"):   
                        if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r][c + 1] == "s" and twoD_array[r + 1][c + 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  " and twoD_array[r + 1][c - 1] == "  " or (twoD_array[r][c - 1] != "x" or twoD_array[r + 1][c - 1] != "x"):
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r][c + 1] == "s" and twoD_array[r - 1][c + 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop):
                            return True
                        else:
                            return False

            # Laying Type B in Horizontal Orientation (1x2)
            elif r < rs - 1 and twoD_array[r][c + 1] == index:
                if direction == "u":
                    if twoD_array[r + 1][c] == "  " and twoD_array[r + 1][c + 1] == "  " or (twoD_array[r + 1][c] != "x" or twoD_array[r + 1][c + 1] != "x"):
                        if not check_old_moves(twoD_array[r][c], r + 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r + 1][c] == "s" and twoD_array[r + 1][c + 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r + 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "d":
                    if twoD_array[r - 1][c] == "  " and twoD_array[r - 1][c + 1] == "  " or (twoD_array[r - 1][c] != "x" or twoD_array[r - 1][c + 1] != "x"):
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                        
                            return True
                        else:
                            return False
                    elif twoD_array[r - 1][c] == "s" and twoD_array[r - 1][c + 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                
                elif direction == "r":
                    if twoD_array[r][c + 2] == "  " or twoD_array[r][c + 2] != "x":
                        if not check_old_moves(twoD_array[r][c], r, c + 2, old_2darray, stop): 
                            return True
                        else:
                            return False
                    elif twoD_array[r][c + 2] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c + 2, old_2darray, stop): 
                            return True
                        else:
                            return False
                        
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  " or twoD_array[r][c - 1] != "x":
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop): 
                            return True
                        else:
                            return False
                    elif twoD_array[r][c - 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop):
                            return True
                        else:
                            return False


    # Rules for Upright Type C (1x1)
        elif twoD_array[r][c] in ("c", "C") and check_piece_upright(r, c, twoD_array):
            # If it is purely empty?
            if direction == "u":
                if r + 3 < rs and ((twoD_array[r + 1][c] == "  " and twoD_array[r + 2][c] == "  " and twoD_array[r + 3][c] == "  ")
                                or (twoD_array[r + 1][c] != "x" or twoD_array[r + 2][c] != "x" or twoD_array[r + 3][c] != "x")
                                or (twoD_array[r + 1][c] == "*" or twoD_array[r + 2][c] == "*" or twoD_array[r + 3][c] == "*")):
                    if not check_old_moves(twoD_array[r][c], r + 1, c, old_2darray, stop):
                        return True
                    else:
                        return False
            elif direction == "d":
                if r - 3 >= 0 and (twoD_array[r - 1][c] == "  " and twoD_array[r - 2][c] == "  " and twoD_array[r - 3][c] == "  "
                                or (twoD_array[r - 1][c] != "x" or twoD_array[r - 2][c] != "x" or twoD_array[r - 3][c] != "x")):
                    if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                        return True
                    else:
                        return False
            elif direction == "l":
                if c - 3 >= 0 and (twoD_array[r][c - 1] in "  *" and twoD_array[r][c - 2] in "  *" and twoD_array[r][c - 3] in "  *"):
                                #or (twoD_array[r][c - 1] != "x" or twoD_array[r][c - 2] != "x" or twoD_array[r][c - 3] != "x")):
                    if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop):
                        return True
                    else:
                        return False
            elif direction == "r":
                if c < cs - 3 and (twoD_array[r][c + 1] == "  " and twoD_array[r][c + 2] == "  " and twoD_array[r][c + 3] == "  "
                                or (twoD_array[r][c + 1] != "x" or twoD_array[r][c + 2] != "x" and twoD_array[r][c + 3] != "x")):
                    if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                        return True
                    else:
                        return False
        
        elif twoD_array[r][c] in ("c", "C") and not check_piece_upright(r, c, twoD_array):
            if r + 2 < rs and twoD_array[r + 1][c] and twoD_array[r + 2][c] == index:
                if direction == "u":
                    # If it is purely empty?
                    if r + 3 >= rs:
                        return False
                    if twoD_array[r + 3][c] == "  " or twoD_array[r + 3][c] != "x":
                        if not check_old_moves(twoD_array[r][c], r + 3, c, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r + 3][c] == "s":
                        if not check_old_moves(twoD_array[r][c], r + 3, c, old_2darray, stop):
                            return True
                        else:
                            return False

                elif direction == "d":
                    if r - 1 < 0:
                        return False    
                    if twoD_array[r - 1][c] == "  " or twoD_array[r - 1][c] != "x":
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                    elif twoD_array[r - 1][c] == "s":
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "r":
                    if (twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  " and twoD_array[r + 2][c + 1] == "  "
                        or (twoD_array[r][c + 1] != "x" or twoD_array[r + 1][c + 1] != "x" or twoD_array[r + 2][c + 1] != "x")):
                        if not check_old_moves(twoD_array[r][c], r, c + 1, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "l":
                    if (twoD_array[r][c - 1] == "  " and twoD_array[r + 1][c - 1] == "  " and twoD_array[r + 2][c - 1] == "  "
                        or (twoD_array[r][c - 1] != "x" or twoD_array[r + 1][c - 1] != "x" or twoD_array[r + 2][c - 1] != "x")):
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop):
                            return True
                        else:
                            return False

            # Laying Type C in Horizontal Orientation (1x2)
            elif r < rs - 3 and twoD_array[r][c + 1] == index and twoD_array[r][c + 2] == index:
                if direction == "u":
                    if (twoD_array[r + 1][c] == "  " and twoD_array[r + 1][c + 1] == "  " and twoD_array[r + 1][c + 2] == "  "
                        or (twoD_array[r + 1][c] != "x" or twoD_array[r + 1][c + 1] != "x" or twoD_array[r + 1][c + 2] != "x")):
                        if not check_old_moves(twoD_array[r][c], r + 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                        
                elif direction == "d":
                    if (twoD_array[r - 1][c] == "  " and twoD_array[r - 1][c + 1] == "  " and twoD_array[r - 1][c + 2] == "  "
                        or (twoD_array[r - 1][c] != "x" or twoD_array[r - 1][c + 1] != "x" or twoD_array[r - 1][c + 2] != "x")):
                        if not check_old_moves(twoD_array[r][c], r - 1, c, old_2darray, stop):
                            return True
                        else:
                            return False
                
                elif direction == "r":
                    if twoD_array[r][c + 3] == "  " or twoD_array[r][c + 3] != "x":
                        if not check_old_moves(twoD_array[r][c], r, c + 3, old_2darray, stop): 
                            return True
                        else:
                            return False
                    elif twoD_array[r][c + 3] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c + 3, old_2darray,stop): 
                            return True
                        else:
                            return False
                        
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  " or twoD_array[r][c - 1] != "x":
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop): 
                            return True
                        else:
                            return False
                    elif twoD_array[r][c - 1] == "s":
                        if not check_old_moves(twoD_array[r][c], r, c - 1, old_2darray, stop): 
                            return True
                        else:
                            return False
                        
        elif twoD_array[r][c] in ("D", "d"):
            if direction == "r":
                if (twoD_array[r][c + 2] == "  " and twoD_array[r][c + 3] == "  " and twoD_array[r+1][c+2] == "  " and twoD_array[r+1][c+2] == "  " ) or \
                    (twoD_array[r][c + 3] == "s" and twoD_array[r][c + 3] == "s" and twoD_array[r+1][c+2] == "s" and twoD_array[r+1][c+2] == "s"):
                    if not check_old_moves(twoD_array[r][c], r, c + 2, old_2darray,stop):
                        return True
                    else:
                        return False
            elif direction == "l":
                if (twoD_array[r][c - 1] == "  " and twoD_array[r][c - 2] == "  " and twoD_array[r+1][c-1] == "  " and twoD_array[r+1][c-2] == "  " ) or \
                    (twoD_array[r][c - 1] == "s" and twoD_array[r][c - 2] == "s" and twoD_array[r+1][c-1] == "s" and twoD_array[r+1][c-2] == "s"):
                    if not check_old_moves(twoD_array[r][c], r, c - 2, old_2darray,stop):
                        return True
                    else:
                        return False
            elif direction == "u":
                if (twoD_array[r + 2][c] == "  " and twoD_array[r + 3][c] == "  " and twoD_array[r+2][c+1] == "  " and twoD_array[r+3][c+1] == "  " ) or \
                    (twoD_array[r + 2][c] == "s" and twoD_array[r + 3][c] == "s" and twoD_array[r+2][c+1] == "s" and twoD_array[r+3][c+1] == "s"):
                    if not check_old_moves(twoD_array[r][c], r + 2, c, old_2darray,stop):
                        return True
                    else:
                        return False
            elif direction == "d":
                if (twoD_array[r - 1][c] == "  " and twoD_array[r - 2][c] == "  " and twoD_array[r-1][c+1] == "  " and twoD_array[r+2][c+1] == "  " ) or \
                    (twoD_array[r - 2][c] == "s" and twoD_array[r - 2][c] == "s" and twoD_array[r-1][c+1] == "s" and twoD_array[r+2][c+1] == "s"):
                    if not check_old_moves(twoD_array[r][c], r - 2, c, old_2darray,stop):
                        return True
                    else:
                        return False
    except:
        IndexError

def do_move(r, c, direction, twoD_array, scores, gui_mode, player):
    """
    Executes the given move on the board.
    """
    # This function may be useful for separating out the logic of doing a move.
    '''if direction not in directions:
        stdio.writeln("ERROR: Invalid direction " + direction)
        sys.exit()'''

    rs = len(twoD_array)
    cs = len(twoD_array[0])

    try:
        piece = twoD_array[r][c]
        if twoD_array[r][c].lower() == "a":
            if direction == "l":
                if twoD_array[r][c - 1] == "  ":
                    twoD_array[r][c - 1] = twoD_array[r][c]
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c - 1] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 1
                elif twoD_array[r][c - 1] == "*":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c - 1] = "  "
            elif direction == "r":
                if twoD_array[r][c + 1] == "  ":
                    twoD_array[r][c + 1] = twoD_array[r][c]
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c + 1] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 1
                elif twoD_array[r][c + 1] == "*":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
            elif direction == "u":
                if twoD_array[r + 1][c] == "  ":
                    twoD_array[r + 1][c] = twoD_array[r][c]
                    twoD_array[r][c] = "  "
                elif twoD_array[r + 1][c] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 1
                elif twoD_array[r + 1][c] == "*":
                    twoD_array[r][c] = "  "
                    twoD_array[r + 1][c] = "  "
            elif direction == "d":
                if twoD_array[r - 1][c] == "  ":
                    twoD_array[r - 1][c] = twoD_array[r][c]
                    twoD_array[r][c] = "  "
                elif twoD_array[r - 1][c] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 1
                elif twoD_array[r - 1][c] == "*":
                    twoD_array[r][c] = "  "
                    twoD_array[r - 1][c] = "  "
    # Handle other directions similarly...
 
            
        elif (twoD_array[r][c] in ("b", "B")) and check_piece_upright(r, c, twoD_array):
            if direction == "l":
                if twoD_array[r][c - 1] == "  " and twoD_array[r][c - 2] == "  ":
                    twoD_array[r][c - 2] = piece
                    twoD_array[r][c - 1] = str((cs * r) + c - 2)
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c - 1] == "s" and twoD_array[r][c - 2] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 2
                elif twoD_array[r][c - 1] == "*" or twoD_array[r][c - 2] == "*":
                    twoD_array[r][c - 2] = "  "
                    twoD_array[r][c - 1] = "  "
                    twoD_array[r][c] = "  "
            elif direction == "r":
                if twoD_array[r][c + 1] == "  " and twoD_array[r][c + 2] == "  ":
                    twoD_array[r][c + 2] = str((cs * r) + c + 1)
                    twoD_array[r][c + 1] = piece
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c + 1] == "s" and twoD_array[r][c + 2] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 2
                elif twoD_array[r][c + 1] == "*" or twoD_array[r][c + 2] == "*":
                    twoD_array[r][c + 2] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r][c] = "  "
            elif direction == "u":
                if twoD_array[r + 1][c] == "  " and twoD_array[r + 2][c] == "  ":
                    twoD_array[r + 1][c] = piece
                    twoD_array[r + 2][c] = str((cs * (r + 1)) + c)
                    twoD_array[r][c] = "  "
                elif twoD_array[r + 1][c] == "s" and twoD_array[r + 1][c] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 2
                elif twoD_array[r + 1][c] == "*" or twoD_array[r + 1][c] == "*":
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 2][c] = "  "
                    twoD_array[r][c] = "  "
            elif direction == "d":
                if twoD_array[r - 1][c] == "  " and twoD_array[r - 2][c] == "  ":
                    twoD_array[r - 2][c] = piece
                    twoD_array[r - 1][c] = str((cs * (r - 2)) + c)
                    twoD_array[r][c] = "  "
                elif twoD_array[r - 1][c] == "s" and twoD_array[r - 1][c] == "s":
                    twoD_array[r][c] = "  "
                    scores[player] += 2
                elif twoD_array[r - 1][c] == "*" or twoD_array[r - 1][c] == "*":
                    twoD_array[r - 1][c] = "  "
                    twoD_array[r - 2][c] = "  "
                    twoD_array[r][c] = "  "
        #checking if lying down        
        elif (twoD_array[r][c] in ("b", "B")) or twoD_array[r -     1][c] in ("b", "B"):
            if twoD_array[r + 1][c] == str((cs * r) + c):
            #checking if vertical
                if direction == "u":
                    if twoD_array[r + 2][c] == "  ":
                        twoD_array[r + 2][c] = piece
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r - 2][c] = "  "
                    elif twoD_array[r + 2][c] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        scores[player] += 2
                    elif twoD_array[r + 2][c] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                elif direction == "r":
                    if twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r][c + 1] = piece
                        twoD_array[r + 1][c + 1] = str((cs * r) + c + 1)
                    elif twoD_array[r][c + 1] == "s" and twoD_array[r + 1][c + 1] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        scores[player] += 2
                    elif twoD_array[r][c + 1] == "*" or twoD_array[r + 1][c + 1] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r + 1][c + 1] = "  "
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  " and twoD_array[r + 1][c - 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r][c - 1] = piece
                        twoD_array[r + 1][c - 1] = str((cs * r) + c - 1)
                    elif twoD_array[r][c - 1] == "s" and twoD_array[r + 1][c - 1] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        scores[player] += 2
                    elif twoD_array[r][c - 1] == "*" or twoD_array[r + 1][c - 1] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r][c - 1] = "  "
                        twoD_array[r + 1][c - 1] = "  "
                #elif twoD_array[r][c] == "b" and (twoD_array[r + 1][c] == str((cs * r) + c)):
                elif direction == "d":
                    if twoD_array[r - 1][c] == "  ":
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r][c] = "  "
                        twoD_array[r - 1][c] = piece
                    elif twoD_array[r - 1][c] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        scores[player] += 2
                    elif twoD_array[r - 1][c] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r - 1][c] = "  "
                
            elif twoD_array[r][c + 1] == str((cs * r) + c):
                if direction == "u":
                    if twoD_array[r + 1][c] == "  " and twoD_array[r + 1][c + 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r + 1][c] = piece
                        twoD_array[r + 1][c + 1] = str((cs * (r + 1)) + c)
                    elif twoD_array[r + 1][c] == "s" and twoD_array[r + 1][c + 1] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        scores[player] += 2
                    elif twoD_array[r + 1][c] == "*" or twoD_array[r + 1][c + 1] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 1][c + 1] = "  "
                elif direction == "d":
                    if twoD_array[r - 1][c] == "  " and twoD_array[r - 1][c + 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r - 1][c] = piece
                        twoD_array[r - 1][c + 1] = str((cs * (r - 1)) + c)
                    elif twoD_array[r - 1][c] == "s" and twoD_array[r - 1][c + 1] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        scores[player] += 2
                    elif twoD_array[r - 1][c] == "*" or twoD_array[r - 1][c + 1] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r - 1][c] = "  "
                        twoD_array[r - 1][c + 1] = "  "
                elif direction == "r":
                    if twoD_array[r][c + 2] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = piece
                    elif twoD_array[r][c + 2] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        scores[player] += 2
                    elif twoD_array[r][c + 2] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c - 1] = piece
                    elif twoD_array[r][c - 1] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        #remove this line for this and the rest
                        scores[player] += 2
                    elif twoD_array[r][c - 1] == "*":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c - 1] = "  "


        #[r][c - 1] checks go here if needed        
                
        elif twoD_array[r][c] in ("c", "C") and check_piece_upright(r, c, twoD_array):
            if direction == "l":
                if twoD_array[r][c - 3] == "  " and twoD_array[r][c - 2] == "  " and twoD_array[r][c - 1] == "  ":
                    twoD_array[r][c - 1] = str((cs * r) + c - 3)
                    twoD_array[r][c - 3] = piece
                    twoD_array[r][c - 2] = str((cs * r) + c - 3)
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c - 3] == "*" or twoD_array[r][c - 2] == "*" or twoD_array[r][c - 1] == "*":
                    twoD_array[r][c - 1] = "  "
                    twoD_array[r][c - 2] = "  "
                    twoD_array[r][c - 3] = "  "
                    twoD_array[r][c] = "  "
            elif direction == "r":
                if twoD_array[r][c + 3] == "  " and twoD_array[r][c + 2] == "  " and twoD_array[r][c + 1] == "  ":
                    twoD_array[r][c + 1] = piece
                    twoD_array[r][c + 2] = str((cs * r) + c + 1)
                    twoD_array[r][c + 3] = str((cs * r) + c + 1)
                    twoD_array[r][c] = "  "
                elif twoD_array[r][c + 3] == "b" or twoD_array[r][c + 2] == "b" or twoD_array[r][c + 1] == "b":
                    #########################
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r][c + 3] = "  "
                    twoD_array[r][c + 2] = "  "
            elif direction == "u":
                if twoD_array[r + 3][c] == "  " and twoD_array[r + 2][c] == "  " and twoD_array[r + 1][c] == "  ":
                    twoD_array[r + 1][c] = piece
                    twoD_array[r + 2][c] = str((cs * (r + 1)) + c)
                    twoD_array[r + 3][c] = str((cs * (r + 1)) + c)
                    twoD_array[r][c] = "  "
                elif twoD_array[r + 3][c] == "b" or twoD_array[r + 2][c] == "b" or twoD_array[r + 1][c] == "  ":
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 2][c] = "  "
                    twoD_array[r + 3][c] = "  "
                    twoD_array[r][c] = "  "
            elif direction == "d":
                if twoD_array[r - 3][c] == "  " and twoD_array[r - 2][c] == "  " and twoD_array[r - 1][c] == "  ":
                    twoD_array[r - 3][c] = piece
                    twoD_array[r - 2][c] = str((cs * (r - 3)) + c)
                    twoD_array[r - 1][c] = str((cs * (r - 3)) + c)
                    twoD_array[r][c] = "  "  

        #checking if lying down        
        elif twoD_array[r][c] in ("c", "C") and twoD_array[r + 1][c] == str((cs * r) + c):
            if twoD_array[r + 1][c] == str((cs * r) + c) and twoD_array[r + 2][c] == str((cs * r) + c):
            #checking if vertical
                if direction == "u":
                    if twoD_array[r + 3][c] == "  ":
                        twoD_array[r + 3][c] = piece
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                    elif twoD_array[r + 3][c] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                        scores[player] += 3
                elif direction == "r":
                    if twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  " and twoD_array[r + 2][c + 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                        twoD_array[r][c + 1] = piece
                        twoD_array[r + 1][c + 1] = str((cs * r) + c + 1)
                        twoD_array[r + 2][c + 1] = str((cs * r) + c + 1)
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  " and twoD_array[r + 1][c - 1] == "  " and twoD_array[r + 2][c - 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                        twoD_array[r][c - 1] = piece
                        twoD_array[r + 1][c - 1] = str((cs * r) + c - 1)
                        twoD_array[r + 2][c - 1] = str((cs * r) + c - 1)
                #elif twoD_array[r][c] == "b" and (twoD_array[r + 1][c] == str((cs * r) + c)):
                elif direction == "d":
                    if twoD_array[r - 1][c] == "  ":
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                        twoD_array[r][c] = "  "
                        twoD_array[r - 1][c] = piece
                    elif twoD_array[r - 1][c] == "s":
                        twoD_array[r + 1][c] = "  "
                        twoD_array[r + 2][c] = "  "
                        twoD_array[r][c] = "  "
                        scores[player] += 3
                
            elif twoD_array[r][c + 1] == str((cs * r) + c) and twoD_array[r][c + 2] == str((cs * r) + c):
                if direction == "u":
                    if twoD_array[r + 1][c] == "  " and twoD_array[r + 1][c + 1] == "  " and twoD_array[r + 1][c + 2] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        twoD_array[r + 1][c] = piece
                        twoD_array[r + 1][c + 1] = str((cs * (r + 1)) + c)
                        twoD_array[r + 1][c + 2] = str((cs * (r + 1)) + c)
                elif direction == "d":
                    if twoD_array[r - 1][c] == "  " and twoD_array[r - 1][c + 1] == "  " and twoD_array[r - 1][c + 2]:
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        twoD_array[r - 1][c] = piece
                        twoD_array[r - 1][c + 1] = str((cs * (r - 1)) + c)
                        twoD_array[r - 1][c + 2] = str((cs * (r - 1)) + c)
                elif direction == "r":
                    if twoD_array[r][c + 3] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        twoD_array[r][c + 3] = piece
                    if twoD_array[r][c + 3] == "s":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        scores[player] += 3
                elif direction == "l":
                    if twoD_array[r][c - 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        twoD_array[r][c - 1] = piece
                    elif twoD_array[r][c - 1] == "  ":
                        twoD_array[r][c] = "  "
                        twoD_array[r][c + 1] = "  "
                        twoD_array[r][c + 2] = "  "
                        scores[player] += 3

        elif twoD_array[r][c] in ("d", "D"):
            if direction == "u":
                if twoD_array[r + 2][c] == "  " and twoD_array[r + 3][c] == "  " and twoD_array[r + 3][c + 1] == "  " and twoD_array[r + 2][c + 1] == "  ":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
                    twoD_array[r + 2][c] = piece    
                    twoD_array[r + 3][c] = str((cs * (r + 2)) + c)
                    twoD_array[r + 3][c + 1] = str((cs * (r + 2)) + c)
                    twoD_array[r + 2][c + 1] = str((cs * (r + 2)) + c)
                elif twoD_array[r + 2][c] == "s" and twoD_array[r + 3][c] == "s" and twoD_array[r + 3][c + 1] == "s" and twoD_array[r + 2][c + 1] == "s":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "   
            elif direction == "r":
                if twoD_array[r][c + 2] == "  " and twoD_array[r + 1][c + 2] == "  " and twoD_array[r][c + 3] == "  " and twoD_array[r + 1][c + 3] == "  ":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
                    twoD_array[r][c + 2] = piece
                    twoD_array[r + 1][c + 2] = str((cs * r) + c + 2)
                    twoD_array[r][c + 3] = str((cs * r) + c + 2)
                    twoD_array[r + 1][c + 3] = str((cs * r) + c + 2)
                elif twoD_array[r][c + 2] == "s" and twoD_array[r + 1][c + 2] == "s" and twoD_array[r][c + 3] == "s" and twoD_array[r + 1][c + 3] == "s":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
            elif direction == "l":
                if twoD_array[r][c - 2] == "  " and twoD_array[r][c - 1] == "  " and twoD_array[r + 1][c - 1] == "  " and twoD_array[r + 1][c - 2] == "  ":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
                    twoD_array[r][c - 2] = piece
                    twoD_array[r][c - 1] = str((cs * r) + c - 2)
                    twoD_array[r + 1][c - 1] = str((cs * r) + c - 2)
                    twoD_array[r + 1][c - 2] = str((cs * r) + c - 2)
                elif twoD_array[r][c - 2] == "s" and twoD_array[r][c - 1] == "s" and twoD_array[r + 1][c - 1] == "s" and twoD_array[r + 1][c - 2] == "s":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
            elif direction == "d":
                if twoD_array[r - 2][c] == "  " and twoD_array[r - 1][c] == "  " and twoD_array[r - 1][c + 1] == "  " and twoD_array[r - 2][c + 1] == "  ":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
                    twoD_array[r - 2][c] = piece
                    twoD_array[r - 1][c] = str((cs * (r - 2)) + c)
                    twoD_array[r - 1][c + 1] = str((cs * (r - 2)) + c) 
                    twoD_array[r - 2][c + 1] = str((cs * (r - 2)) + c)
                elif twoD_array[r - 2][c] == "s" and twoD_array[r - 1][c] == "s" and twoD_array[r - 1][c + 1] == "s" and twoD_array[r - 2][c + 1] == "s":
                    twoD_array[r][c] = "  "
                    twoD_array[r][c + 1] = "  "
                    twoD_array[r + 1][c] = "  "
                    twoD_array[r + 1][c + 1] = "  "
    except:
        raise IndexError("Error")
        

def read_board(row_max, col_max, stop=True):
    twoD_array = [["  " for _ in range(col_max)] for _ in range(row_max)]
    while True:
        try:
            line = stdio.readLine().strip()
        except EOFError:
            sys.exit()
        
        # Stop getting inputs
        if line == "#":
            break
        parts = line.split()
        
        # Check if 4-part input
        if len(parts) == 4:
            piece_type = parts[0]
            piece_size = parts[1]
            r = int(parts[2])
            c = int(parts[3])
        
        # Check if 3-part input
        elif len(parts) == 3:
            piece_type = parts[0] 
            r = int(parts[1])
            c = int(parts[2])
            #twoD_array[r][c] = piece_type
        
        
        else:
            # stdio.write("ERROR: Too few arguments")
            # sys.exit()
            pass
        
        # Is it a valid piece type?
        if piece_type not in pieces:
            print_errors("ERROR: Invalid object type " + piece_type, stop)
            return False
        # Is it a valid piece size?
        if piece_type != "x":
            if piece_size not in piece_sizes:
                print_errors("ERROR: Invalid piece type " + piece_size, stop)
                return False
        # is it a valid sink?
        if piece_type == "s" and piece_size not in ("1", "2"):
            print_errors("ERROR: Invalid sink type " + piece_size, stop)
            return False
        
        # Check if in range of board
        if not (0 <= r < row_max and 0 <= c < col_max):
            print_errors("ERROR: Field " + str(r) + " " + str(c) + " not on board", stop)
            return False
        
        # Add 2x2 sink
        if piece_type == "s" and piece_size == "2":
            
            # Check if ALL pieces are in sink range
            if not (check_sink_range(row_max, col_max, r, c, stop) 
                and check_sink_range(row_max, col_max, r, c + 1, stop)
                and check_sink_range(row_max, col_max, r + 1, c, stop)
                and check_sink_range(row_max, col_max, r + 1, c + 1, stop)):   
                print_errors("ERROR: Invalid sink position.", stop)  
                return False
            
            # All valid, add to board   
            elif twoD_array[r][c] == "  " and twoD_array[r + 1][c] == "  " and twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  ":
                
                for ri, ci in [(r + 1, c), (r + 1, c + 1), (r, c + 2), (r + 1, c + 2), 
                                    (r + 2, c + 1), (r + 2, c), (r + 1, c - 1), (r, c - 1)]:
                    try:
                        if twoD_array[ri][ci] == "s":
                            print_errors("ERROR: Sink cannot be next to another sink", stop)  
                            return False
                    except IndexError:
                        pass 
                
                twoD_array[r][c] = piece_size 
                twoD_array[r][c] = 's'
                twoD_array[r][c + 1] = 's'
                twoD_array[r + 1][c] = 's'
                twoD_array[r + 1][c + 1] = 's'
            else: 
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False
        # Add 1x1 sink
        elif piece_type == "s" and piece_size == "1":
            
            # Check if piece is in sink range
            if not check_sink_range(row_max, col_max, r, c, stop):
                print_errors("ERROR: Invalid sink position.", stop)
                return False
            
            # Valid, add to board 
            if twoD_array[r][c] == "  ": 

                for ri, ci in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    try:
                        if twoD_array[ri][ci] == "s":
                            print_errors("ERROR: Sink cannot be next to another sink", stop)
                            return False
                    except IndexError:
                        pass  

                twoD_array[r][c] = "s"
            else: 
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False
        
        elif piece_type == "x":
            # Valid, add to board 
            if twoD_array[r][c] == "  ":   
                twoD_array[r][c] = "x"
            else: 
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False

        # Add 1x1 player 1 piece
        elif piece_type == "l" and piece_size != "d":  
            # Check if piece is in piece range
            if not check_piece_range(row_max, col_max, r, c, stop):
                print_errors("ERROR: Invalid piece position.", stop)
                return False
            
            # Valid, add to board    
            if twoD_array[r][c] == "  ":
                twoD_array[r][c] = piece_size
            else:
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False
            
        # Add 1x1 player 2 piece
        elif piece_type == "d" and piece_size != "d":  
            # Check if piece is in piece range
            if not check_piece_range(row_max, col_max, r, c, stop):
                print_errors("ERROR: Invalid piece position.", stop)
                return False
            
            # Valid, add to board
            if twoD_array[r][c] == "  ":
                twoD_array[r][c] = piece_size.upper()
            else:
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False
       
        # Add 2x2 player 1 d-piece
        elif piece_type == "l" and piece_size == "d":
            # Check if ALL pieces are in piece range
            if not (check_piece_range(row_max, col_max, r, c, stop) 
                and check_piece_range(row_max, col_max, r, c + 1, stop)
                and check_piece_range(row_max, col_max, r + 1, c, stop)
                and check_piece_range(row_max, col_max, r + 1, c + 1, stop)):
                print_errors("ERROR: Invalid piece position.", stop)
                return False
            
            # All valid, add to board
            elif twoD_array[r][c] == "  " and twoD_array[r + 1][c] == "  " and twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  ":
                twoD_array[r][c] = piece_size
                twoD_array[r][c + 1] = str((col_max * r) + c)
                twoD_array[r + 1][c] = str((col_max * r) + c)
                twoD_array[r + 1][c + 1] = str((col_max * r) + c)
            else:
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False
            
        # Add 2x2 player 2 d-piece    
        elif piece_type == "d" and piece_size == "d":
            # Check if ALL pieces are in piece range
            if not (check_piece_range(row_max, col_max, r, c, stop) 
                and check_piece_range(row_max, col_max, r, c + 1, stop)
                and check_piece_range(row_max, col_max, r + 1, c, stop)
                and check_piece_range(row_max, col_max, r + 1, c + 1, stop)):
                print_errors("ERROR: Invalid piece position.", stop)
                return False
            
            # All valid, add to board
            elif twoD_array[r][c] == "  " and twoD_array[r + 1][c] == "  " and twoD_array[r][c + 1] == "  " and twoD_array[r + 1][c + 1] == "  ":
                twoD_array[r][c] = piece_size.upper()
                twoD_array[r][c + 1] = str((col_max * r) + c)
                twoD_array[r + 1][c] = str((col_max * r) + c)
                twoD_array[r + 1][c + 1] = str((col_max * r) + c)
            else:
                print_errors("ERROR: Field " + str(r) + " " + str(c) + " not free", stop)
                return False

        # Special pieces
        elif piece_type == "x":
            twoD_array[r][c] = " "
            twoD_array[r][c] = piece_size

    
    # atomic -> pages
    
    return twoD_array
   
def print_board(board):
    """
    Prints the given board out to the standard output in the format specified in
    the project specification.

    Args:
        board (2D array of str): The game board
        make array and update it after input has been taken in
    """
    #m = int(sys.argv[1])  #rows
    #n = int(sys.argv[2])  #colums 

    
    m = len(board)
    n = len(board[0])
    
    stdio.write("  ")
    for i in range(n):
        stdio.write(" " + (str(i) + " "))
    stdio.writeln()
    
    top_layer = "  " + "+" + ("--" + "+") * n
    stdio.writeln(top_layer)
    
    
    for i in range(m - 1, -1, -1): #[m - 1, 0]
        cell = " |"
        
        middle_layer = " " + ("|" + cell * n)
        bottom_layer = " " + ("+" + "--+" * n)
        reverse = m - 1 - i
        
        middle_layer = " |"
        for j in range(n):
            cell = board[i][j]
            if cell == "*":
                cell = "  "
            if len(cell) == 2:
                middle_layer += cell + "|"
            else:
                middle_layer += " " + cell + "|"
                
        row_number = 9 - (m - 1 - i)
        
        stdio.writeln(str(row_number) + middle_layer)
        stdio.writeln("  " + ("+" + "--+" * n))
    
        # TODO: implement this function.
        # remove the following line when you add something to this function:


def draw_game(twoD_array):
    """
    Draws the given board using standard draw.

    Args:
        board (2D array of str): The game board
    """
    # When implemented correctly, this function can be called after each move to
    # re-draw the game for the GUI.
    # remove the following line when you add something to this function:
    
    BOARD_SIZE_ROWS = len(twoD_array)
    BOARD_SIZE_COLS = len(twoD_array[0])
    stddraw.setXscale(0, BOARD_SIZE_COLS)
    stddraw.setYscale(0, BOARD_SIZE_ROWS)
    stddraw.setFontSize(12)

    for i in range(BOARD_SIZE_ROWS):
        for j in range(BOARD_SIZE_COLS - 1, -1, -1):
            x = j + 0.5
            y = i + 0.5

            if (i + j) % 2 == 0:
                stddraw.setPenColor(stddraw.WHITE)
            else:
                stddraw.setPenColor(stddraw.GRAY)
            stddraw.filledSquare(x, y, 0.5) 


            if twoD_array[i][j] in ["a", "b", "c", "d"]:
                stddraw.setPenColor(stddraw.BLUE) 
                stddraw.filledSquare(x, y, 0.55) 

                if twoD_array[i][j] in ["a", "b", "c", "d"]:
                    stddraw.setPenColor(stddraw.LIGHT_GRAY)
                stddraw.filledSquare(x, y, 0.45) 
                #try to figure out how to add the letters onto the blocks

            elif twoD_array[i][j] in ["A", "B", "C", "D"]:
                stddraw.setPenColor(stddraw.GREEN) 
                stddraw.filledSquare(x, y, 0.55) 

                if twoD_array[i][j] in ["A", "B", "C", "D"]:
                    stddraw.setPenColor(stddraw.LIGHT_GRAY)
                stddraw.filledSquare(x, y, 0.45)
            

            elif twoD_array[i][j] == "s":
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledSquare(x, y, 0.5) 

# Make your copy function
# input: twoD_array
# output: a totally new carbon-copy of twoD_array

def make_copy_of_board(twoD_array):
    row_max = len(twoD_array)
    col_max = len(twoD_array[0])

    result = [["  " for _ in range(col_max)] for _ in range(row_max)]
    
    for i in range(row_max):
        for j in range(col_max):
            result[i][j] = twoD_array[i][j]
    return result


def check_for_any_moves(twoD_array, old_2darray, player):

    rs = len(twoD_array)
    cs = len(twoD_array[0])
    for r in range(rs):
        for c in range(cs):
            for direction in directions:
                if validate_move(r, c, direction, player, twoD_array, old_2darray, stop=False):
                    return True
    
    return False
            
def game_loop(twoD_array, stop=True):
    # Game variables
    player = 0
    scores = [0, 0]
    bomb_count = 0
    turns = 0
    winner = None

    old_2darray = None

    # Run the game
    while True:
        if check_for_any_moves(twoD_array, old_2darray, player) and scores[player] > 0:
            if player == 0:
                return print_errors("Light loses", stop)
            elif player == 1:
                return print_errors("Dark loses", stop)

        # Get the move from player    
        try:
            move_input = stdio.readLine() # "row col direction"
        except EOFError:
            sys.exit()
        
        parts = move_input.split()
        r = int(parts[0])
        c = int(parts[1])
        direction = parts[2]

        if direction == "b":
            twoD_array[r][c] = "*"
            print_board(twoD_array)
        
        #Is it a valid move?
        if validate_move(r, c, direction, player, twoD_array, old_2darray, stop=False):
            
            # Valid move, do the move
            if twoD_array[r][c] in ("d", "D") and turns == 1:
                #error moving when youve already had one turn for type D 
                print_errors("ERROR: Cannot move a 2x2x2 piece on the second move", stop)
                return False
            
            elif twoD_array[r][c] in ("d", "D"):
                turns += 2
                do_move(r, c, direction, twoD_array, scores, gui_mode, player)
            else:
                if turns == 0:
                    old_2darray = make_copy_of_board(twoD_array) 
                turns += 1
                do_move(r, c, direction, twoD_array, scores, gui_mode, player)
        else:
            continue
        # Display the board
        print_board(twoD_array)
        
        # Check for winner
        if scores[player] >= 4:
            winner = player
            break

        # Update turns   
        if turns == 2:
            if player == 0:
                player = 1
            elif player == 1:
                player = 0
                
            turns = 0
            old_2darray = None
            
    # Reveal the winner
    if winner == 0:
        stdio.writeln("Light wins!")
    elif winner == 1:
        stdio.writeln("Dark wins!")

def gui_game_loop(twoD_array):
    player = 0
    scores = [0, 0]
    turns = 0
    winner = None

    old_2darray = None

    mode = "select"
    piece_r = -1
    piece_c = -1

    import math

    # Run the game
    while True:
        stddraw.clear()

        if stddraw.mousePressed():
            if mode == "select":
                piece_c = math.floor(stddraw.mouseX())
                piece_r = math.floor(stddraw.mouseY())
                stdio.writeln(
                    f"piece_r={piece_r}, piece_c={piece_c}, piece='{twoD_array[piece_r][piece_c]}'"
                )

                mode = "move"
                stdio.writeln("Move mode")
            elif mode == "move":
                c = math.floor(stddraw.mouseX())
                r = math.floor(stddraw.mouseY())

                dr = piece_r - r
                dc = piece_c - c

                direction = ""
                # Up
                if dr == -1 and dc == 0:
                    direction = "u"
                # Down
                elif dr == 1 and dc == 0:
                    direction = "d"
                # Left
                elif dr == 0 and dc == 1:
                    direction = "l"
                # Right
                elif dr == 0 and dc == -1:
                    direction = "r"
                else:
                    stdio.write("Unknown move")
                    mode = "select"
                    stdio.write("Select mode")
                    continue

                stdio.writeln(f"dr={dr}, dc={dc}")
                stdio.writeln(f"direction={direction}, new_r={r}, new_c={c}")
                do_move(piece_r, piece_c, direction, twoD_array, [0, 0], 0, 0)
                mode = "select"
                stdio.writeln("Select mode")
        # (twoD_array)
        draw_game(twoD_array) # <------ Missing `draw_game` in your code
        stddraw.show(100)

        
        
if __name__ == "__main__":
    # TODO: put logic here to check if the command-line arguments are correct,
    # and then call the game functions using these arguments. The following code
    # is a placeholder for this to give you an idea, and MUST be changed when
    # you start editing this file.
    row_max = 10
    col_max = 10
    gui_mode = 0
    
    cmd_line_parameters(stop=True)
    
    # Get initial board
    twoD_array = read_board(row_max, col_max, stop=True)
    
    '''stddraw.clear()
    stddraw.show()'''
    # Print the board
    print_board(twoD_array)

    # Run the game
    if gui_mode:
        gui_game_loop(twoD_array)
    else:
        game_loop(twoD_array, stop=True)
   