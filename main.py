#Sophia Alexander
#CGT 115
#Shapes With Pygame Assignment

#Imports the pygame module.
#Had to install in the terminal first using "pip install pygame"
import pygame

#Initiates the pygame module
pygame.init()

screen = pygame.display.set_mode((1000, 800))
rect=pygame.Rect(300,300,150,100)
pygame.draw.rect(screen,(255,255,255), rect)
pygame.draw.circle(screen, (255,255,255), (100,100), (100))
pygame.display.update()
done = False
while not done:
    events = pygame.event.get()
for event in events:
    if event.type == pygame.QUIT:
        done = True
        pygame.quit()
