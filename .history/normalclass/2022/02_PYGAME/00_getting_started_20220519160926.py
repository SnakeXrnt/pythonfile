import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("00_images\land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2*screen_rect.width,platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.x, platform_rect.y = 250-platform_rect.width/2, 500-platform_rect.height
platform_rect.midbottom = screen_rect.midbottom

def platform_move():
    platform_rect.x -= 5
    if platform_rect.centerx == 0:
        platform_rect.left = screen_rect.left
    

bird = pygame.image.load("00_images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

pipe = pygame.Rect()

def event_listener():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


while True:
	pygame.display.flip() # draw - clear - draw dst.
	
	screen.fill([245, 66, 239]) #light purple
	screen.blit(platform, platform_rect)
	platform_move()
	screen.blit(bird, bird_rect)

	pygame.time.Clock().tick(25) # 25 frames in a second
	event_listener()
 
	


