import pygame
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroids")

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width -self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(2, 6)
asteroid_group = pygame.sprite.Group()

for i in range(6):
    x = random.randint(0, screen_width - 50)
    y = random.randint(-150, -40)
    asteroid = Asteroid(x, y)
    asteroid_group.add(asteroid)

run = True
while run:

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    asteroid_group.update()
    screen.fill((255, 255, 255))
    asteroid_group.draw(screen)

    pygame.display.update()

pygame.quit()
