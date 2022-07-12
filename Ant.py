import pygame
import math

pygame.init()
screenWidth = 1280
screenHeight = 1024
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("LangtonAnt")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
running = True

grid = []
for i in range(screenWidth):
    row = []
    for j in range(screenHeight):
        row.append(False)
    grid.append(row)

pos = [int(screenWidth / 2), int(screenHeight / 2)]
angle = 180
fps = 2
scale = 10
screen.fill(WHITE)
pygame.display.update()
while running:
    #screen.fill(BLACK)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        fps += 1
        print(fps)
    if key[pygame.K_DOWN]:
        if fps >= 1:
            fps -= 1
            print(fps)
    if not grid[pos[1]][pos[0]]:
        angle -= 90
        grid[pos[1]][pos[0]] = True
        pygame.draw.rect(screen, BLACK, [pos[0], pos[1], scale, scale])
        pos = [pos[0] + int(scale * math.cos(angle * math.pi / 180)),
               pos[1] - int(scale * math.sin(angle * math.pi / 180))]
    else:
        angle += 90
        grid[pos[1]][pos[0]] = False
        pygame.draw.rect(screen, WHITE, [pos[0], pos[1], scale, scale])
        pos = [pos[0] + int(scale * math.cos(angle * math.pi / 180)),
               pos[1] - int(scale * math.sin(angle * math.pi / 180))]

    pygame.display.update()






