"""
Connect 4 style game
"""

import pygame, sys

from pygame.key import set_repeat
from cell import BoardCell
from red_token import RedToken
from yellow_token import YellowToken

"""
Game Class contains main Game logic
"""

class Game:
    # Initial Game Setup
    def __init__(self) -> None:

        # Board Setup
        self.cells = pygame.sprite.Group()
        self.board_setup(rows = 6, cols = 7)
        self.turn = 0

        # Token
        self.red_tokens = pygame.sprite.Group()
        self.yellow_tokens = pygame.sprite.Group()
        self.speed = 10
        self.check_enabled = False

    def board_setup(self, rows, cols):
        for row in range(rows):
            for col in range(cols):
                x = col * SCALE + BOARD_X_OFFSET
                y = row * SCALE + BOARD_Y_OFFSET
                board_cell_sprite = BoardCell(x, y)
                print("ROW " + str(row) +  " COL " + str(col) + "X is " + str(x) + "Y is " + str(y))
                self.cells.add(board_cell_sprite)


    def generate_token(self):
        # Get Mouse Button and coords
        # Handle events
        print("INSIDE GENERATE TOKEN the turn is " + str(self.turn))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Translate x, y pos to grid coord
                clicked_col = (event.pos[0] // SCALE - (BOARD_X_OFFSET // SCALE) - 1)
                # clicked_row = (event.pos[1] // SCALE - (BOARD_Y_OFFSET // SCALE)) - # Testing clicking on a cell
                #clicked_row = (WINDOW_HEIGHT // 2) // SCALE
                x_coord = clicked_col * SCALE + (BOARD_X_OFFSET)
                y_coord = WINDOW_HEIGHT // 2 - SCALE
                #print(clicked_col, clicked_row, x_coord, y_coord)
                if self.turn == 0:
                    red_token_sprite = RedToken(x_coord, y_coord, self.speed, WINDOW_HEIGHT)
                    self.red_tokens.add(red_token_sprite)
                    self.turn = 1
                    self.check_enabled = False
                else:
                    yellow_token_sprite = YellowToken(x_coord, y_coord, self.speed, WINDOW_HEIGHT)
                    self.yellow_tokens.add(yellow_token_sprite)
                    self.turn = 0
                    self.check_enabled = True
                


    def collision_checks(self):
        if self.yellow_tokens and self.red_tokens:
            for red_token in self.red_tokens:
                print("Red token list " + str(red_token))
                if pygame.sprite.spritecollide(red_token, self.yellow_tokens, False):
                    return True
        if self.yellow_tokens and self.red_tokens:
            for yellow_token in self.yellow_tokens:
                print("Yellow token list " + str(yellow_token))
                if pygame.sprite.spritecollide(yellow_token, self.red_tokens, False):
                    return True

        
    # Game logic
    def run(self):

        # Move Token(s) when not colliding
        check_touching = self.collision_checks()
        if not check_touching and self.check_enabled:
            self.red_tokens.update()
            self.yellow_tokens.update()

        # Draw Sprites
        self.red_tokens.draw(screen)
        self.yellow_tokens.draw(screen)
        self.cells.draw(screen)

        # Generate Token
        game_over = self.generate_token()

        return game_over


"""
Program body and main loop
"""
if __name__ == '__main__':
    # Initialise Constants
    SCALE = 60
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 700
    VERSION = "1.0.0"
    BLACK = (0, 0, 0)
    BOARD_Y_OFFSET = WINDOW_HEIGHT // 2
    BOARD_X_OFFSET = WINDOW_WIDTH // 4

    # Pygame Initialise 
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Connect 4 ' + 'Version ' + VERSION)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))

    start = True
    fps = 60
    game = Game()

    # Main loop
    while start:

        # Set Frame Rate
        clock.tick(fps)

        # Erase Background
        screen.fill(BLACK)

        # Call Game Elements
        run_game = game.run()
        if run_game == False:
            start = False

        # Update display
        pygame.display.flip()


    pygame.quit() 