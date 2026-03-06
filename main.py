#Sophia Alexander
#CGT 115
#Shapes With Pygame Assignment

#Imports the pygame module.
#Had to install in the terminal first using "pip install pygame"
import pygame
import math

#Initiates the pygame module
pygame.init()

#Sets the name and size of the window
screen = pygame.display.set_mode((1000, 800))

#Defines the name, coordinates, width, and length of the rectangle
rect=pygame.Rect(385,300,180,100)
#tells the program to draw the above rectangle, named rect, and fill it in as white
pygame.draw.rect(screen,(255,255,255), rect)

#Tells the program to draw 2 circles and fill them in as white
pygame.draw.circle(screen, (255,255,255), (425,425), (30))
pygame.draw.circle(screen, (255,255,255), (525,425), (30))

#Tells the program to draw an arc on top to complete the truck
pygame.draw.arc(screen, (255,255,255), (400,260,149,80), 0, math.pi, 2)

pygame.display.update()
done = False
while not done:
    events = pygame.event.get()
for event in events:
    if event.type == pygame.QUIT:
        done = True
        pygame.quit()
