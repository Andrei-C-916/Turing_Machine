import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('TuringTrouble')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

test_surface = pygame.Surface((200,200))
test_surface.fill('white')
text_surface = test_font.render('My game', False, 'blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))
    screen.blit(text_surface, (300,50))

    pygame.display.update()
    clock.tick()

