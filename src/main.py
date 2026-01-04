import pygame
from pawn import pawn_move 

pygame.init()

width = 720
height = 720
Square = height // 8
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spell Chess")

# Initialize chess board 
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

valid_moves = []
invalid_move = False 

def position_finder(index_number):
    MAX_COL = 8  # Number of columns
    x = (index_number % MAX_COL) * Square  # Column position (horizontal)
    y = (index_number // MAX_COL) * Square  # Row position (vertical)
    return x, y



# Function to convert mouse coordinates to the clicked square index
def get_square_for_position(mouse_x, mouse_y):
    col = mouse_x // Square
    row = mouse_y // Square
    index = row * 8 + col  # Index in the 1D chessboard list
    return index


def piece_move_set(mouse_x, mouse_y, player_turn):
    clicked_square_index = get_square_for_position(mouse_x, mouse_y)

    selected_piece = chess_board[clicked_square_index]
    valid_moves = []

    # Determine player color
    player_color = "white" if player_turn == 0 else "black"

    if selected_piece != 'empty_square' and player_color in selected_piece:
        # For now, just handle pawns
        if "pawn" in selected_piece:
            valid_moves = pawn_move(clicked_square_index, player_turn, chess_board)
        # You can add rook, knight, bishop, etc. here
        elif "knight" in selected_piece:
            print("knight")  # placeholder

    return clicked_square_index, valid_moves
    
        

                    
    
        



def draw_board(chess_board, selected_square=None, valid_moves=None):
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


def promotion(player_turn, clicked_square ):

  
    if player_turn == 1:
      
        chess_board[clicked_square] = "black_queen" 

    else:
        chess_board[clicked_square] = "white_queen" 







# Main loop
selected_square = None
running = True
first_clicked_square = None  # Initialize the first clicked square
player_turn = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_square, moves = piece_move_set(mouse_x, mouse_y, player_turn)
            
            clicked_piece = chess_board[clicked_square]

            # 1 If nothing is selected yet
            if selected_square is None:
                # Only select your own piece
                if clicked_piece != 'empty_square' and (
                    ("white" in clicked_piece and player_turn == 0) or
                    ("black" in clicked_piece and player_turn == 1)
                ):
                    selected_square = clicked_square
                    valid_moves = moves
                else:
                    valid_moves = []  # Clicked empty or opponent piece first

            # 2️ If a piece is already selected
            else:
                # If clicked another of same player's pieces → switch selection
                if clicked_piece != 'empty_square' and (
                    ("white" in clicked_piece and player_turn == 0) or
                    ("black" in clicked_piece and player_turn == 1)
                ):
                    selected_square = clicked_square
                    valid_moves = moves

                # If clicked on a valid move → make the move
                elif clicked_square in valid_moves:
                    chess_board[clicked_square] = chess_board[selected_square]
                    chess_board[selected_square] = 'empty_square'
                    
                    
                    if ((56 <= clicked_square <= 63) or (0 <= clicked_square <= 7)) and "pawn" in chess_board[clicked_square]:
                        promotion(player_turn, clicked_square)


                    # Switch turn
                    player_turn = 1 - player_turn

                    # Reset selection
                    selected_square = None
                    valid_moves = []

                # Invalid click → do nothing, keep selection
                else:
                    pass

    # Draw the board and highlights
    draw_board(chess_board, selected_square, valid_moves)

pygame.quit()