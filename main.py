import pygame


ScreenWidth, ScreenHeight = 500, 500
WIN = pygame.display.set_mode((ScreenWidth, ScreenHeight))

'''Colors'''
Green = (76, 163, 54)
DarkGreen = (55, 115, 40)


'''Chars'''
FroggerX, FroggerY, FroggerWidth, FroggerHeight = 250, 250, 16, 16
Frogger = pygame.Rect(FroggerX, FroggerY, FroggerWidth, FroggerHeight)

def drawScreen():
    WIN.fill(Green)

    pygame.draw.rect(WIN, DarkGreen, Frogger)    
    pygame.display.update()

def main():
    truth = True
    while truth == True:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
                  truth = False
              elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_w:
                      FroggerY += 16 # :P
                  elif event.key == pygame.K_a:
                      FroggerX -= 16 # :P
                  elif event.key == pygame.K_s:
                      FroggerY -= 16 # :P
                  elif event.key == pygame.K_d:
                      FroggerX += 16 # :P
        
       drawScreen()
    
    pygame.quit()
             
    

main()
