#Sophia Alexander
#CGT 115
#Shapes With Pygame Assignment

#Imports the pygame module
import pygame

#Initiates the pygame module
pygame.init()

screen = pygame.display.set_mode((800, 600))
rect=pygame.Rect(100,100,200,200)
pygame.draw.rect(screen,(255,0, 0), rect)
pygame.display.update()
done = False
while not done:
    events = pygame.event.get()
for event in events:
    if event.type == pygame.QUIT:
        done = True
        pygame.quit()
