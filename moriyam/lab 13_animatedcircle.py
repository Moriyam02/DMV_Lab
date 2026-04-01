import pygame
import sys


speed = float(input("Enter circle speed (e.g., 2): "))
radius = int(input("Enter circle size (radius, e.g., 30): "))
fps = int(input("Enter frame rate (e.g., 60): "))


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")


black = (0, 0, 0)
blue = (0, 150, 255)


x, y = width // 2, height // 2


dx, dy = speed, speed

clock = pygame.time.Clock()


running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    x += dx
    y += dy

    
    if x - radius <= 0 or x + radius >= width:
        dx = -dx
    if y - radius <= 0 or y + radius >= height:
        dy = -dy

   
    screen.fill(black)
    pygame.draw.circle(screen, blue, (int(x), int(y)), radius)

    pygame.display.flip()

pygame.quit()
sys.exit()