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

     
if __name__=="__main__":
    main()