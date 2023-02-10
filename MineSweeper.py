import pygame
import numpy as np

SQAURE_PIXEL_SIZE = 30
DARK_GREEN = pygame.Color(38, 206, 2)
LIGHT_GREEN = pygame.Color(119, 255, 90)
HIGHLIGHT_GREEN = pygame.Color(179, 255, 179)
DARK_BROWN = pygame.Color(210, 164, 121)
LIGHT_BROWN = pygame.Color(217, 177, 140)
HIGHLIGHT_BROWN = pygame.Color(230, 203, 179)
RED = pygame.Color(230, 0, 0)
WIDTH, HEIGHT = (10, 10)

 
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Mine Sweeper")

    
    screen = initialize_board()

    # define a variable to control the main loop
    running = True

    # Initialise clock
    clock = pygame.time.Clock()

    revealed_board = initialize_revealed_board()
    prev_x = -1
    prev_y = -1

    start = False
    mines = np.zeros((HEIGHT, WIDTH))
     
    # main loop
    while running:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        curr_x, curr_y = highlight_square(screen, revealed_board, prev_x, prev_y)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not start:
                    mines = generate_mine(curr_x, curr_y, 10)
                    print(mines)
                    start = True
                reveal_board(mines, revealed_board, curr_x, curr_y)
                draw_board(screen, revealed_board, list())
                print(revealed_board)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        prev_x, prev_y = curr_x, curr_y

####
# Initialize screen based on size passed in, and draw the board,
# return the screen. Width and height represent how many squares
# there should be. I.e. width of 10 and height of 10 is a 10x10
# board.
####
def initialize_board() -> pygame.Surface: 
    screenWidth = SQAURE_PIXEL_SIZE * WIDTH
    screenHeight = SQAURE_PIXEL_SIZE * HEIGHT
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    screen.fill(LIGHT_GREEN)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x + y) % 2 == 0:
                rect = pygame.Rect(x * SQAURE_PIXEL_SIZE, y * SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE)
                pygame.draw.rect(screen, DARK_GREEN, rect)
    pygame.display.flip()
    return screen

####
# Initialize numbers to a picture asset. Use https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
# as a guide. This function will return a list of text Surface 1-8 for later use
####
def initialize_numbers() -> list[pygame.Surface]:
    return list()

####
# Initialize revealed board. revealed board should be an int ndarray with size (width, height),
# -3 -> mine, -2 -> flag, -1 -> unrevealed, 0 - 8 -> revealed with number of surrounding mines as the number
# revealed board should start with all -1s.
####
def initialize_revealed_board() -> np.ndarray:
    return np.zeros((HEIGHT, WIDTH), dtype = np.int16) - 1

####
# Generate the mines. width and height is the size of the board, x and y is the 
# initial position user clicked, make sure no mines are populated 1 space surrending
# the initial position and the initial position. The output should be a numpy 
# array of size (width, height), and true represent mine present, false represent mine absent.
# mineNum represent the number of mines. 
####
def generate_mine(x: int, y: int, mineNum: int) -> np.ndarray:
    # get board with increase numbers based on flattened index
    board = np.arange(WIDTH*HEIGHT).reshape((HEIGHT, WIDTH))

    # masked the initial position and surrounding area
    mask = np.zeros(WIDTH*HEIGHT).reshape((HEIGHT, WIDTH))
    mask[max((y-1),0):min((y+2), HEIGHT), max((x-1),0):min((x+2), WIDTH)] = 1

    # create the masked board with random permutation of the flattened board
    masked_board = np.ma.masked_array(np.random.permutation(board.flatten()), mask=mask)

    # create mine map
    mines = np.zeros((HEIGHT, WIDTH))

    # sort the array and get index of mineNum smallest numbers of the masked array
    for flate_index in np.argsort(masked_board)[:mineNum]:
        # translate index to the mine map and set it to 1 to indicate mines
        mines[np.unravel_index(flate_index, (HEIGHT, WIDTH))] = 1
    return mines > 0.5

