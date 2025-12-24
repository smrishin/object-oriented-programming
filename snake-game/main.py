import pygame
from core.game import Game

pygame.init()
screen = pygame.display.set_mode((700, 500))

game = Game(screen)

game.run()

