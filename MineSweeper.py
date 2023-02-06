import pygame
import numpy as np

SQAURE_PIXEL_SIZE = 30
 
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Mine Sweeper")

    width, height = (30, 40)
    screen = initialize_board(width, height)
    #generate_mine(4, 4, 2, 2, 1)

    # define a variable to control the main loop
    running = True

    # Initialise clock
    clock = pygame.time.Clock()

    prev_mouse_x = -1
    prev_mouse_y = -1
     
    # main loop
    while running:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

####
# Initialize screen based on size passed in, and draw the board,
# return the screen. Width and height represent how many squares
# there should be. I.e. width of 10 and height of 10 is a 10x10
# board.
####
def initialize_board(width: int, height: int) -> pygame.Surface: 
    darkGreen = pygame.Color(38, 206, 2)
    lightGreen = pygame.Color(119, 255, 90)
    screenWidth = SQAURE_PIXEL_SIZE * width
    screenHeight = SQAURE_PIXEL_SIZE * height
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    screen.fill(lightGreen)
    if width >= height:
        for row in range(width):
            for col in range(row % 2, width, 2):
                darkRect = pygame.Rect(col * SQAURE_PIXEL_SIZE, row * SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE)
                pygame.draw.rect(screen, darkGreen, darkRect)
    else:
        for row in range(height):
            for col in range(row % 2, height, 2):
                darkRect = pygame.Rect(col * SQAURE_PIXEL_SIZE, row * SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE, SQAURE_PIXEL_SIZE)
                pygame.draw.rect(screen, darkGreen, darkRect)
    pygame.display.flip()

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
def initialize_revealed_board(width: int, height: int) -> np.ndarray:
    return null

####
# Generate the mines. width and height is the size of the board, x and y is the 
# initial position user clicked, make sure no mines are populated 1 space surrending
# the initial position and the initial position. The output should be a numpy 
# array of size (width, height), and true represent mine present, false represent mine absent.
# mineNum represent the number of mines. 
####
def generate_mine(width: int, height: int, x: int, y: int, mineNum: int) -> np.ndarray:
    # get board with increase numbers based on flattened index
    board = np.arange(width*height).reshape((height, width))
    print(board)

    # masked the initial position and surrounding area
    mask = np.zeros(width*height).reshape((height, width))
    mask[max((x-1),0):min((x+2), height), max((y-1),0):min((y+2), width)] = 1

    # create the masked board with random permutation of the flattened board
    masked_board = np.ma.masked_array(np.random.permutation(board.flatten()), mask=mask)
    print(masked_board)

    # create mine map
    mines = np.zeros((height, width))

    # sort the array and get index of mineNum smallest numbers of the masked array
    for flate_index in np.argsort(masked_board)[:mineNum]:
        # translate index to the mine map and set it to 1 to indicate mines
        mines[np.unravel_index(flate_index, (height, width))] = 1
    return mines

####
# Highlight the sqaure where the curser is at. If previous mouse position is on the same square
# as the current mouse poition, do nothing. If the curser is at a revealed location, do nothing.
# Make sure to redraw 2 potions of the screen. One to get rid of highlight. One to
# add the highlight. You can use pygame.mouse.get_pos() to get the mouse position. prev_x = -1 and
# prev_y = -1 means mouse is outside of screen. Use width and height to observe if mouse is outside of 
# the screen. Return current index of the square mouse is at. (-1,-1) means outside.
####
def highlight_square(screen: pygame.Surface, revealed_board: np.ndarray, prev_x: int, prev_y: int, width: int, height: int) -> tuple[int, int]:
    return (-1, -1)

####
# x and y is the user clicked location, update the revealed board, return true when
# no mine is hit, return false when user clicked on mine
####
def reveal_board(mines: np.ndarray, revealed_board: np.ndarray, x: int, y: int) -> bool:
    return null

####
# draw revealed board, for now mine use red color, flag use yellow color, and 0-8 will
# use light brown and dark brown as background color. For 1-8, also draw the number on top
####
def draw_board(screen: pygame.Surface, revealed_board: np.ndarray, number_image: list[pygame.Surface]):
    return null
     
if __name__=="__main__":
    main()