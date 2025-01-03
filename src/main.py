import pygame

pygame.init()

width = 720
height = 720
Square = height // 8
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spell Chess")

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

def position_finder(index_number):
    MAX_COL = 8  # Number of columns
    x = (index_number % MAX_COL) * Square  # Column position (horizontal)
    y = (index_number // MAX_COL) * Square  # Row position (vertical)
    return x, y

def moveing_pieces(player_turn, clicked_square_index, first_clicked_square):
    if first_clicked_square is None and chess_board[clicked_square_index] != "empty_square" and player_turn in chess_board[clicked_square_index]:
        first_clicked_square = clicked_square_index
        print(f"First click at {clicked_square_index} ({chess_board[clicked_square_index]})")
        piece_type(clicked_square_index)
    elif first_clicked_square is not None and chess_board[clicked_square_index] == "empty_square":
        # Second click: Move the piece to an empty square
        print(f"Moving piece from {first_clicked_square} to {clicked_square_index}")
        chess_board[clicked_square_index] = chess_board[first_clicked_square]
        chess_board[first_clicked_square] = "empty_square"
        first_clicked_square = None  # Reset after move
        player_turn = "black" if player_turn == "white" else "white"  # Toggle turn
    elif first_clicked_square is not None and chess_board[clicked_square_index] != "empty_square":
        # Second click: Handle occupied square (do nothing for now)
        print("Space is occupied by another piece. Choose a different square.")
        first_clicked_square = None  # Reset after invalid move attempt
    
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
    
    pygame.display.update()


def piece_type(clicked_square_index):

    x, y = position_finder(clicked_square_index)
      # Convert index to row and column in the chessboard
    row = y // Square  # Row (0 to 7)
    col = x // Square  # Column (0 to 7)

    # Convert to chess notation (e.g., "a7", "h1")
    rows = "abcdefgh"
    cols = "87654321"
    square_col = cols[col]  # Column as chess letter (a-h)
    square_row = rows[row]  # Row as number (1-8)
    piece_square = square_col + square_row  # Full square (e.g., "a7")

    if "pawn" in chess_board[clicked_square_index]:
       if "black" in chess_board[clicked_square_index]:
            if row == 6:
                print("black piece selected")  

    else:
        print("not working")


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
    draw_board()

pygame.quit()


