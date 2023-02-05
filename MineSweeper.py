from ast import List
import pygame
import numpy as np
import random

SQAURE_PIXEL_SIZE = 30
 
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Mine Sweeper")

    width, height = (10, 10)
    screen = initialize_board(width, height)

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
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
    for row in range(width):
        for col in range(row % 2, width, 2):
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
def initialize_reveal_board(width: int, height: int) -> np.ndarray:
    return null

####
# Generate the mines. width and height is the size of the board, x and y is the 
# initial position user clicked, make sure no mines are populated 1 space surrending
# the initial position and the initial position. The output should be a numpy 
# array of size (width, height), and true represent mine present, false represent mine absent.
# mineNum represent the number of mines. 
####
def generate_mine(width: int, height: int, x: int, y: int, mineNum: int) -> np.ndarray:
    board = np.array([[0 for i in range(height)] for j in range(width)])
    board[x, y] = False
    adj_squares = board[min((y-1), 0):max((y+1),height-1), min((x-1), 0):max((x+1),width-1)]
    for i in range(mineNum):
        while True:
            x_pos, y_pos = random.randint(0, width), random.randint(0,height)
            if (board[x_pos, y_pos] != board[x, y]) and (board[x_pos, y_pos] not in adj_squares):
                board[y_pos, x_pos] = True
                break
    
    return board

####
# Highlight the sqaure where the curser is at. If the curser is at a revealed location, do nothing.
# Make sure to redraw the screen first to get rid of previous highlighted portion. You can use 
# pygame.mouse.get_pos() to get the mouse position.
####
def highlight_square(screen: pygame.Surface, revealed_board: np.ndarray):
    return null

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