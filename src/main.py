import pygame

pygame.init()

width = 720
height = 720
Square = height // 8
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spell Chess")

# Initialize chess board (as in your code)
chess_board = ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook",
               "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn",
               "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square",
               "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square",
               "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square",
               "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square", "empty_square",
               "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn",
               "white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook"]

piece_images = {
    "white_rook": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_rook.png"),
    "white_knight": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_knight.png"),
    "white_bishop": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_bishop.png"),
    "white_queen": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_queen.png"),
    "white_king": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_king.png"),
    "white_pawn": pygame.image.load("pixel_chess_pieces/pixel_pieces/white_pawn.png"),
    "black_rook": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_rook.png"),
    "black_knight": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_knight.png"),
    "black_bishop": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_bishop.png"),
    "black_queen": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_queen.png"),
    "black_king": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_king.png"),
    "black_pawn": pygame.image.load("pixel_chess_pieces/pixel_pieces/black_pawn.png"),
    "empty_square": pygame.Surface((Square, Square))  # Empty square is just a blank surface
}

valid_moves = []  # Track valid moves
invalid_move = False 

def position_finder(index_number):
    MAX_COL = 8  # Number of columns
    x = (index_number % MAX_COL) * Square  # Column position (horizontal)
    y = (index_number // MAX_COL) * Square  # Row position (vertical)
    return x, y

def moveing_pieces(player_turn, clicked_square_index, first_clicked_square):
    global valid_moves
    
    # First click logic
    if first_clicked_square is None and chess_board[clicked_square_index] != "empty_square" and player_turn in chess_board[clicked_square_index]:
        first_clicked_square = clicked_square_index
        print(f"First click at {clicked_square_index} ({chess_board[clicked_square_index]})")
        valid_moves = piece_type(clicked_square_index, valid_moves)  # Get valid moves for the selected piece
        print(f"Valid moves for selected piece: {valid_moves}")
    
    # Second click logic
    elif first_clicked_square is not None :
        if  player_turn in chess_board[clicked_square_index] or clicked_square_index not in valid_moves:
            valid_moves.clear()
            valid_moves = piece_type(clicked_square_index,valid_moves)
            first_clicked_square = clicked_square_index 

        elif chess_board[clicked_square_index] == "empty_square" and clicked_square_index in valid_moves:
            # If the square is empty and the move is valid
            print(f"Second click: Moving piece from {first_clicked_square} to {clicked_square_index}")
            chess_board[clicked_square_index] = chess_board[first_clicked_square]  # Move the piece
            chess_board[first_clicked_square] = "empty_square"  # Empty the original square
            first_clicked_square = None  # Reset first clicked square after move
            valid_moves = []  # Reset valid moves
            
        elif chess_board[clicked_square_index] != "empty_square":
            # If the space is occupied by another piece, reset first click
            print(f"Second click: Space occupied by {chess_board[clicked_square_index]}. Choose a different square.")
            first_clicked_square = None  # Reset the first clicked square
    
    return player_turn, first_clicked_square

# Function to convert mouse coordinates to the clicked square index
def get_square_for_position(mouse_x, mouse_y):
    col = mouse_x // Square
    row = mouse_y // Square
    index = row * 8 + col  # Index in the 1D chessboard list
    return index

def draw_board():
    for i, piece in enumerate(chess_board):
        # Get the x, y position of the square based on the index
        x, y = position_finder(i)
        
        # Alternate square colors (light green and dark green)
        if (i + (i // 8)) % 2 == 0:
            pygame.draw.rect(screen, (234, 235, 200), (x, y, Square, Square))  # Light green square
        else:
            pygame.draw.rect(screen, (119, 154, 88), (x, y, Square, Square))  # Dark green square
        
        # Draw the piece if it's not an empty square
        if piece != "empty_square":
            # Get the piece's image
            piece_image = piece_images[piece]
            
            # Resize the piece image
            scaled_piece_image = pygame.transform.scale(piece_image, (piece_image.get_width() * 2, piece_image.get_height() * 2))
            
            # Calculate the position to center the piece in the square
            piece_width = scaled_piece_image.get_width()
            piece_height = scaled_piece_image.get_height()
            
            # Center the piece within the square
            center_x = x + (Square - piece_width) // 2
            center_y = y + (Square - piece_height) // 2
            
            # Draw the centered and resized piece
            screen.blit(scaled_piece_image, (center_x , center_y - 10))
        
        # Draw the valid move dot on top of the piece (if the square is a valid move)
        if i in valid_moves:
            # Create a surface with transparency
            dot_surface = pygame.Surface((Square, Square), pygame.SRCALPHA)  # Transparent surface
            
            # Draw a transparent black circle
            pygame.draw.circle(dot_surface, (0, 0, 0, 128), (Square // 2, Square // 2), 10)  # (R, G, B, A)
            
            # Blit the surface onto the screen
            screen.blit(dot_surface, (x, y))  # Position the dot surface on top of the square


    pygame.display.update()


def piece_type(clicked_square_index, valid_move):
    x, y = position_finder(clicked_square_index)
    row = y // Square  # Row (0 to 7)
    col = x // Square  # Column (0 to 7)

    if "pawn" in chess_board[clicked_square_index]:
        if "black" in chess_board[clicked_square_index]:
            # Black pawn moves
            if row == 1:  # Black pawn on its starting position (rank 2 in chess, row index 1)
                # Can move one or two squares forward
                valid_move.append(clicked_square_index + 8)  # Move one square forward
                valid_move.append(clicked_square_index + 16)  # Move two squares forward
            elif chess_board[clicked_square_index + 8] == "empty_square":
                valid_move.append(clicked_square_index + 8)  # Can only move one square forward

            # Capture logic for black pawn
            if col > 0:  # Ensure there's space to check left capture
                if "white" in chess_board[clicked_square_index + 7]:  # Capture diagonally to the left
                    valid_move.append(clicked_square_index + 7)

            if col < 7:  # Ensure there's space to check right capture
                if "white" in chess_board[clicked_square_index + 9]:  # Capture diagonally to the right
                    valid_move.append(clicked_square_index + 9)

        elif "white" in chess_board[clicked_square_index]:
            # White pawn moves
            if row == 6:  # White pawn on its starting position (rank 7 in chess, row index 6)
                # Can move one or two squares forward
                valid_move.append(clicked_square_index - 8)  # Move one square forward
                valid_move.append(clicked_square_index - 16)  # Move two squares forward
            elif chess_board[clicked_square_index - 8] == "empty_square":
                valid_move.append(clicked_square_index - 8)  # Can only move one square forward

            # Capture logic for white pawn
            if col > 0:  # Ensure there's space to check left capture
                if "black" in chess_board[clicked_square_index - 7]:  # Capture diagonally to the left
                    valid_move.append(clicked_square_index - 7)

            if col < 7:  # Ensure there's space to check right capture
                if "black" in chess_board[clicked_square_index - 9]:  # Capture diagonally to the right
                    valid_move.append(clicked_square_index - 9)

    return valid_move


# Main loop
running = True
first_clicked_square = None  # Initialize the first clicked square
player_turn = "white"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_square_index = get_square_for_position(mouse_x, mouse_y)
            player_turn, first_clicked_square = moveing_pieces(player_turn, clicked_square_index, first_clicked_square)  # Update turn and first clicked square       
            player_turn = "black" if player_turn == "white" else "white" 
    draw_board()

pygame.quit()
