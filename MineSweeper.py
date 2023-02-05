import pygame
import numpy as np
 
def main():

    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Mine Sweeper")
     
    screen = pygame.display.set_mode((300,300))

    draw_board(screen, 10, 10)

    pygame.display.flip()
     
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

def draw_board(screen: pygame.Surface, width: int, height: int):
    darkGreen = pygame.Color(38, 206, 2)
    lightGreen = pygame.Color(119, 255, 90)
    startRect = pygame.Rect(0, 0, 30, 30)
    pygame.draw.rect(screen, darkGreen, startRect)
    pygame.draw.rect(screen, lightGreen, pygame.Rect(30, 0, 30, 30))

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()