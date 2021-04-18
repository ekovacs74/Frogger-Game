import pygame
import os

ScreenWidth, ScreenHeight = 704, 704
WIN = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Frogger Game")

'''Colors'''
Green = (76, 163, 54)
DarkGreen = (55, 115, 40)
DarkGreen2 = (90, 135, 62)


'''Chars'''
Frogger_Image = pygame.image.load(os.path.join('Assets', 'Frogger.png'))
FroggerX, FroggerY, FroggerWidth, FroggerHeight = 250, 250, 64, 64

Frogger = pygame.transform.scale(Frogger_Image, (FroggerWidth, FroggerHeight))


'''Screen Update Speed'''
FPS = 60

def drawScreen():
    WIN.fill(DarkGreen2)

    WIN.blit(Frogger, (FroggerX, FroggerY))

    pygame.display.update()

def main():
    global FroggerY, FroggerX
    clock = pygame.time.Clock()
    truth = True
    while truth == True:
        clock.tick(FPS)
        for event in pygame.event.get():
              if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
                  truth = False
              elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_UP and FroggerY > 0:
                      FroggerY -= 64
                  elif event.key == pygame.K_LEFT and FroggerX > 0:
                      FroggerX -= 64
                  elif event.key == pygame.K_DOWN and FroggerY < ScreenHeight - FroggerHeight * 2:
                      FroggerY += 64
                  elif event.key == pygame.K_RIGHT and FroggerX < ScreenWidth - FroggerWidth * 2:
                      FroggerX += 64

        drawScreen()

        FroggerY += 1

        if FroggerY >= ScreenHeight:
            print("Game Over")
            truth = False


    pygame.quit()



main()