####
# This function determines the square mouse is at based on mouse pixel position.
# You can use pygame.mouse.get_pos() to get the mouse position. (-1,-1) means out of screen
####
def get_sqaure_index() -> tuple[int, int]:
    if not pygame.mouse.get_focused():
        return (-1, -1)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return (int(mouse_x/SQAURE_PIXEL_SIZE), int(mouse_y/SQAURE_PIXEL_SIZE))

####
# draw a square given color and index
####
def draw_square(screen: pygame.Surface, x: int, y: int, color: pygame.Color):
    rect = pygame.Rect(x * SQAURE_PIXEL_SIZE, y * SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.display.update(rect)

####
# Highlight the sqaure where the curser is at. If previous mouse position is on the same square
# as the current mouse poition, do nothing. If the curser is at a revealed location, do nothing.
# Make sure to redraw 2 potions of the screen. One to get rid of highlight. One to
# add the highlight. You can use get_sqaure_index() to get the square index mouse is at. prev_x = -1 and
# prev_y = -1 means mouse is outside of screen. Use width and height to observe if mouse is outside of 
# the screen. Return current index of the square mouse is at. (-1,-1) means outside.
####
def highlight_square(screen: pygame.Surface, revealed_board: np.ndarray, prev_x: int, prev_y: int) -> tuple[int, int]:
    curr_x, curr_y = get_sqaure_index()
    if (curr_x, curr_y) == (prev_x, prev_y):
        return (curr_x, curr_y)
    if (curr_x, curr_y) != (-1, -1):
        if revealed_board[curr_y, curr_x] > 0:
            draw_square(screen, curr_x, curr_y, HIGHLIGHT_BROWN)
        elif revealed_board[curr_y, curr_x] == -1:
            draw_square(screen, curr_x, curr_y, HIGHLIGHT_GREEN)
    if (prev_x, prev_y) != (-1, -1):
        if revealed_board[prev_y, prev_x] > 0:
            if (prev_x + prev_y) % 2 == 0:
                draw_square(screen, prev_x, prev_y, DARK_BROWN)
            else:
                draw_square(screen, prev_x, prev_y, LIGHT_BROWN)
        elif revealed_board[prev_y, prev_x] == -1:
            if (prev_x + prev_y) % 2 == 0:
                draw_square(screen, prev_x, prev_y, DARK_GREEN)
            else:
                draw_square(screen, prev_x, prev_y, LIGHT_GREEN)
    return (curr_x, curr_y)

def get_nearby_mines(mines: np.ndarray, x: int, y: int) -> int:
    return np.sum(mines[max(0, y-1):min(HEIGHT, y+2), max(0, x-1):min(WIDTH, x+2)])

####
# x and y is the user clicked location, update the revealed board, return whether current position
# is mine, if it is zero, check all nearby location by resursively calling this function
####
def reveal_board(mines: np.ndarray, revealed_board: np.ndarray, x: int, y: int) -> bool:
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return False
    if mines[y, x]:
        revealed_board[y, x] = -3
        return True
    if revealed_board[y, x] != -1:
        return False
    revealed_board[y, x] = get_nearby_mines(mines, x, y)
    if revealed_board[y, x] == 0:
        nearby_index = np.array([[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]) + np.array([x, y])
        for (curr_x, curr_y) in nearby_index:
            reveal_board(mines, revealed_board, curr_x, curr_y)
    return False

####
# draw revealed board, for now mine use red color, flag use yellow color, and 0-8 will
# use light brown and dark brown as background color. For 1-8, also draw the number on top
####
def draw_board(screen: pygame.Surface, revealed_board: np.ndarray, number_image: list[pygame.Surface]):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if revealed_board[y, x] > -1:
                if (x + y) % 2 == 0:
                    draw_square(screen, x, y, DARK_BROWN)
                else:
                    draw_square(screen, x, y, LIGHT_BROWN)
            if revealed_board[y, x] == -3:
                draw_square(screen, x, y, RED)

if __name__=="__main__":
    main()