import pygame
rect1 = pygame.Rect((0, 0, 40, 60))
rect2 = pygame.Rect((39, 59, 50, 50))

sur = pygame.Surface((50, 50))
l = sur.get_rect()
print(type(l))
print(rect1.colliderect(rect2))

print(type(rect1))
print(rect1.bottom)
print(rect1.center)
rect1.normalize()