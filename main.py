import pygame
import os
import random

ScreenWidth, ScreenHeight = 704, 704
WIN = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Frogger Game")
FPS = 60 # Screen update speed

'''Colors'''
Green = (76, 163, 54)
DarkGreen = (55, 115, 40)
DarkGreen2 = (90, 135, 62)


'''Chars'''
Frogger_Image = pygame.image.load(os.path.join('Assets', 'Frogger.png')) # Loading image for Frogger
FroggerX, FroggerY, FroggerWidth, FroggerHeight = 320, 576, 64, 64 # Properties of Frogger
Frogger = pygame.transform.scale(Frogger_Image, (FroggerWidth, FroggerHeight)) # Sacling Frogger

Bus_Image = pygame.image.load(os.path.join('Assets', 'Schoolbus.png')) # Loading image for School Bus
BusRight = pygame.transform.flip(Bus_Image, True, False) # Flips bus so it faces to the right
BusLeft = pygame.transform.flip(Bus_Image, False, False) # Flip bus so it to the left

Lane_Image = pygame.image.load(os.path.join('Assets', 'Road.png'))


'''Class for handling the traffic lanes'''
Lanes = {}

class TrafficLane:

    def __init__(self, y_level, name):

        self.name = name
        self.y_level = y_level

        if (random.randint(0,1) == 1): # Determines which direction the traffic will move
            self.direction = "right"
        else:
            self.direction = "left"



def drawScreen():
    WIN.fill(DarkGreen2) # Background

    # For things on the screen (Might make a separate function)
    for item in Lanes:
        WIN.blit(Lane_Image, (0, Lanes[item][0]))

    WIN.blit(Frogger, (FroggerX, FroggerY))

    pygame.display.update() # Updates the screen

def main():
    global FroggerY, FroggerX
    clock = pygame.time.Clock()
    GameLoop = True # Variable for the Main Game Loop

    ScreenMoveUp = 0

    LaneNum = 0
    for y in range(0, 11):
            x = y * 64
            temp = TrafficLane(x, LaneNum)
            LaneNum += 1
            Lanes[temp.name] = [temp.y_level, temp.direction]


    while GameLoop == True: # Main Game Loop

        clock.tick(FPS)

        for event in pygame.event.get():

              if event.type == pygame.QUIT:  # Quit Event
                  GameLoop = False

              elif event.type == pygame.KEYDOWN: # Buttons Pressed

                  if event.key == pygame.K_UP and FroggerY > 0: # Button for moving up with limits
                      FroggerY -= 64
                  elif event.key == pygame.K_LEFT and FroggerX > 0: # Button for moving left with limits
                      FroggerX -= 64
                  elif event.key == pygame.K_DOWN and FroggerY < ScreenHeight - FroggerHeight * 2: # Button for moving down with limits
                      FroggerY += 64
                  elif event.key == pygame.K_RIGHT and FroggerX < ScreenWidth - FroggerWidth: # Button for moving right with limits
                      FroggerX += 64

        drawScreen() # Draws what needs to be drawn for the game

        ScreenMoveUp += 1
        if ScreenMoveUp == 10: # Slowly moves screen elements down.

            FroggerY += 1

            for item in Lanes:
                Lanes[item][0] +=1

            ScreenMoveUp = 0

        if FroggerY >= ScreenHeight: # If frogger gets below the bottom of the screen
            print("Game Over")
            GameLoop = False


    pygame.quit() # Stops pygame once main game loop is over

    for item in Lanes:
        print(str(item) + " : " + str(Lanes[item][0]))


if __name__ == "__main__":
    main() # Runs the main function
