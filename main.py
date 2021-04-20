import pygame
import os
import random

os.system("cls")

SCREENWIDTH, SCREENHEIGHT = 704, 704
WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Frogger Game")
FPS = 60 # Screen update speed

'''Colors'''
GREEN = (76, 163, 54)
DARKGREEN1 = (55, 115, 40)
DARKGREEN2 = (90, 135, 62)


'''Chars'''
Frogger_Image = pygame.image.load(os.path.join('Assets', 'Froggy.png')) # Loading image for Frogger
FroggerX, FroggerY, FroggerWidth, FroggerHeight = 320, 576, 64, 64 # Properties of Frogger

FroggerUp = pygame.transform.scale(Frogger_Image, (FroggerWidth, FroggerHeight)) # Setting frogger up for facing up
FroggerDown = pygame.transform.rotate(Frogger_Image, 180) # Setting frogger up for facing down
FroggerRight = pygame.transform.rotate(Frogger_Image, 270) # Setting frogger up for facing right
FroggerLeft = pygame.transform.rotate(Frogger_Image, 90) # Setting frogger up for facing left
Frogger = pygame.transform.scale(Frogger_Image, (FroggerWidth, FroggerHeight)) # Sacling Frogger

Bus_Image = pygame.image.load(os.path.join('Assets', 'Schoolbus.png')) # Loading image for School Bus
BusRight = pygame.transform.flip(Bus_Image, True, False) # Flips bus so it faces to the right
BusLeft = pygame.transform.flip(Bus_Image, False, False) # Flip bus so it to the left

Lane_Image = pygame.image.load(os.path.join('Assets', 'Road.png')) # Image for the road


'''Class for handling the traffic lanes'''
Lanes = {} # Dictionary for the lanes

class TrafficLane: # Creating the class for the lanes

    def __init__(self, y_level, name):

        self.name = name
        self.y_level = y_level

        if (random.randint(0,1) == 1): # Determines which direction the traffic will move
            self.direction = "right"
        else:
            self.direction = "left"



'''Class for handling the cars'''
Cars = {} # Dictionary for the cars

class Cars: # Creating the class for the cars

    def __init__(self, lane, direction, speed, carNum):

        self.lane = lane
        self.direction = direction
        self.speed = speed
        self.carNum = carNum

        imageSelector = random.randint(0,0)

        if (imageSelector == 0):
            if (self.direction == "right"):
                self.image = BusRight
            else:
                self.image = BusLeft


def drawScreen():
    WIN.fill(DARKGREEN2) # Background

    # For things on the screen (Might make a separate function)
    for item in Lanes:
        WIN.blit(Lane_Image, (0, Lanes[item][0]))

    WIN.blit(Frogger, (FroggerX, FroggerY))

    pygame.display.update() # Updates the screen



'''Main Function'''

def main():
    global Frogger, FroggerUp, FroggerDown, FroggerRight, FroggerLeft
    global FroggerY, FroggerX
    clock = pygame.time.Clock()
    GameLoop = True # Variable for the Main Game Loop

    ScreenMoveUp = 0

    LaneNum = 0 
    for y in range(0, 11): # Creating the lanes
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
                      Frogger = FroggerUp
                  elif event.key == pygame.K_LEFT and FroggerX > 0: # Button for moving left with limits
                      FroggerX -= 64
                      Frogger = FroggerLeft
                  elif event.key == pygame.K_DOWN and FroggerY < SCREENHEIGHT - FroggerHeight * 2: # Button for moving down with limits
                      FroggerY += 64
                      Frogger = FroggerDown
                  elif event.key == pygame.K_RIGHT and FroggerX < SCREENWIDTH - FroggerWidth: # Button for moving right with limits
                      FroggerX += 64
                      Frogger = FroggerRight

        drawScreen() # Draws what needs to be drawn for the game

        # Variables for next lane handling
        NextLaneNum = -1
        YLevelToBeat = 0
        AlreadyHaveLane = 0

        ScreenMoveUp += 1
        if ScreenMoveUp == 10: # Slowly moves screen elements down.

            FroggerY += 1

            for item in Lanes: # Handling the upcoming lane
                if (Lanes[item][0] > YLevelToBeat and Lanes[item][0] <= SCREENHEIGHT):
                    YLevelToBeat = Lanes[item][0]
                    NextLaneNum = item
                Lanes[item][0] +=1

            if (SCREENHEIGHT - YLevelToBeat > 0 and AlreadyHaveLane == 0): # Creating the next lane
                if (NextLaneNum == 11):
                    temp = TrafficLane(YLevelToBeat - SCREENHEIGHT, NextLaneNum + 1)
                    Lanes[temp.name] = [temp.y_level, temp.direction] 

                else:
                    temp = TrafficLane(YLevelToBeat - SCREENHEIGHT, NextLaneNum + 1)
                    Lanes[temp.name] = [temp.y_level, temp.direction] 

            ScreenMoveUp = 0

        if FroggerY >= SCREENHEIGHT: # If frogger gets below the bottom of the screen
            print("Game Over")
            GameLoop = False


    pygame.quit() # Stops pygame once main game loop is over

    for item in Lanes: # Debug
        print(str(item) + " : " + str(Lanes[item][0]))


if __name__ == "__main__":
    main() # Runs the main function
