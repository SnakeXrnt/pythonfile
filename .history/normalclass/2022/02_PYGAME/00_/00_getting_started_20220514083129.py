import pygame 

pygame.init()

screen = pygame.display.set_mode({500 , 500})

while True:
    pygame.display.flip()
    screen.fill([245,66,239])
    
    pygame.time.Clock().tick(25)