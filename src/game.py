import pygame
from const import * 
from board import Board
from pieces import *
from square import Square
import os

class Game:

    def __init__(self):
        self.board = Board()
        self.piece_textures = {}  # Cache for loaded textures

    def _load_texture(self, piece):
        """Load the texture only once and store it in the texture cache."""
        if piece.name not in self.piece_textures:
            texture_path = piece.texture
            if os.path.exists(texture_path):
                self.piece_textures[piece.name] = pygame.image.load(texture_path)
            else:
                print(f"Texture for {piece.name} not found at {texture_path}")
        return self.piece_textures.get(piece.name, None)

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Check if the square should be light or dark
                color = (234, 235, 200) if (row + col) % 2 == 0 else (119, 154, 88)
                
                # Draw the square
                rect = (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                
                if square.has_piece():
                    piece = square.piece

                    # Load the texture for the piece
                    img = self._load_texture(piece)
                    if img:
                        # Center the image on the square
                        img_center = (col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2)
                        piece.texture_rect = img.get_rect(center=img_center)

                        # Draw the piece on the board
                        surface.blit(img, piece.texture_rect)
