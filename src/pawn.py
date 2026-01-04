import pygame 
def pawn_move(clicked_square_index, player_turn, chess_board):
    moves = []
    row = clicked_square_index // 8
    col = clicked_square_index % 8

    if player_turn == 0:  # White pawns move up
        # Capture left
        if col > 0 and "black" in chess_board[clicked_square_index - 9]:
            moves.append(clicked_square_index - 9)
        # Capture right
        if col < 7 and "black" in chess_board[clicked_square_index - 7]:
            moves.append(clicked_square_index - 7)
        # Move forward
        if chess_board[clicked_square_index - 8] == 'empty_square':
            moves.append(clicked_square_index - 8)
            # Double move from starting row
            if row == 6 and chess_board[clicked_square_index - 16] == 'empty_square':
                moves.append(clicked_square_index - 16)

    elif player_turn == 1:  # Black pawns move down (from row 1 → 7)
        # Capture left
        if col > 0 and "white" in chess_board[clicked_square_index + 7]:
            moves.append(clicked_square_index + 7)
        # Capture right
        if col < 7 and "white" in chess_board[clicked_square_index + 9]:
            moves.append(clicked_square_index + 9)
      
        # Move forward
        if chess_board[clicked_square_index + 8] == 'empty_square':
            moves.append(clicked_square_index + 8)
            # Double move from starting row (row 1 for black)
            if row == 1 and chess_board[clicked_square_index + 16] == 'empty_square':
                moves.append(clicked_square_index + 16)

    return moves


