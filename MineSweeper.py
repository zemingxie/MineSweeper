import pygame
import numpy as np
import random
 
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Mine Sweeper")

    screen = initialize_board(10, 10)
     
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
    RectSize = 30
    screenWidth = RectSize * width
    screenHeight = RectSize * height
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    screen.fill(lightGreen)
    for row in range(width):
        for col in range(row % 2, width, 2):
            pygame.draw.rect(screen, darkGreen, (col * RectSize, row*RectSize, RectSize, RectSize))
    pygame.display.flip()
    return screen

####
# Generate the mines. width and height is the size of the board, x and y is the 
# initial position user clicked, make sure no mines are populated 1 space surrending
# the initial position and the initial position. The output should be a numpy 
# array of size (width, height), and true represent mine present, false represent mine absent.
# mineNum represent the number of mines. 
####
def generate_mine(width: int, height: int, x: int, y: int, mineNum: int) -> np.ndarray:
    #board_coordinates = [(i, j) for i in range(0,width) for j in range(0, height)]
    #mine_coordinates = random.sample(board_coordinates, mineNum)  
    board = np.array([[0 for i in range(width)] for j in range(height)])
    board[x, y] = 'b'
    adj_squares = board[max((y_pos-1),0):min(height + 2, y_pos + 2), max((x_pos-1),0):min(width + 2, x_pos + 2)]
    for i in range(mineNum):
        while True:
            x_pos, y_pos = random.randint(0, width), random.randint(0,height)
            if board[y_pos, x_pos] != 'b':
                board[y_pos, x_pos] = 'b'
                break
     
if __name__=="__main__":
    main()